import math
from datetime import datetime
from typing import Dict, Any, List

__author__ = "Chirag Kamble"


class CalculatePoints:
    @staticmethod
    def calculate_points(data: Dict[str, Any]) -> Dict[str, int]:
        """
        Calculate points based on the receipt data
        :param data: JSON with receipt data
        :return: Dictionary with points data
        """
        points: int = 0
        retailer_name: str = data["retailer"]
        for char in retailer_name:
            points += 1 if char.isalnum() else 0

        total: str = data["total"]
        cents: str = total.split(".")[1] if "." in total else "0"
        if int(cents) == 0:
            points += 50

        if float(total) % 0.25 == 0:
            points += 25

        items: List[Dict[str, Any]] = data["items"]
        num_of_pair_items: int = len(items) // 2
        points += num_of_pair_items * 5

        for item in items:
            description: str = item["shortDescription"]
            trimmed_desc: str = description.strip()
            if len(trimmed_desc) % 3 == 0:
                new_price: int = math.ceil(float(item["price"]) * 0.2)
                points += new_price

        purchase_date: str = data["purchaseDate"]
        date_obj: datetime = datetime.strptime(purchase_date, "%Y-%m-%d")
        day: int = date_obj.day
        if day % 2 != 0:
            points += 6

        time_format: str = "%H:%M"
        start_time: datetime.time = datetime.strptime("14:00", time_format).time()
        end_time: datetime.time = datetime.strptime("16:00", time_format).time()
        purchase_time: str = data["purchaseTime"]
        time_obj: datetime.time = datetime.strptime(purchase_time, time_format).time()
        if start_time < time_obj < end_time:
            points += 10

        return {"points": points}
