#ifndef HEALTH_CHECKER_CORE_HPP
#define HEALTH_CHECKER_CORE_HPP

#include <string>

class HealthCheckerCore 
{
public:
    HealthCheckerCore();
    ~HealthCheckerCore();

    void start_health_check();
    void stop_health_check();
    bool is_system_healthy() const;
    
private:
    bool health_status_;
    void perform_health_check();
    void log_health_status(const std::string& status) const;
};

#endif // HEALTH_CHECKER_CORE_HPP
