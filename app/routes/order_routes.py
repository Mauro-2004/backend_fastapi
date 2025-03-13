from fastapi import APIRouter, Depends
from app.models.order_model import Order
from app.controllers.order_controller import OrderController

router = APIRouter()
order_controller = OrderController()

@router.post("/order", response_model=dict)
def create_order(order: Order):
    return order_controller.create_order(order)

@router.get("/order/{order_id}", response_model=dict)
def get_order(order_id: int):
    return order_controller.get_order(order_id)

@router.get("/order", response_model=dict)
def get_order():
    return order_controller.get_order()

@router.put("/order/{order_id}", response_model=dict)
def update_order(order_id: int, order: Order):
    return order_controller.update_order(order_id, order)

@router.delete("/order/{order_id}", response_model=dict)
def delete_order(order_id: int):
    return order_controller.delete_order(order_id)
