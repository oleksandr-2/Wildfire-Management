#ifndef IMAGE_PROCESSOR_HPP
#define IMAGE_PROCESSOR_HPP

#include <opencv2/opencv.hpp>

class ImageProcessor 
{
public:
    ImageProcessor(); // Constructor
    void processImage(const cv::Mat& image); // Method to process an image
    // Add other public methods here

private:
    // Add private members and methods here
};

#endif // IMAGE_PROCESSOR_HPP
