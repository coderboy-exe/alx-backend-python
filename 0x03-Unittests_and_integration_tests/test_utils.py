#!/usr/bin/env python3
""" Module fot testing Utils class """
import unittest
from unittest.mock import patch
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


class TestGetJson(unittest.TestCase):
    """ Test suite for get_json function """
    @parameterized.expand([
        ({"http://example.com"}, {"payload": True}),
        ({"http://holberton.io"}, {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """ Test case for get_json function """
        with patch('requests.get') as mock_get:
            mock_get.return_value.json.return_value = test_payload
            res = get_json(test_url)

            mock_get.assert_called_once_with(test_url)
            self.assertEqual(res, test_payload)


class TestMemoize(unittest.TestCase):
    """ Test suite for memoize function """
    def test_memoize(self):
        """ Test case for memoize function """
        class TestClass:
            """ Test class """
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mock_m:
            test_class = TestClass()
            test_class.a_property
            test_class.a_property

        mock_m.assert_called_once()
