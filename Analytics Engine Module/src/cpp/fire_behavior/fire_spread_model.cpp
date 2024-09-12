#include "fire_spread_model.hpp"
#include <cmath>
#include <iostream>

// Define constants for the Rothermel fire spread model
const double ROTHERMEL_K = 0.01; // example constant
const double ROTHERMEL_L = 0.05; // example constant

FireSpreadModel::FireSpreadModel(double fuelMoisture, double windSpeed, double slope) 
    : fuelMoisture(fuelMoisture), windSpeed(windSpeed), slope(slope) {}

double FireSpreadModel::calculateRateOfSpread(double fuelLoad, double terrainRoughness) 
{
    // Basic implementation of Rothermel's fire spread model
    double rateOfSpread = ROTHERMEL_K * (fuelLoad / (fuelMoisture + 1)) *
        (windSpeed + ROTHERMEL_L * slope) / (terrainRoughness + 1);
    return rateOfSpread;
}

double FireSpreadModel::calculateFireIntensity(double rateOfSpread, double fuelHeatContent) 
{
    // Intensity is a function of the rate of spread and fuel heat content
    double fireIntensity = rateOfSpread * fuelHeatContent;
    return fireIntensity;
}

void FireSpreadModel::printModelParameters() const 
{
    std::cout << "Fire Spread Model Parameters:" << std::endl;
    std::cout << "Fuel Moisture: " << fuelMoisture << std::endl;
    std::cout << "Wind Speed: " << windSpeed << std::endl;
    std::cout << "Slope: " << slope << std::endl;
}

// Example usage
int main() 
{
    FireSpreadModel model(10.0, 5.0, 15.0);
    model.printModelParameters();

    double fuelLoad = 2.0;
    double terrainRoughness = 1.0;
    double rateOfSpread = model.calculateRateOfSpread(fuelLoad, terrainRoughness);
    double fireIntensity = model.calculateFireIntensity(rateOfSpread, 20.0);

    std::cout << "Rate of Spread: " << rateOfSpread << std::endl;
    std::cout << "Fire Intensity: " << fireIntensity << std::endl;

    return 0;
}
