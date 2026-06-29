# test_databridge.py
"""
Tests for DataBridge module.
"""

import unittest
from databridge import DataBridge

class TestDataBridge(unittest.TestCase):
    """Test cases for DataBridge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DataBridge()
        self.assertIsInstance(instance, DataBridge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DataBridge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
