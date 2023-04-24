#!/usr/bin/env python3
""" Module fot testing Utils class """
import unittest
from parameterized import parameterized, parameterized_class

utils = __import__('utils')
access_nested_map = utils.access_nested_map
get_json = utils.get_json
memoize = utils.memoize


class TestAccessNestedMap(unittest.TestCase):
    """ Test class for access_nested_map function """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])

    def test_access_nested_map(self, nested_map, path, expected):
        """ Test case foer access_nested_map function """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])

    def test_access_nested_map_exception(self, nested_map, path, expected):
        """ Test case foer access_nested_map function exception"""
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)
