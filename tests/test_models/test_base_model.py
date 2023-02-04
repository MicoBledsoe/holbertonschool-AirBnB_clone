#!/usr/bin/python3

import unittest
import uuid
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    def test_init(self):
        bm = BaseModel(my_number=42)
        self.assertEqual(bm.my_number, 42)
        self.assertIsInstance(bm.id, str)
        self.assertIsInstance(bm.created_at, datetime)
        self.assertIsInstance(bm.updated_at, datetime)
        self.assertEqual(bm.created_at, bm.updated_at)
        
    def test_str(self):
        bm = BaseModel()
        expected_str = "[BaseModel] ({}) {{'id': '{}', 'created_at': {}, 'updated_at': {}}}".format(
            bm.id, bm.id, bm.created_at, bm.updated_at)
        self.assertEqual(str(bm), expected_str)
        
    def test_save(self):
        bm = BaseModel()
        created_at = bm.created_at
        updated_at = bm.updated_at
        bm.save()
        self.assertEqual(bm.created_at, created_at)
        self.assertGreater(bm.updated_at, updated_at)
        
    def test_to_dict(self):
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertEqual(bm_dict["__class__"], "BaseModel")
        self.assertEqual(bm_dict["id"], bm.id)
        self.assertEqual(bm_dict["created_at"], bm.created_at.isoformat())
        self.assertEqual(bm_dict["updated_at"], bm.updated_at.isoformat())
        
    def test_created_at_str_input(self):
        created_at_str = "2022-02-02T02:02:02.000000"
        bm = BaseModel(created_at=created_at_str)
        self.assertEqual(bm.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f"), created_at_str)
        
    def test_updated_at_str_input(self):
        updated_at_str = "2022-02-02T02:02:02.000000"
        bm = BaseModel(updated_at=updated_at_str)
        self.assertEqual(bm.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f"), updated_at_str)

if __name__ == "__main__":
    unittest.main()

