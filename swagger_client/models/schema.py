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

class Schema(object):
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
        'version': 'int',
        'directus': 'str',
        'vendor': 'str',
        'collections': 'list[Collections]',
        'fields': 'list[Fields]',
        'relations': 'list[Relations]'
    }

    attribute_map = {
        'version': 'version',
        'directus': 'directus',
        'vendor': 'vendor',
        'collections': 'collections',
        'fields': 'fields',
        'relations': 'relations'
    }

    def __init__(self, version=None, directus=None, vendor=None, collections=None, fields=None, relations=None):  # noqa: E501
        """Schema - a model defined in Swagger"""  # noqa: E501
        self._version = None
        self._directus = None
        self._vendor = None
        self._collections = None
        self._fields = None
        self._relations = None
        self.discriminator = None
        if version is not None:
            self.version = version
        if directus is not None:
            self.directus = directus
        if vendor is not None:
            self.vendor = vendor
        if collections is not None:
            self.collections = collections
        if fields is not None:
            self.fields = fields
        if relations is not None:
            self.relations = relations

    @property
    def version(self):
        """Gets the version of this Schema.  # noqa: E501


        :return: The version of this Schema.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Schema.


        :param version: The version of this Schema.  # noqa: E501
        :type: int
        """

        self._version = version

    @property
    def directus(self):
        """Gets the directus of this Schema.  # noqa: E501


        :return: The directus of this Schema.  # noqa: E501
        :rtype: str
        """
        return self._directus

    @directus.setter
    def directus(self, directus):
        """Sets the directus of this Schema.


        :param directus: The directus of this Schema.  # noqa: E501
        :type: str
        """

        self._directus = directus

    @property
    def vendor(self):
        """Gets the vendor of this Schema.  # noqa: E501


        :return: The vendor of this Schema.  # noqa: E501
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """Sets the vendor of this Schema.


        :param vendor: The vendor of this Schema.  # noqa: E501
        :type: str
        """

        self._vendor = vendor

    @property
    def collections(self):
        """Gets the collections of this Schema.  # noqa: E501


        :return: The collections of this Schema.  # noqa: E501
        :rtype: list[Collections]
        """
        return self._collections

    @collections.setter
    def collections(self, collections):
        """Sets the collections of this Schema.


        :param collections: The collections of this Schema.  # noqa: E501
        :type: list[Collections]
        """

        self._collections = collections

    @property
    def fields(self):
        """Gets the fields of this Schema.  # noqa: E501


        :return: The fields of this Schema.  # noqa: E501
        :rtype: list[Fields]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this Schema.


        :param fields: The fields of this Schema.  # noqa: E501
        :type: list[Fields]
        """

        self._fields = fields

    @property
    def relations(self):
        """Gets the relations of this Schema.  # noqa: E501


        :return: The relations of this Schema.  # noqa: E501
        :rtype: list[Relations]
        """
        return self._relations

    @relations.setter
    def relations(self, relations):
        """Sets the relations of this Schema.


        :param relations: The relations of this Schema.  # noqa: E501
        :type: list[Relations]
        """

        self._relations = relations

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
        if issubclass(Schema, dict):
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
        if not isinstance(other, Schema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
