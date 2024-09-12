#ifndef INPUT_SOURCE_HPP
#define INPUT_SOURCE_HPP

#include <string>
#include <memory>

class InputSource 
{
public:
    virtual ~InputSource() = default;
    virtual std::unique_ptr<std::string> read_data() = 0;
};

#endif // INPUT_SOURCE_HPP