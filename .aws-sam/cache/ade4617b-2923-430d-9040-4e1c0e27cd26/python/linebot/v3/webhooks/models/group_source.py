# coding: utf-8

"""
    Webhook Type Definition

    Webhook event definition of the LINE Messaging API  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic.v1 import Field, StrictStr
from linebot.v3.webhooks.models.source import Source

class GroupSource(Source):
    """
    GroupSource
    """
    group_id: StrictStr = Field(..., alias="groupId", description="Group ID of the source group chat")
    user_id: Optional[StrictStr] = Field(None, alias="userId", description="ID of the source user. Only included in message events. Only users of LINE for iOS and LINE for Android are included in userId.")
    type: str = "group"

    __properties = ["type", "groupId", "userId"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> GroupSource:
        """Create an instance of GroupSource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GroupSource:
        """Create an instance of GroupSource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GroupSource.parse_obj(obj)

        _obj = GroupSource.parse_obj({
            "type": obj.get("type"),
            "group_id": obj.get("groupId"),
            "user_id": obj.get("userId")
        })
        return _obj
