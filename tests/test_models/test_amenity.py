#!/usr/bin/python3
"""Module for test Amenity class"""
import unittest
import json
import pep8
import datetime

from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test State class implementation"""
    def test_doc_module(self):
        """Module documentation"""
        doc = Amenity.__doc__
        self.assertGreater(len(doc), 1)
