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

class PermissionsBody1(object):
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
        'keys': 'list[str]',
        'data': 'PermissionsBody'
    }

    attribute_map = {
        'keys': 'keys',
        'data': 'data'
    }

    def __init__(self, keys=None, data=None):  # noqa: E501
        """PermissionsBody1 - a model defined in Swagger"""  # noqa: E501
        self._keys = None
        self._data = None
        self.discriminator = None
        if keys is not None:
            self.keys = keys
        if data is not None:
            self.data = data

    @property
    def keys(self):
        """Gets the keys of this PermissionsBody1.  # noqa: E501


        :return: The keys of this PermissionsBody1.  # noqa: E501
        :rtype: list[str]
        """
        return self._keys

    @keys.setter
    def keys(self, keys):
        """Sets the keys of this PermissionsBody1.


        :param keys: The keys of this PermissionsBody1.  # noqa: E501
        :type: list[str]
        """

        self._keys = keys

    @property
    def data(self):
        """Gets the data of this PermissionsBody1.  # noqa: E501


        :return: The data of this PermissionsBody1.  # noqa: E501
        :rtype: PermissionsBody
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this PermissionsBody1.


        :param data: The data of this PermissionsBody1.  # noqa: E501
        :type: PermissionsBody
        """

        self._data = data

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
        if issubclass(PermissionsBody1, dict):
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
        if not isinstance(other, PermissionsBody1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
