#ifndef FIRE_SPREAD_MODEL_HPP
#define FIRE_SPREAD_MODEL_HPP

class FireSpreadModel 
{
public:
    // Constructor to initialize the model parameters
    FireSpreadModel(double fuelMoisture, double windSpeed, double slope);

    // Method to calculate the rate of spread of the fire
    double calculateRateOfSpread(double fuelLoad, double terrainRoughness);

    // Method to calculate the intensity of the fire
    double calculateFireIntensity(double rateOfSpread, double fuelHeatContent);

    // Method to print model parameters
    void printModelParameters() const;

private:
    double fuelMoisture; // Fuel moisture content
    double windSpeed;    // Wind speed affecting the fire
    double slope;        // Slope of the terrain
};

#endif // FIRE_SPREAD_MODEL_HPP
