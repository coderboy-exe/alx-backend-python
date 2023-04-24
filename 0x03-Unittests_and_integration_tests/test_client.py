#!/usr/bin/env python3
""" Module contining test suites for client class """
import unittest
from unittest.mock import patch
from parameterized import parameterized, parameterized_class

Client = __import__("client").GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ Test suite for Github Org Client class """
    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch("client.get_json")
    def test_org(self, org_name):
        """ test case for org """
        client = Client(org_name)
        self.assertEqual(client.org, {"payload": True})
