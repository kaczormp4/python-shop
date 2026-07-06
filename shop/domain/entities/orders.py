from pydantic import BaseModel
from enum import Enum

class OrderStatus(Enum):
    ORDERED = "ordered"
    PAID = "paid"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"
        
class Order(BaseModel):
    id: str
    creation_date: str
    delivery_date: str
    items: list
    price: float
    status: OrderStatus
    
      
