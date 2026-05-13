from pydantic import BaseModel, ConfigDict


class OrderBase(BaseModel):
    customer: str
    status: str


class OrderCreate(OrderBase):
    pass


class OrderResponse(OrderBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class InventoryResponse(BaseModel):
    id: int
    product: str
    stock: int

    @property
    def critical(self) -> bool:
        return self.stock < 10

    model_config = ConfigDict(from_attributes=True)


class CargoResponse(BaseModel):
    id: int
    tracking: str
    status: str
    model_config = ConfigDict(from_attributes=True)


class DashboardSummary(BaseModel):
    total_orders: int
    critical_stock_count: int
    delayed_cargo_count: int