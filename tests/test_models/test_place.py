#!/usr/bin/python3
"""defines all unnittest tests for the models/place.py module"""
import unittest
import os
import models
import pep8
from datetime import datetime
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """unittest tests for the Place model class"""

    def test_style_check(self):
        """Test for pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/place.py'])
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

    def test_place_is_subclass_of_BaseModel(self):
        self.assertTrue(issubclass(Place().__class__, BaseModel), True)

    def test_place_for_doc(self):
        self.assertIsNotNone(Place.__doc__)

    def test_place_instantiation_no_args(self):
        """Tests the Place instantiation with no parameters"""
        self.assertEqual(Place, type(Place()))

    def test_place_instance_stored(self):
        """Tests that a new Place instance is stored"""
        self.assertIn(Place(), models.storage.all().values())

    def test_place_id(self):
        """tests the type of a Place instance id"""
        self.assertEqual(str, type(Place().id))

    def test_place_created_at_is_datetime(self):
        """test that the Place class attribute created_at is an instance
        of datetime"""
        self.assertEqual(datetime, type(Place().created_at))

    def test_place_updated_at_is_datetime(self):
        """test that the Place class attribute updated_at is an
        instance of datetime"""
        self.assertEqual(datetime, type(Place().updated_at))

    def test_place_name_attr_is_public_class_attr(self):
        """test that the Place attribute name is public class attribute"""
        model = Place()
        self.assertNotIn("name", model.__dict__)
        self.assertEqual(str, type(Place.description))
        self.assertIn("description", dir(model))

    def test_place_instance_id_is_unique(self):
        """test that the Place instances ids are unique"""
        self.assertNotEqual(Place().id, Place().id)

    def test_place_created_at_attr_are_different(self):
        """tests that the Place created_at attributes for two
            instances are different"""
        self.assertLess(Place().created_at, Place().created_at)

    def test_place_updated_at_attr_are_different(self):
        """tests that the Place updated_at attribute for two
            instances are different"""
        self.assertLess(Place().updated_at, Place().updated_at)

    def test_unused_args(self):
        """test for unused args"""
        model = Place(None)
        self.assertNotIn(None, model.__dict__.values())

    def test_place_instantiation_with_kwargs(self):
        "tests the instantiation of the Place class with kwargs"
        dt = datetime.now().isoformat()
        kwargs = {"id": "121212", "created_at": dt, "updated_at": dt}
        model = Place(**kwargs)
        self.assertEqual(model.id, "121212")
        self.assertEqual(model.created_at.isoformat(), dt)
        self.assertEqual(model.updated_at.isoformat(), dt)

    def test_place_instantiation_with_None_kwargs(self):
        """test Place instatiation with a dictionary whose values are None"""
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)

    def test_place_save_method_once(self):
        model = Place()
        updated_at_1 = model.updated_at
        model.save()
        updated_at_2 = model.updated_at
        self.assertLess(updated_at_1, updated_at_2)

    def test_place_save_method_twice(self):
        model = Place()
        updated_at_1 = model.updated_at
        model.save()
        updated_at_2 = model.updated_at
        self.assertLess(updated_at_1, updated_at_2)
        model.save()
        updated_at_3 = model.updated_at
        self.assertLess(updated_at_2, updated_at_3)

    def test_place_save_method_with_None_arg(self):
        """tests the save method with None as argument"""
        model = Place()
        with self.assertRaises(TypeError):
            model.save(None)

    def test_place_save_to_update_file(self):
        model = Place()
        model.save()
        model_id = f'{model.__class__.__name__}.{model.id}'
        with open("file.json", "r") as f:
            self.assertIn(model_id, f.read())

    def test_place_dict_type(self):
        self.assertTrue(dict, type(Place().to_dict()))

    def test_place_to_dict_has_valid_keys(self):
        model = Place()
        self.assertIn("id", model.to_dict())
        self.assertIn("created_at", model.to_dict())
        self.assertIn("updated_at", model.to_dict())
        self.assertIn("__class__", model.to_dict())

    def test_place_to_dict_has_new_attrs(self):
        model = Place()
        model.added_name = "Holberton"
        model.added_number = 12345
        self.assertEqual("Holberton", model.added_name)
        self.assertEqual(12345, model.added_number)

    def test_place_to_dict_attrs_are_str(self):
        _dict = Place().to_dict()
        self.assertEqual(str, type(_dict["id"]))
        self.assertEqual(str, type(_dict["created_at"]))
        self.assertEqual(str, type(_dict["updated_at"]))

    def test_place_correct_dict_output(self):
        model = Place()
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

    def test_place_to_dict_and_magic_dict_methods(self):
        model = Place()
        self.assertNotEqual(model.to_dict(), model.__dict__)

    def test_place_to_dict_method_with_None_arg(self):
        model = Place()
        with self.assertRaises(TypeError):
            model.to_dict(None)


if __name__ == '__main__':
    unittest.main()
