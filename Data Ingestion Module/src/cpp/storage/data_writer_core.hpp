#ifndef DATA_WRITER_CORE_HPP
#define DATA_WRITER_CORE_HPP

#include <string>

class DataWriterCore 
{
public:
    DataWriterCore(const std::string& dbConnectionString);
    ~DataWriterCore();

    void write_to_postgresql(const std::string& table, const std::string& data);
    void write_to_mongodb(const std::string& collection, const std::string& data);

private:
    std::string dbConnectionString_;
    
    // Private methods for database connections
    void connect_to_postgresql();
    void connect_to_mongodb();
    
    // Database client handles (placeholders)
    void* postgres_client_; // PostgreSQL client handle
    void* mongodb_client_;  // MongoDB client handle

    // Private methods for writing data
    void write_data_to_postgresql(const std::string& table, const std::string& data);
    void write_data_to_mongodb(const std::string& collection, const std::string& data);
};

#endif // DATA_WRITER_CORE_HPP
