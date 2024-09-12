#ifndef DATA_PROCESSOR_HPP
#define DATA_PROCESSOR_HPP

#include <string>
#include <memory>

class DataProcessor 
{
public:
    std::unique_ptr<std::string> process(const std::string& data);
    std::unique_ptr<std::string> process(std::unique_ptr<std::string> data);
};

#endif // DATA_PROCESSOR_HPP