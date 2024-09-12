#ifndef PREPROCESSOR_CORE_HPP
#define PREPROCESSOR_CORE_HPP

#include <vector>
#include <string>

class DataPreprocessorCore 
{
public:
    DataPreprocessorCore();
    ~DataPreprocessorCore();

    void preprocess(const std::vector<std::string>& rawData, std::vector<std::string>& processedData);

private:
    // Private methods for internal data processing
    void clean_data(const std::string& rawData, std::string& cleanedData);
    void normalize_data(const std::string& cleanedData, std::string& normalizedData);
};

#endif // PREPROCESSOR_CORE_HPP
