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
from swagger_client.api.flows_api import FlowsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestFlowsApi(unittest.TestCase):
    """FlowsApi unit test stubs"""

    def setUp(self):
        self.api = FlowsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_flow(self):
        """Test case for create_flow

        Create a Flow  # noqa: E501
        """
        pass

    def test_delete_flow(self):
        """Test case for delete_flow

        Delete a Flow  # noqa: E501
        """
        pass

    def test_delete_flows(self):
        """Test case for delete_flows

        Delete Multiple Flows  # noqa: E501
        """
        pass

    def test_get_flow(self):
        """Test case for get_flow

        Retrieve a Flow  # noqa: E501
        """
        pass

    def test_get_flows(self):
        """Test case for get_flows

        List Flows  # noqa: E501
        """
        pass

    def test_update_flow(self):
        """Test case for update_flow

        Update a Flow  # noqa: E501
        """
        pass

    def test_update_flows(self):
        """Test case for update_flows

        Update Multiple Flows  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()