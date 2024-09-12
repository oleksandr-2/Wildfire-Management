#include <gtest/gtest.h>
#include "fire_spread_model.hpp"

// Test fixture for the FireSpreadModel
class FireSpreadModelTest : public ::testing::Test 
{
protected:
    FireSpreadModel model;

    // Setup and teardown methods
    void SetUp() override 
    {
        // Initialization code here
        // e.g., model.initialize();
    }

    void TearDown() override 
    {
        // Cleanup code here
    }
};

// Test the default constructor
TEST_F(FireSpreadModelTest, DefaultConstructor)
{
    EXPECT_NO_THROW({
        FireSpreadModel m;
    });
}

// Test a simple fire spread calculation
TEST_F(FireSpreadModelTest, FireSpreadCalculation) 
{
    // Set up test data
    double initialIntensity = 10.0;
    double expectedSpread = 15.0;
    
    // Initialize model
    model.setInitialIntensity(initialIntensity);
    
    // Perform calculation
    double result = model.calculateSpread();
    
    // Check if the result is as expected
    EXPECT_NEAR(result, expectedSpread, 0.1);
}

// Test fire spread with varying intensity
TEST_F(FireSpreadModelTest, VariableIntensity) 
{
    // Test for different intensity levels
    double intensity1 = 5.0;
    double intensity2 = 20.0;
    double expectedSpread1 = 8.0;
    double expectedSpread2 = 25.0;
    
    model.setInitialIntensity(intensity1);
    EXPECT_NEAR(model.calculateSpread(), expectedSpread1, 0.1);
    
    model.setInitialIntensity(intensity2);
    EXPECT_NEAR(model.calculateSpread(), expectedSpread2, 0.1);
}

// Test edge case: zero intensity
TEST_F(FireSpreadModelTest, ZeroIntensity) 
{
    model.setInitialIntensity(0.0);
    EXPECT_EQ(model.calculateSpread(), 0.0);
}

// Test invalid intensity (negative value)
TEST_F(FireSpreadModelTest, NegativeIntensity) 
{
    model.setInitialIntensity(-10.0);
    EXPECT_THROW(model.calculateSpread(), std::invalid_argument);
}

// Add more tests as needed

// Main function for running all tests
int main(int argc, char **argv) 
{
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
