#ifndef INPUT_HANDLER_HPP
#define INPUT_HANDLER_HPP

#include <boost/asio.hpp>
#include <memory>
#include <vector>
#include <thread>
#include <atomic>
#include "input_source.hpp"
#include "config_manager.hpp"
#include "data_processor.hpp"
#include "logger.hpp"


class InputHandler 
{
public:
    InputHandler(const std::string& config_file);
    ~InputHandler();

    void start();
    void stop();

private:
    void init_sources();
    void worker_thread();
    void handle_network_input();
    void start_accept();
    void handle_accept(const boost::system::error_code& error);
    void handle_client(boost::asio::ip::tcp::socket socket);

    ConfigManager config_;
    std::vector<std::unique_ptr<InputSource>> sources_;
    std::unique_ptr<DataProcessor> data_processor_;
    Logger logger_;

    boost::asio::io_service io_service_;
    boost::asio::ip::tcp::acceptor acceptor_;
    boost::asio::ip::tcp::socket socket_;

    std::vector<std::thread> worker_threads_;
    std::atomic<bool> running_;
};

#endif // INPUT_HANDLER_HPP