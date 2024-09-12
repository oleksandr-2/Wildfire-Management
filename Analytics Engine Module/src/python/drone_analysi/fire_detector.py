import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms, models
from torch.utils.data import DataLoader
import numpy as np
from PIL import Image

class FireDetectionCNN(nn.Module):
    def __init__(self):
        super(FireDetectionCNN, self).__init__()
        # Using a pre-trained ResNet model and modifying the final layer
        self.model = models.resnet18(pretrained=True)
        num_features = self.model.fc.in_features
        self.model.fc = nn.Linear(num_features, 2)  # Assuming binary classification (fire/no fire)

    def forward(self, x):
        return self.model(x)

class FireDetector:
    def __init__(self, model_path):
        """
        Initializes the FireDetector with a trained model.

        :param model_path: Path to the trained model checkpoint
        """
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model = FireDetectionCNN().to(self.device)
        self.model.load_state_dict(torch.load(model_path, map_location=self.device))
        self.model.eval()
        
        # Define image transformations
        self.transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ])

    def predict(self, image_path):
        """
        Predicts whether the image contains fire or not.

        :param image_path: Path to the image file
        :return: Prediction result (0 for no fire, 1 for fire)
        """
        image = Image.open(image_path).convert('RGB')
        image = self.transform(image).unsqueeze(0).to(self.device)
        
        with torch.no_grad():
            output = self.model(image)
            _, predicted = torch.max(output, 1)
        
        return predicted.item()

# Example usage
if __name__ == "__main__":
    # Path to the trained model checkpoint
    model_path = 'path/to/trained_model.pth'

    # Initialize fire detector
    detector = FireDetector(model_path)

    # Path to an example image
    test_image_path = 'path/to/test_image.jpg'
    
    # Predict fire presence
    result = detector.predict(test_image_path)
    print(f'Prediction: {"Fire detected" if result == 1 else "No fire detected"}')
