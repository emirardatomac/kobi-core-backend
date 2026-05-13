from fastapi import FastAPI
from database.config import engine, Base, SessionLocal
from routes.endpoints import router
from models.domain import Order, Inventory, Cargo

Base.metadata.create_all(bind=engine)

app = FastAPI(title="KOBI Command Center API")

def seed_data():
    db = SessionLocal()
    if db.query(Order).count() == 0:
        db.add_all([
            Order(customer="Ahmet Yılmaz", status="Hazırlanıyor"),
            Order(customer="Ayşe Demir", status="Kargoya Verildi"),
            Order(customer="Mehmet Kaya", status="Teslim Edildi")
        ])
        db.add_all([
            Inventory(product="Filtre Kahve", stock=8),
            Inventory(product="Espresso", stock=50),
            Inventory(product="Chemex Kağıdı", stock=3)
        ])
        db.add_all([
            Cargo(tracking="TR123", status="Dağıtıma Çıktı"),
            Cargo(tracking="TR456", status="Gecikmede"),
            Cargo(tracking="TR789", status="Transfer Merkezinde")
        ])
        db.commit()
    db.close()

seed_data()

app.include_router(router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Sistem Aktif. /docs adresine giderek test edebilirsin."}