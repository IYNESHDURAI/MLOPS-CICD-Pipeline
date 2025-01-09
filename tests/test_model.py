import unittest
import sys
import os

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from model import model, accuracy

class TestModel(unittest.TestCase):
    def test_model_accuracy(self):
        # Ensure the model accuracy meets the threshold
        self.assertGreaterEqual(accuracy, 0.90, "Model accuracy is below 90%")
    
    def test_model_instance(self):
        # Ensure the model is a RandomForestClassifier instance
        from sklearn.ensemble import RandomForestClassifier
        self.assertIsInstance(model, RandomForestClassifier, "Model is not a RandomForestClassifier")

if __name__ == "__main__":
    unittest.main()
