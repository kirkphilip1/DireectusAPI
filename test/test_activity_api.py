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
from swagger_client.api.activity_api import ActivityApi  # noqa: E501
from swagger_client.rest import ApiException


class TestActivityApi(unittest.TestCase):
    """ActivityApi unit test stubs"""

    def setUp(self):
        self.api = ActivityApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_comment(self):
        """Test case for create_comment

        Create a Comment  # noqa: E501
        """
        pass

    def test_delete_comment(self):
        """Test case for delete_comment

        Delete a Comment  # noqa: E501
        """
        pass

    def test_get_activities(self):
        """Test case for get_activities

        List Activity Actions  # noqa: E501
        """
        pass

    def test_get_activity(self):
        """Test case for get_activity

        Retrieve an Activity Action  # noqa: E501
        """
        pass

    def test_update_comment(self):
        """Test case for update_comment

        Update a Comment  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
