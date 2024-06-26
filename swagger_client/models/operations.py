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

class Operations(object):
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
        'key': 'str',
        'type': 'str',
        'position_x': 'int',
        'position_y': 'int',
        'options': 'object',
        'resolve': 'OneOfOperationsResolve',
        'reject': 'OneOfOperationsReject',
        'flow': 'OneOfOperationsFlow',
        'date_created': 'datetime',
        'user_created': 'OneOfOperationsUserCreated'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'key': 'key',
        'type': 'type',
        'position_x': 'position_x',
        'position_y': 'position_y',
        'options': 'options',
        'resolve': 'resolve',
        'reject': 'reject',
        'flow': 'flow',
        'date_created': 'date_created',
        'user_created': 'user_created'
    }

    def __init__(self, id=None, name=None, key=None, type=None, position_x=None, position_y=None, options=None, resolve=None, reject=None, flow=None, date_created=None, user_created=None):  # noqa: E501
        """Operations - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._key = None
        self._type = None
        self._position_x = None
        self._position_y = None
        self._options = None
        self._resolve = None
        self._reject = None
        self._flow = None
        self._date_created = None
        self._user_created = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if key is not None:
            self.key = key
        if type is not None:
            self.type = type
        if position_x is not None:
            self.position_x = position_x
        if position_y is not None:
            self.position_y = position_y
        if options is not None:
            self.options = options
        if resolve is not None:
            self.resolve = resolve
        if reject is not None:
            self.reject = reject
        if flow is not None:
            self.flow = flow
        if date_created is not None:
            self.date_created = date_created
        if user_created is not None:
            self.user_created = user_created

    @property
    def id(self):
        """Gets the id of this Operations.  # noqa: E501

        Unique identifier for the operation.  # noqa: E501

        :return: The id of this Operations.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Operations.

        Unique identifier for the operation.  # noqa: E501

        :param id: The id of this Operations.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Operations.  # noqa: E501

        The name of the operation.  # noqa: E501

        :return: The name of this Operations.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Operations.

        The name of the operation.  # noqa: E501

        :param name: The name of this Operations.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def key(self):
        """Gets the key of this Operations.  # noqa: E501

        Key for the operation. Must be unique within a given flow.  # noqa: E501

        :return: The key of this Operations.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this Operations.

        Key for the operation. Must be unique within a given flow.  # noqa: E501

        :param key: The key of this Operations.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def type(self):
        """Gets the type of this Operations.  # noqa: E501

        Type of operation. One of `log`, `mail`, `notification`, `create`, `read`, `request`, `sleep`, `transform`, `trigger`, `condition`, or any type of custom operation extensions.  # noqa: E501

        :return: The type of this Operations.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Operations.

        Type of operation. One of `log`, `mail`, `notification`, `create`, `read`, `request`, `sleep`, `transform`, `trigger`, `condition`, or any type of custom operation extensions.  # noqa: E501

        :param type: The type of this Operations.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def position_x(self):
        """Gets the position_x of this Operations.  # noqa: E501

        Position of the operation on the X axis within the flow workspace.  # noqa: E501

        :return: The position_x of this Operations.  # noqa: E501
        :rtype: int
        """
        return self._position_x

    @position_x.setter
    def position_x(self, position_x):
        """Sets the position_x of this Operations.

        Position of the operation on the X axis within the flow workspace.  # noqa: E501

        :param position_x: The position_x of this Operations.  # noqa: E501
        :type: int
        """

        self._position_x = position_x

    @property
    def position_y(self):
        """Gets the position_y of this Operations.  # noqa: E501

        Position of the operation on the Y axis within the flow workspace.  # noqa: E501

        :return: The position_y of this Operations.  # noqa: E501
        :rtype: int
        """
        return self._position_y

    @position_y.setter
    def position_y(self, position_y):
        """Sets the position_y of this Operations.

        Position of the operation on the Y axis within the flow workspace.  # noqa: E501

        :param position_y: The position_y of this Operations.  # noqa: E501
        :type: int
        """

        self._position_y = position_y

    @property
    def options(self):
        """Gets the options of this Operations.  # noqa: E501

        Options depending on the type of the operation.  # noqa: E501

        :return: The options of this Operations.  # noqa: E501
        :rtype: object
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this Operations.

        Options depending on the type of the operation.  # noqa: E501

        :param options: The options of this Operations.  # noqa: E501
        :type: object
        """

        self._options = options

    @property
    def resolve(self):
        """Gets the resolve of this Operations.  # noqa: E501

        The operation triggered when the current operation succeeds (or `then` logic of a condition operation).  # noqa: E501

        :return: The resolve of this Operations.  # noqa: E501
        :rtype: OneOfOperationsResolve
        """
        return self._resolve

    @resolve.setter
    def resolve(self, resolve):
        """Sets the resolve of this Operations.

        The operation triggered when the current operation succeeds (or `then` logic of a condition operation).  # noqa: E501

        :param resolve: The resolve of this Operations.  # noqa: E501
        :type: OneOfOperationsResolve
        """

        self._resolve = resolve

    @property
    def reject(self):
        """Gets the reject of this Operations.  # noqa: E501

        The operation triggered when the current operation fails (or `otherwise` logic of a condition operation).  # noqa: E501

        :return: The reject of this Operations.  # noqa: E501
        :rtype: OneOfOperationsReject
        """
        return self._reject

    @reject.setter
    def reject(self, reject):
        """Sets the reject of this Operations.

        The operation triggered when the current operation fails (or `otherwise` logic of a condition operation).  # noqa: E501

        :param reject: The reject of this Operations.  # noqa: E501
        :type: OneOfOperationsReject
        """

        self._reject = reject

    @property
    def flow(self):
        """Gets the flow of this Operations.  # noqa: E501


        :return: The flow of this Operations.  # noqa: E501
        :rtype: OneOfOperationsFlow
        """
        return self._flow

    @flow.setter
    def flow(self, flow):
        """Sets the flow of this Operations.


        :param flow: The flow of this Operations.  # noqa: E501
        :type: OneOfOperationsFlow
        """

        self._flow = flow

    @property
    def date_created(self):
        """Gets the date_created of this Operations.  # noqa: E501

        Timestamp in ISO8601 when the operation was created.  # noqa: E501

        :return: The date_created of this Operations.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this Operations.

        Timestamp in ISO8601 when the operation was created.  # noqa: E501

        :param date_created: The date_created of this Operations.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def user_created(self):
        """Gets the user_created of this Operations.  # noqa: E501

        The user who created the operation.  # noqa: E501

        :return: The user_created of this Operations.  # noqa: E501
        :rtype: OneOfOperationsUserCreated
        """
        return self._user_created

    @user_created.setter
    def user_created(self, user_created):
        """Sets the user_created of this Operations.

        The user who created the operation.  # noqa: E501

        :param user_created: The user_created of this Operations.  # noqa: E501
        :type: OneOfOperationsUserCreated
        """

        self._user_created = user_created

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
        if issubclass(Operations, dict):
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
        if not isinstance(other, Operations):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
