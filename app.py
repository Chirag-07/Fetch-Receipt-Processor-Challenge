from typing import Dict, Any
from flask import Flask, request, jsonify
import uuid

from calculate_points import CalculatePoints
from validate_json import JSONValidation
from custom_exceptions import CustomException

__author__ = "Chirag Kamble"


app = Flask(__name__)

db: Dict[str, Dict[str, int]] = {}


@app.route("/receipts/process", methods=["POST"])
def process_receipt():
    """
    Generate id for receipt, calculate points and store it
    :return: JSON with receipt id
    """
    receipt_data: Dict[str, Any] = request.get_json()
    if not receipt_data:
        return jsonify({"error": "Invalid or empty JSON"}), 400

    try:
        JSONValidation.validate_json(receipt_data)
    except CustomException as ce:
        return jsonify({"error": str(ce)}), 400

    receipt_id: str = str(uuid.uuid4())

    points_data: Dict[str, int] = CalculatePoints.calculate_points(receipt_data)

    db[receipt_id] = points_data

    return jsonify({"id": receipt_id}), 201


@app.route("/receipts/<string:receipt_id>/points", methods=["GET"])
def get_points(receipt_id: str) -> Dict[str, int]:
    """
    Get points for a given receipt id
    :param receipt_id: Receipt id string used to get corresponding points
    :return: JSON with points of the receipt
    """
    points_data: Dict[str, int] = db[receipt_id]
    return jsonify(points_data)


if __name__ == "__main__":
    app.run(debug=True)
