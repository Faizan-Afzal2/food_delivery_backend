# app/routes/order_routes.py
from flask import Blueprint, request, jsonify
from app.models.models import Customer, MenuItem
from app.services.core_services import OrderService

bp = Blueprint("orders", __name__)

# Simulated DB

mock_customers = {}
mock_items = {
    "burger": MenuItem("Burger", 500),
    "fries": MenuItem("Fries", 200),
}

@bp.route("/order", methods=["POST"])
def place_order():
    data = request.json
    name = data.get("name")
    items = data.get("items", [])

    if not name or not items:
        return jsonify({"error": "Missing name or items"}), 400

    customer = Customer(name)
    mock_customers[customer.id] = customer

    for item_name in items:
        item = mock_items.get(item_name.lower())
        if item:
            customer.add_to_cart(item)

    try:
        order = OrderService.place_order(customer)
        return jsonify({
            "order_id": order.id,
            "total": order.total,
            "status": order.status.value
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@bp.route("/order/menu", methods=["GET"])
def get_menu():
    menu = {name: {"name": item.name, "price": item.price} for name, item in mock_items.items()}
    return jsonify(menu)
