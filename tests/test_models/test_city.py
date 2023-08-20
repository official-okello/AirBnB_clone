#!/usr/bin/python3
"""defines all unnittest tests for the models/city module"""
import unittest
import os
import models
import pep8
from datetime import datetime
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """unittest tests for the City model class"""

    def test_style_check(self):
        """Test for pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/city.py'])
        self.assertEqual(p.total_errors, 0, 'fix pep8')

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp.json")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

        try:
            os.rename("tmp.json", "file.json")
        except IOError:
            pass

    def test_city_is_subclass_of_BaseModel(self):
        self.assertTrue(issubclass(City().__class__, BaseModel), True)

    def test_city_for_doc(self):
        self.assertIsNotNone(City.__doc__)

    def test_city_instantiation_no_args(self):
        """Tests the City instantiation with no parameters"""
        self.assertEqual(City, type(City()))

    def test_city_instance_stored(self):
        """Tests that a new City instance is stored"""
        self.assertIn(City(), models.storage.all().values())

    def test_city_id(self):
        """tests the type of a City instance id """
        self.assertEqual(str, type(City().id))

    def test_city_created_at_is_datetime(self):
        """test that the City attribute created_at is an instance
        of datetime """
        self.assertEqual(datetime, type(City().created_at))

    def test_city_updated_at_is_datetime(self):
        """test that the City attribute updated_at is an instance
        of datetime"""
        self.assertEqual(datetime, type(City().updated_at))

    def test_city_name_attr_is_public_class_attr(self):
        """test that the City attribute name is public class
        attribute"""
        model = City()
        self.assertNotIn("name", model.__dict__)
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(model))

    def test_city_instance_id_is_unique(self):
        """test that the City instances ids are unique"""
        self.assertNotEqual(City().id, City().id)

    def test_city_created_at_attrs_are_different(self):
        """tests that the City created_at attributes for two
            instances are different"""
        self.assertLess(City().created_at, City().created_at)

    def test_city_updated_at_attrs_are_different(self):
        """tests that the City updated_at attribute for two
            instances are different"""
        self.assertLess(City().updated_at, City().updated_at)

    def test_unused_args(self):
        """test for unused args"""
        model = City(None)
        self.assertNotIn(None, model.__dict__.values())

    def test_city_instantiation_with_kwargs(self):
        "tests the instantiation of the City class with kwargs"
        dt = datetime.now().isoformat()
        kwargs = {"id": "121212", "created_at": dt, "updated_at": dt}
        model = City(**kwargs)
        self.assertEqual(model.id, "121212")
        self.assertEqual(model.created_at.isoformat(), dt)
        self.assertEqual(model.updated_at.isoformat(), dt)

    def test_city_instantiation_with_None_kwargs(self):
        """test User instatiation with a dictionary whose values
        are None"""
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)

    def test_city_save_method_once(self):
        model = City()
        updated_at_1 = model.updated_at
        model.save()
        updated_at_2 = model.updated_at
        self.assertLess(updated_at_1, updated_at_2)

    def test_city_save_method_twice(self):
        model = City()
        updated_at_1 = model.updated_at
        model.save()
        updated_at_2 = model.updated_at
        self.assertLess(updated_at_1, updated_at_2)
        model.save()
        updated_at_3 = model.updated_at
        self.assertLess(updated_at_2, updated_at_3)

    def test_city_save_method_with_None_arg(self):
        """tests the save method with None as argument"""
        model = City()
        with self.assertRaises(TypeError):
            model.save(None)

    def test_city_save_to_update_file(self):
        model = City()
        model.save()
        model_id = f'{model.__class__.__name__}.{model.id}'
        with open("file.json", "r") as f:
            self.assertIn(model_id, f.read())

    def test_city_dict_type(self):
        self.assertTrue(dict, type(City().to_dict()))

    def test_city_to_dict_has_valid_keys(self):
        model = City()
        self.assertIn("id", model.to_dict())
        self.assertIn("created_at", model.to_dict())
        self.assertIn("updated_at", model.to_dict())
        self.assertIn("__class__", model.to_dict())

    def test_city_to_dict_has_new_attrs(self):
        model = City()
        model.added_name = "Holberton"
        model.added_number = 12345
        self.assertEqual("Holberton", model.added_name)
        self.assertEqual(12345, model.added_number)

    def test_city_to_dict_attrs_are_str(self):
        _dict = City().to_dict()
        self.assertEqual(str, type(_dict["id"]))
        self.assertEqual(str, type(_dict["created_at"]))
        self.assertEqual(str, type(_dict["updated_at"]))

    def test_city_correct_dict_output(self):
        model = City()
        dt = datetime.now()
        model.id = '121212'
        model.created_at = model.updated_at = dt

        new_dict = {
            'id': '121212',
            '__class__': model.__class__.__name__,
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
        }
        self.assertEqual(model.to_dict(), new_dict)

    def test_city_to_dict_and_magic_dict_methods(self):
        model = City()
        self.assertNotEqual(model.to_dict(), model.__dict__)

    def test_city_to_dict_method_with_None_arg(self):
        model = City()
        with self.assertRaises(TypeError):
            model.to_dict(None)


if __name__ == '__main__':
    unittest.main()
