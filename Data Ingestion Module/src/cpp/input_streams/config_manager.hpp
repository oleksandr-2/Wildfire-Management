#ifndef CONFIG_MANAGER_HPP
#define CONFIG_MANAGER_HPP

#include <string>
#include <vector>

struct SourceConfig 
{
    std::string type;
    // Other configuration parameters
};

class ConfigManager 
{
public:
    ConfigManager(const std::string& config_file);
    std::vector<SourceConfig> get_source_configs() const;
    int get_network_port() const;
    int get_polling_interval() const;
    int get_buffer_size() const;
private:
    // Implementation details
};

#endif // CONFIG_MANAGER_HPP