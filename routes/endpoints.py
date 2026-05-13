from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.config import get_db
import models.domain as domain
import schemas.dtos as dtos

router = APIRouter()


@router.get("/orders", response_model=list[dtos.OrderResponse])
def get_orders(db: Session = Depends(get_db)):
    return db.query(domain.Order).all()


@router.get("/orders/{order_id}", response_model=dtos.OrderResponse)
def get_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(domain.Order).filter(domain.Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Sipariş bulunamadı")
    return order


@router.post("/orders", response_model=dtos.OrderResponse)
def create_order(order: dtos.OrderCreate, db: Session = Depends(get_db)):
    db_order = domain.Order(customer=order.customer, status=order.status)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


@router.get("/inventory", response_model=list[dtos.InventoryResponse])
def get_inventory(db: Session = Depends(get_db)):
    return db.query(domain.Inventory).all()


@router.get("/inventory/critical")
def get_critical_inventory(db: Session = Depends(get_db)):
    critical_items = db.query(domain.Inventory).filter(domain.Inventory.stock < 10).all()
    return [{"product": item.product, "stock": item.stock} for item in critical_items]


@router.get("/cargo/{tracking_id}", response_model=dtos.CargoResponse)
def get_cargo(tracking_id: str, db: Session = Depends(get_db)):
    cargo = db.query(domain.Cargo).filter(domain.Cargo.tracking == tracking_id).first()
    if not cargo:
        raise HTTPException(status_code=404, detail="Kargo bulunamadı")
    return cargo


@router.get("/dashboard/summary", response_model=dtos.DashboardSummary)
def get_dashboard_summary(db: Session = Depends(get_db)):
    total_orders = db.query(domain.Order).count()
    critical_stock_count = db.query(domain.Inventory).filter(domain.Inventory.stock < 10).count()
    delayed_cargo_count = db.query(domain.Cargo).filter(domain.Cargo.status == "Gecikmede").count()

    return dtos.DashboardSummary(
        total_orders=total_orders,
        critical_stock_count=critical_stock_count,
        delayed_cargo_count=delayed_cargo_count
    )