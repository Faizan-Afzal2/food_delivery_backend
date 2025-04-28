# Food Delivery System

A simple object-oriented Flask backend for a food delivery system.

---

## Project Structure

- `app/`
  - `__init__.py` - Initializes Flask app
  - `models.py` - Core OOP models (Customer, Order, etc.)
  - `routes/order_routes.py` - API endpoints
  - `services/core_services.py` - Business logic (cart, order, payment)
- `run.py` - Run the Flask app
- `requirements.txt` - Project dependencies
- `README.md` - Project documentation

---
## Features
- Add items to the cart
- Place orders
- Simulate payments
- Clean OOP structure
- Service layer for business logic
- Organized routing with Blueprints

## OOP Concepts Used
- Encapsulation - Each model handles its data and logic
- Inheritance - Payment processors inherit common behavior
- Abstraction - Payment processing interface hides complexity
- Polymorphism - Different payment types handled interchangeably



## How to Run

1. Clone the project
2. Create a virtual environment
3. Install dependencies
4. Run the server

```bash
git clone <repo_url>
cd food_delivery
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python run.py```


---
