#!/usr/bin/env python3
""" Module contining test suites for client class """
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class

Client = __import__("client").GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ Test suite for Github Org Client class """
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_json):
        """ test case for org """
        client = Client(org_name)
        mock_json.return_value = {"payload": True}
        self.assertEqual(client.org, {"payload": True})

    def test_public_repos_url(self):
        """ Test case for _public_repos_url property """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_repos_url:
            test = {"repos_url": Client.org}
            mock_repos_url.return_value = test
            mock_client = Client(test)
            self.assertEqual(mock_client._public_repos_url, test['repos_url'])

    @patch("client.get_json")
    def test_public_repos(self, mock_json):
        """ Test case for public_repos """
        test = [{"name": "holberton"}]
        mock_json.return_value = test
        with patch("client.GithubOrgClient._public_repos_url",
                    new_callable=PropertyMock) as mock_repos:
            mock_repos.return_value = test
            mock_client = Client("holberton")
            self.assertEqual(mock_client.public_repos(), ["holberton"])
            mock_json.assert_called_once()
