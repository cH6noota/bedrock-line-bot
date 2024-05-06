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


from typing import Optional, Union
from pydantic.v1 import Field, StrictFloat, StrictInt, StrictStr
from linebot.v3.webhooks.models.message_content import MessageContent

class LocationMessageContent(MessageContent):
    """
    LocationMessageContent
    """
    title: Optional[StrictStr] = Field(None, description="Title")
    address: Optional[StrictStr] = Field(None, description="Address")
    latitude: Union[StrictFloat, StrictInt] = Field(..., description="Latitude")
    longitude: Union[StrictFloat, StrictInt] = Field(..., description="Longitude")
    type: str = "location"

    __properties = ["type", "id", "title", "address", "latitude", "longitude"]

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
    def from_json(cls, json_str: str) -> LocationMessageContent:
        """Create an instance of LocationMessageContent from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LocationMessageContent:
        """Create an instance of LocationMessageContent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LocationMessageContent.parse_obj(obj)

        _obj = LocationMessageContent.parse_obj({
            "type": obj.get("type"),
            "id": obj.get("id"),
            "title": obj.get("title"),
            "address": obj.get("address"),
            "latitude": obj.get("latitude"),
            "longitude": obj.get("longitude")
        })
        return _obj
