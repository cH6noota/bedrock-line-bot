# coding: utf-8

"""
    LINE Messaging API

    This document describes LINE Messaging API.  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conint

class ShowLoadingAnimationRequest(BaseModel):
    """
    ShowLoadingAnimationRequest
    https://developers.line.biz/en/reference/messaging-api/#display-a-loading-indicator-request-body
    """
    chat_id: StrictStr = Field(..., alias="chatId", description="User ID of the target user for whom the loading animation is to be displayed.")
    loading_seconds: Optional[conint(strict=True, le=60, ge=5)] = Field(None, alias="loadingSeconds", description="The number of seconds to display the loading indicator. It must be a multiple of 5. The maximum value is 60 seconds. ")

    __properties = ["chatId", "loadingSeconds"]

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
    def from_json(cls, json_str: str) -> ShowLoadingAnimationRequest:
        """Create an instance of ShowLoadingAnimationRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ShowLoadingAnimationRequest:
        """Create an instance of ShowLoadingAnimationRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ShowLoadingAnimationRequest.parse_obj(obj)

        _obj = ShowLoadingAnimationRequest.parse_obj({
            "chat_id": obj.get("chatId"),
            "loading_seconds": obj.get("loadingSeconds")
        })
        return _obj
