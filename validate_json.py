from typing import Dict, List, Any
from datetime import datetime

from custom_exceptions import CustomException

__author__ = "Chirag Kamble"


class JSONValidation:
    @staticmethod
    def validate_json(data: Dict[str, Any]):
        """
        Validate the payload
        :param data: JSON payload
        """
        required_outer_fields: List[str] = ["retailer", "purchaseDate", "purchaseTime", "items", "total"]
        required_inner_fields: List[str] = ["shortDescription", "price"]
        for field in required_outer_fields:
            if field not in data or (not isinstance(data[field], str) and not isinstance(data[field], list)):
                raise CustomException(f"Missing required field or Wrong data type for field: {field}")
        try:
            datetime.strptime(data["purchaseDate"], "%Y-%m-%d")
        except ValueError:
            raise CustomException("Incorrect Date format for field: 'puchaseDate'")

        try:
            datetime.strptime(data["purchaseTime"], "%H:%M").time()
        except ValueError as e:
            raise CustomException("Incorrect Time format for field: 'puchaseTime'")

        try:
            float(data["total"])
        except ValueError:
            raise CustomException("Value Error for field: 'total'")

        for item in data["items"]:
            for field in required_inner_fields:
                if field not in item or not isinstance(item[field], str):
                    raise CustomException(f"Missing required field or Wrong data type for field: {field}")
            try:
                float(item["price"])
            except ValueError:
                raise CustomException("Value Error for field: 'price'")
