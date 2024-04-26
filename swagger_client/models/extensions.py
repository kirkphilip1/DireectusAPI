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

class Extensions(object):
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
        'enabled': 'bool',
        'id': 'str',
        'folder': 'str',
        'source': 'str',
        'bundle': 'str'
    }

    attribute_map = {
        'enabled': 'enabled',
        'id': 'id',
        'folder': 'folder',
        'source': 'source',
        'bundle': 'bundle'
    }

    def __init__(self, enabled=None, id=None, folder=None, source=None, bundle=None):  # noqa: E501
        """Extensions - a model defined in Swagger"""  # noqa: E501
        self._enabled = None
        self._id = None
        self._folder = None
        self._source = None
        self._bundle = None
        self.discriminator = None
        if enabled is not None:
            self.enabled = enabled
        if id is not None:
            self.id = id
        if folder is not None:
            self.folder = folder
        if source is not None:
            self.source = source
        if bundle is not None:
            self.bundle = bundle

    @property
    def enabled(self):
        """Gets the enabled of this Extensions.  # noqa: E501


        :return: The enabled of this Extensions.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this Extensions.


        :param enabled: The enabled of this Extensions.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def id(self):
        """Gets the id of this Extensions.  # noqa: E501


        :return: The id of this Extensions.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Extensions.


        :param id: The id of this Extensions.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def folder(self):
        """Gets the folder of this Extensions.  # noqa: E501


        :return: The folder of this Extensions.  # noqa: E501
        :rtype: str
        """
        return self._folder

    @folder.setter
    def folder(self, folder):
        """Sets the folder of this Extensions.


        :param folder: The folder of this Extensions.  # noqa: E501
        :type: str
        """

        self._folder = folder

    @property
    def source(self):
        """Gets the source of this Extensions.  # noqa: E501


        :return: The source of this Extensions.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this Extensions.


        :param source: The source of this Extensions.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def bundle(self):
        """Gets the bundle of this Extensions.  # noqa: E501

        Name of the bundle the extension is in.  # noqa: E501

        :return: The bundle of this Extensions.  # noqa: E501
        :rtype: str
        """
        return self._bundle

    @bundle.setter
    def bundle(self, bundle):
        """Sets the bundle of this Extensions.

        Name of the bundle the extension is in.  # noqa: E501

        :param bundle: The bundle of this Extensions.  # noqa: E501
        :type: str
        """

        self._bundle = bundle

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
        if issubclass(Extensions, dict):
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
        if not isinstance(other, Extensions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other