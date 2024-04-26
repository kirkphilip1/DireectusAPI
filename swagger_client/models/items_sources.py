# coding: utf-8

"""
    Dynamic API Specification

    This is a dynamically generated API specification for all endpoints existing on the current project.  # noqa: E501

    OpenAPI spec version: 10.10.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ItemsSources(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'name': 'str',
        'base_url': 'str',
        'username': 'str',
        'password': 'str',
        'active': 'bool',
        'created_on': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'base_url': 'base_url',
        'username': 'username',
        'password': 'password',
        'active': 'active',
        'created_on': 'created_on'
    }

    def __init__(self, id=None, name=None, base_url=None, username=None, password=None, active=None, created_on=None):  # noqa: E501
        """ItemsSources - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._base_url = None
        self._username = None
        self._password = None
        self._active = None
        self._created_on = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if base_url is not None:
            self.base_url = base_url
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password
        if active is not None:
            self.active = active
        if created_on is not None:
            self.created_on = created_on

    @property
    def id(self):
        """Gets the id of this ItemsSources.  # noqa: E501


        :return: The id of this ItemsSources.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ItemsSources.


        :param id: The id of this ItemsSources.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ItemsSources.  # noqa: E501


        :return: The name of this ItemsSources.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ItemsSources.


        :param name: The name of this ItemsSources.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def base_url(self):
        """Gets the base_url of this ItemsSources.  # noqa: E501


        :return: The base_url of this ItemsSources.  # noqa: E501
        :rtype: str
        """
        return self._base_url

    @base_url.setter
    def base_url(self, base_url):
        """Sets the base_url of this ItemsSources.


        :param base_url: The base_url of this ItemsSources.  # noqa: E501
        :type: str
        """

        self._base_url = base_url

    @property
    def username(self):
        """Gets the username of this ItemsSources.  # noqa: E501


        :return: The username of this ItemsSources.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this ItemsSources.


        :param username: The username of this ItemsSources.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def password(self):
        """Gets the password of this ItemsSources.  # noqa: E501


        :return: The password of this ItemsSources.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this ItemsSources.


        :param password: The password of this ItemsSources.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def active(self):
        """Gets the active of this ItemsSources.  # noqa: E501


        :return: The active of this ItemsSources.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this ItemsSources.


        :param active: The active of this ItemsSources.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def created_on(self):
        """Gets the created_on of this ItemsSources.  # noqa: E501


        :return: The created_on of this ItemsSources.  # noqa: E501
        :rtype: str
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this ItemsSources.


        :param created_on: The created_on of this ItemsSources.  # noqa: E501
        :type: str
        """

        self._created_on = created_on

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ItemsSources, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ItemsSources):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other