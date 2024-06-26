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

class Flows(object):
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
        'icon': 'str',
        'color': 'str',
        'description': 'str',
        'status': 'str',
        'trigger': 'str',
        'accountability': 'str',
        'options': 'object',
        'operation': 'OneOfFlowsOperation',
        'date_created': 'datetime',
        'user_created': 'OneOfFlowsUserCreated',
        'operations': 'list[OneOfFlowsOperationsItems]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'icon': 'icon',
        'color': 'color',
        'description': 'description',
        'status': 'status',
        'trigger': 'trigger',
        'accountability': 'accountability',
        'options': 'options',
        'operation': 'operation',
        'date_created': 'date_created',
        'user_created': 'user_created',
        'operations': 'operations'
    }

    def __init__(self, id=None, name=None, icon=None, color=None, description=None, status='active', trigger=None, accountability=None, options=None, operation=None, date_created=None, user_created=None, operations=None):  # noqa: E501
        """Flows - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._icon = None
        self._color = None
        self._description = None
        self._status = None
        self._trigger = None
        self._accountability = None
        self._options = None
        self._operation = None
        self._date_created = None
        self._user_created = None
        self._operations = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if icon is not None:
            self.icon = icon
        if color is not None:
            self.color = color
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if trigger is not None:
            self.trigger = trigger
        if accountability is not None:
            self.accountability = accountability
        if options is not None:
            self.options = options
        if operation is not None:
            self.operation = operation
        if date_created is not None:
            self.date_created = date_created
        if user_created is not None:
            self.user_created = user_created
        if operations is not None:
            self.operations = operations

    @property
    def id(self):
        """Gets the id of this Flows.  # noqa: E501

        Unique identifier for the flow.  # noqa: E501

        :return: The id of this Flows.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Flows.

        Unique identifier for the flow.  # noqa: E501

        :param id: The id of this Flows.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Flows.  # noqa: E501

        The name of the flow.  # noqa: E501

        :return: The name of this Flows.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Flows.

        The name of the flow.  # noqa: E501

        :param name: The name of this Flows.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def icon(self):
        """Gets the icon of this Flows.  # noqa: E501

        Icon displayed in the Admin App for the flow.  # noqa: E501

        :return: The icon of this Flows.  # noqa: E501
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this Flows.

        Icon displayed in the Admin App for the flow.  # noqa: E501

        :param icon: The icon of this Flows.  # noqa: E501
        :type: str
        """

        self._icon = icon

    @property
    def color(self):
        """Gets the color of this Flows.  # noqa: E501

        Color of the icon displayed in the Admin App for the flow.  # noqa: E501

        :return: The color of this Flows.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this Flows.

        Color of the icon displayed in the Admin App for the flow.  # noqa: E501

        :param color: The color of this Flows.  # noqa: E501
        :type: str
        """

        self._color = color

    @property
    def description(self):
        """Gets the description of this Flows.  # noqa: E501


        :return: The description of this Flows.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Flows.


        :param description: The description of this Flows.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def status(self):
        """Gets the status of this Flows.  # noqa: E501

        Current status of the flow.  # noqa: E501

        :return: The status of this Flows.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Flows.

        Current status of the flow.  # noqa: E501

        :param status: The status of this Flows.  # noqa: E501
        :type: str
        """
        allowed_values = ["active", "inactive"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def trigger(self):
        """Gets the trigger of this Flows.  # noqa: E501

        Type of trigger for the flow. One of `hook`, `webhook`, `operation`, `schedule`, `manual`.  # noqa: E501

        :return: The trigger of this Flows.  # noqa: E501
        :rtype: str
        """
        return self._trigger

    @trigger.setter
    def trigger(self, trigger):
        """Sets the trigger of this Flows.

        Type of trigger for the flow. One of `hook`, `webhook`, `operation`, `schedule`, `manual`.  # noqa: E501

        :param trigger: The trigger of this Flows.  # noqa: E501
        :type: str
        """

        self._trigger = trigger

    @property
    def accountability(self):
        """Gets the accountability of this Flows.  # noqa: E501

        The permission used during the flow. One of `$public`, `$trigger`, `$full`, or UUID of a role.  # noqa: E501

        :return: The accountability of this Flows.  # noqa: E501
        :rtype: str
        """
        return self._accountability

    @accountability.setter
    def accountability(self, accountability):
        """Sets the accountability of this Flows.

        The permission used during the flow. One of `$public`, `$trigger`, `$full`, or UUID of a role.  # noqa: E501

        :param accountability: The accountability of this Flows.  # noqa: E501
        :type: str
        """

        self._accountability = accountability

    @property
    def options(self):
        """Gets the options of this Flows.  # noqa: E501

        Options of the selected trigger for the flow.  # noqa: E501

        :return: The options of this Flows.  # noqa: E501
        :rtype: object
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this Flows.

        Options of the selected trigger for the flow.  # noqa: E501

        :param options: The options of this Flows.  # noqa: E501
        :type: object
        """

        self._options = options

    @property
    def operation(self):
        """Gets the operation of this Flows.  # noqa: E501

        UUID of the operation connected to the trigger in the flow.  # noqa: E501

        :return: The operation of this Flows.  # noqa: E501
        :rtype: OneOfFlowsOperation
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """Sets the operation of this Flows.

        UUID of the operation connected to the trigger in the flow.  # noqa: E501

        :param operation: The operation of this Flows.  # noqa: E501
        :type: OneOfFlowsOperation
        """

        self._operation = operation

    @property
    def date_created(self):
        """Gets the date_created of this Flows.  # noqa: E501

        Timestamp in ISO8601 when the flow was created.  # noqa: E501

        :return: The date_created of this Flows.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this Flows.

        Timestamp in ISO8601 when the flow was created.  # noqa: E501

        :param date_created: The date_created of this Flows.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def user_created(self):
        """Gets the user_created of this Flows.  # noqa: E501

        The user who created the flow.  # noqa: E501

        :return: The user_created of this Flows.  # noqa: E501
        :rtype: OneOfFlowsUserCreated
        """
        return self._user_created

    @user_created.setter
    def user_created(self, user_created):
        """Sets the user_created of this Flows.

        The user who created the flow.  # noqa: E501

        :param user_created: The user_created of this Flows.  # noqa: E501
        :type: OneOfFlowsUserCreated
        """

        self._user_created = user_created

    @property
    def operations(self):
        """Gets the operations of this Flows.  # noqa: E501


        :return: The operations of this Flows.  # noqa: E501
        :rtype: list[OneOfFlowsOperationsItems]
        """
        return self._operations

    @operations.setter
    def operations(self, operations):
        """Sets the operations of this Flows.


        :param operations: The operations of this Flows.  # noqa: E501
        :type: list[OneOfFlowsOperationsItems]
        """

        self._operations = operations

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
        if issubclass(Flows, dict):
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
        if not isinstance(other, Flows):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
