#ifndef LOGGER_HPP
#define LOGGER_HPP

#include <string>

enum class LogLevel 
{
    INFO,
    WARNING,
    ERROR
};

class Logger 
{
public:
    Logger(const std::string& log_file);
    void log(LogLevel level, const std::string& message);
};

#endif // LOGGER_HPP