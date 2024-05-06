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



from pydantic.v1 import Field, StrictStr, validator
from linebot.v3.webhooks.models.module_content import ModuleContent

class DetachedModuleContent(ModuleContent):
    """
    DetachedModuleContent
    """
    bot_id: StrictStr = Field(..., alias="botId", description="Detached LINE Official Account bot user ID")
    reason: StrictStr = Field(..., description="Reason for detaching")
    type: str = "detached"

    __properties = ["type", "botId", "reason"]

    @validator('reason')
    def reason_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('bot_deleted'):
            raise ValueError("must be one of enum values ('bot_deleted')")
        return value

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
    def from_json(cls, json_str: str) -> DetachedModuleContent:
        """Create an instance of DetachedModuleContent from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DetachedModuleContent:
        """Create an instance of DetachedModuleContent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DetachedModuleContent.parse_obj(obj)

        _obj = DetachedModuleContent.parse_obj({
            "type": obj.get("type"),
            "bot_id": obj.get("botId"),
            "reason": obj.get("reason")
        })
        return _obj

