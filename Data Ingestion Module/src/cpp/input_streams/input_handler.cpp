#include "input_handler.hpp"
#include "network_source.hpp"
#include "file_source.hpp"
#include "sensor_source.hpp"
#include <stdexcept>


InputHandler::InputHandler(const std::string& config_file)
    : config_(config_file),
      data_processor_(std::make_unique<DataProcessor>()),
      logger_("input_handler.log"),
      acceptor_(io_service_, boost::asio::ip::tcp::endpoint(boost::asio::ip::tcp::v4(), config_.get_network_port())),
      socket_(io_service_),
      running_(false)
{
    init_sources();
}

InputHandler::~InputHandler() 
{
    stop();
}

void InputHandler::start() 
{
    if (running_) 
    {
        logger_.log(LogLevel::WARNING, "InputHandler is already running");
        return;
    }

    running_ = true;
    
    // Start worker threads for each source
    for (const auto& source : sources_) 
    {
        worker_threads_.emplace_back(&InputHandler::worker_thread, this);
    }

    // Start network input handling
    worker_threads_.emplace_back(&InputHandler::handle_network_input, this);

    logger_.log(LogLevel::INFO, "InputHandler started");
}

void InputHandler::stop() 
{
    if (!running_) 
    {
        logger_.log(LogLevel::WARNING, "InputHandler is not running");
        return;
    }

    running_ = false;
    io_service_.stop();

    for (auto& thread : worker_threads_) 
    {
        if (thread.joinable()) 
        {
            thread.join();
        }
    }

    worker_threads_.clear();
    logger_.log(LogLevel::INFO, "InputHandler stopped");
}

void InputHandler::init_sources() 
{
    for (const auto& source_config : config_.get_source_configs()) 
    {
        try 
        {
            if (source_config.type == "network") 
            {
                sources_.push_back(std::make_unique<NetworkSource>(source_config));
            } else if (source_config.type == "file") 
            {
                sources_.push_back(std::make_unique<FileSource>(source_config));
            } else if (source_config.type == "sensor") 
            {
                sources_.push_back(std::make_unique<SensorSource>(source_config));
            } else {
                throw std::runtime_error("Unknown source type: " + source_config.type);
            }
        } catch (const std::exception& e) 
        {
            logger_.log(LogLevel::ERROR, "Failed to initialize source: " + std::string(e.what()));
        }
    }
}

void InputHandler::worker_thread() 
{
    while (running_) {
        for (const auto& source : sources_) 
        {
            try {
                auto data = source->read_data();
                if (data) 
                {
                    auto processed_data = data_processor_->process(data);
                    // TODO: Send processed_data to other modules (e.g., Analytics Engine)
                }
            } catch (const std::exception& e) 
            {
                logger_.log(LogLevel::ERROR, "Error processing data: " + std::string(e.what()));
            }
        }
        std::this_thread::sleep_for(std::chrono::milliseconds(config_.get_polling_interval()));
    }
}

void InputHandler::handle_network_input() 
{
    start_accept();
    io_service_.run();
}

void InputHandler::start_accept() 
{
    acceptor_.async_accept(socket_,
        [this](const boost::system::error_code& error) 
        {
            handle_accept(error);
        });
}

void InputHandler::handle_accept(const boost::system::error_code& error) 
{
    if (!error) 
    {
        std::thread(&InputHandler::handle_client, this, std::move(socket_)).detach();
    } else {
        logger_.log(LogLevel::ERROR, "Accept error: " + error.message());
    }
    start_accept();
}

void InputHandler::handle_client(boost::asio::ip::tcp::socket socket) 
{
    try {
        std::vector<char> data(config_.get_buffer_size());
        while (running_) 
        {
            boost::system::error_code error;
            std::size_t length = socket.read_some(boost::asio::buffer(data), error);

            if (error == boost::asio::error::eof) 
            {
                break;  // Connection closed cleanly by peer
            } else if (error) 
            {
                throw boost::system::system_error(error);  // Some other error
            }

            auto processed_data = data_processor_->process(std::string(data.begin(), data.begin() + length));
            // TODO: Send processed_data to other modules (e.g., Analytics Engine)
        }
    } catch (std::exception& e) 
    {
        logger_.log(LogLevel::ERROR, "Exception in client handler: " + std::string(e.what()));
    }
}