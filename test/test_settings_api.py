# coding: utf-8

"""
    Dynamic API Specification

    This is a dynamically generated API specification for all endpoints existing on the current project.  # noqa: E501

    OpenAPI spec version: 10.10.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.settings_api import SettingsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestSettingsApi(unittest.TestCase):
    """SettingsApi unit test stubs"""

    def setUp(self):
        self.api = SettingsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_settings(self):
        """Test case for get_settings

        Retrieve Settings  # noqa: E501
        """
        pass

    def test_update_setting(self):
        """Test case for update_setting

        Update Settings  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()