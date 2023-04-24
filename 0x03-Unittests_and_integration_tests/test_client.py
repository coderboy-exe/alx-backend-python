#!/usr/bin/env python3
""" Module contining test suites for client class """
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class


Client = __import__("client").GithubOrgClient
TEST_PAYLOAD = __import__("fixtures").TEST_PAYLOAD


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

    @parameterized.expand([
        ({'license': {'key': "my_license"}}, "my_license", True),
        ({'license': {'key': "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, key, status):
        """ Test case for has_license function """
        test_client = Client("holberton")
        self.assertEqual(test_client.has_license(repo, key), status)


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    TEST_PAYLOAD,)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Test suite for GithubOrgClient class """

    @classmethod
    def setUpClass(cls):
        """ setup test suite """
        cls.get_patcher = patch("requests.get")
        cls.mock_method = cls.get_patcher.start()

    def get_side_effect(self):
        """ side_effect getter function """
        self.mock_method.return_value.json.side_effect = [
            self.org_payload,
            self.repos_payload,
        ]

    def test_public_repos(self):
        """ Test case for public_repos method """
        self.get_side_effect()
        test_client = Client("holberton")
        repos = test_client.public_repos()
        self.assertEqual(repos, self.expected_repos)

    def test_public_repos_with_license(self):
        """ Test case for public repos with a specific license """
        self.get_side_effect()
        test_client = Client("holberton")
        repos = test_client.public_repos("apache-2.0")
        self.assertEqual(repos, self.apache2_repos)

    @classmethod
    def tearDownClass(cls):
        """ tear down test suite """
        cls.get_patcher.stop()
