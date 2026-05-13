🧠 KOBI AI Service

KOBI AI Service, küçük ve orta ölçekli işletmeler için geliştirilmiş gerçek zamanlı operasyon yönetim ve AI karar destek sistemidir.

Sistem; sipariş, stok, kargo ve müşteri verilerini tek bir backend üzerinde yönetirken, üst katmanda Gemini destekli bir AI agent ile doğal dil üzerinden operasyon kontrolü sağlar.

🏗️ Sistem Mimarisi
Frontend
   ↓
AI Backend (Gemini Agent + Tool Orchestration)
   ↓
Core Backend (FastAPI Business API)
   ↓
SQLite / PostgreSQL (Production-ready yapı)

🧱 Core Backend (System of Record)

Core Backend, tüm iş verisinin ve operasyonel mantığın merkezi katmanıdır.

🛠️ Teknolojiler
FastAPI
SQLAlchemy
Pydantic
SQLite (dev) / PostgreSQL (prod uyumlu yapı)

📁 Proje Yapısı
app/
 ├── main.py
 ├── routes/
 ├── models/
 ├── schemas/
 ├── services/
 ├── database/
 └── utils/
 
🗄️ Veri Modelleri
📦 Orders
id
customer
status
📦 Inventory
id
product
stock
🚚 Cargo
id
tracking_id
status
👤 Customers
müşteri bilgileri ve ilişkisel veriler
⚙️ Business Logic

Sistem tamamen gerçek veriler üzerinden çalışır.

Örnek kritik iş kuralı:

if stock < 10:
    mark_as_critical(product_id)
🔌 API Endpoints
📦 Orders
GET /orders
GET /orders/{id}
POST /orders
📦 Inventory
GET /inventory
GET /inventory/critical
🚚 Cargo
GET /cargo/{tracking_id}
📊 Analytics
GET /dashboard/summary
📚 Dokümantasyon
Swagger UI: /docs
OpenAPI: otomatik FastAPI schema
🎯 Core Backend Çıktısı
✅ Production-ready API
✅ Database schema + migrations
✅ Seed data (ilk kurulum verisi)
✅ Business rule engine
✅ Swagger documentation
🤖 AI Backend (Intelligence Layer)

AI Backend, sistemin doğal dil ile kontrol edilmesini sağlayan agent katmanıdır.

🛠️ Teknolojiler
Python
Google Gemini
FastAPI
Tool Calling Architecture
💬 AI Endpoint
POST /chat

Kullanıcıdan gelen tüm doğal dil istekleri bu endpoint üzerinden işlenir.

🧠 System Prompt (Çekirdek Davranış)

AI agent şu rol ile çalışır:

Sen KOBİ operasyon yöneticisisin.
Sipariş, stok ve kargo verilerine erişerek karar verirsin.
Gerekirse tool çağrısı yaparak backend sistemden veri çekersin.
🔍 Intent Detection

Kullanıcı mesajı analiz edilerek niyet çıkarılır:

Örnek

Input:

128 numaralı sipariş nerede?

Output:

{
  "intent": "track_order",
  "order_id": "128"
}
🔧 Tool Architecture

Gemini, ihtiyaç duyduğunda aşağıdaki tool’ları seçer:

get_order_status(order_id)
get_inventory_status(product_id)
get_cargo_status(tracking_id)
get_dashboard_summary()
⚙️ Tool Execution Flow
User Message
   ↓
Gemini (decision layer)
   ↓
Tool selection
   ↓
Core Backend API call
   ↓
Raw data response
   ↓
Gemini final response generation
📊 AI Output Examples
“Siparişiniz kargoya verilmiş durumda.”
“3 ürün stok kritik seviyede.”
“Bugün operasyonel olarak 2 risk tespit edildi.”
📈 Intelligence Features
Operasyonel özet üretme
Stok tükenme riski analizi
Sipariş durum takibi
Kargo gecikme tahmini
Otomatik aksiyon önerileri
🎯 AI Backend Çıktısı
✅ Fully working /chat endpoint
✅ Gemini integration
✅ Tool calling system
✅ Context-aware response engine
🔗 Backend Entegrasyon Noktaları

AI layer şu Core API’leri kullanır:

GET /orders/{id}
GET /inventory/critical
GET /cargo/{id}
GET /dashboard/summary
🚀 Çalışma Akışı
1. Kullanıcı Mesajı
Siparişim nerede?
2. AI Decision
Intent: tracking
Tool: get_order_status
3. Backend Call
GET /orders/128
4. Response Processing

AI veriyi yorumlar ve insan diline çevirir.

5. Final Output
Siparişiniz hazırlanıyor ve kargoya verilmek üzere.
🧪 Demo Senaryosu

Sistem şu akışı başarıyla çalıştırır:

User → AI → Backend → AI → User
💡 Engineering Notes
Core backend tamamen bağımsız çalışır
AI backend stateless tasarlanmıştır
Tool layer genişletilebilir mimaridedir
Yeni endpoint eklemek AI sistemini otomatik güçlendirir
