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
from swagger_client.api.users_api import UsersApi  # noqa: E501
from swagger_client.rest import ApiException


class TestUsersApi(unittest.TestCase):
    """UsersApi unit test stubs"""

    def setUp(self):
        self.api = UsersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_accept_invite(self):
        """Test case for accept_invite

        Accept User Invite  # noqa: E501
        """
        pass

    def test_create_user(self):
        """Test case for create_user

        Create a User  # noqa: E501
        """
        pass

    def test_delete_user(self):
        """Test case for delete_user

        Delete a User  # noqa: E501
        """
        pass

    def test_delete_users(self):
        """Test case for delete_users

        Delete Multiple Users  # noqa: E501
        """
        pass

    def test_get_me(self):
        """Test case for get_me

        Retrieve Current User  # noqa: E501
        """
        pass

    def test_get_user(self):
        """Test case for get_user

        Retrieve a User  # noqa: E501
        """
        pass

    def test_get_users(self):
        """Test case for get_users

        List Users  # noqa: E501
        """
        pass

    def test_invite(self):
        """Test case for invite

        Invite User(s)  # noqa: E501
        """
        pass

    def test_me_tfa_disable(self):
        """Test case for me_tfa_disable

        Disable 2FA  # noqa: E501
        """
        pass

    def test_me_tfa_enable(self):
        """Test case for me_tfa_enable

        Enable 2FA  # noqa: E501
        """
        pass

    def test_update_last_used_page_me(self):
        """Test case for update_last_used_page_me

        Update Last Page  # noqa: E501
        """
        pass

    def test_update_me(self):
        """Test case for update_me

        Update Current User  # noqa: E501
        """
        pass

    def test_update_user(self):
        """Test case for update_user

        Update a User  # noqa: E501
        """
        pass

    def test_update_users(self):
        """Test case for update_users

        Update Multiple Users  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
