#include "preprocessor_core.hpp"
#include <algorithm>
#include <cctype>
#include <iostream>

DataPreprocessorCore::DataPreprocessorCore() 
{
    // Initialization code if needed
}

DataPreprocessorCore::~DataPreprocessorCore() 
{
    // Cleanup code if needed
}

void DataPreprocessorCore::preprocess(const std::vector<std::string>& rawData, std::vector<std::string>& processedData) 
{
    processedData.clear();
    for (const auto& data : rawData) 
    {
        std::string cleanedData;
        clean_data(data, cleanedData);

        std::string normalizedData;
        normalize_data(cleanedData, normalizedData);

        processedData.push_back(normalizedData);
    }
}

void DataPreprocessorCore::clean_data(const std::string& rawData, std::string& cleanedData) 
{
    // Example cleaning: Remove whitespace
    cleanedData = rawData;
    cleanedData.erase(std::remove_if(cleanedData.begin(), cleanedData.end(), ::isspace), cleanedData.end());
}

void DataPreprocessorCore::normalize_data(const std::string& cleanedData, std::string& normalizedData) 
{
    // Example normalization: Convert to lowercase
    normalizedData = cleanedData;
    std::transform(normalizedData.begin(), normalizedData.end(), normalizedData.begin(), ::tolower);
}
