# KOBI Command Center - Core API

Bu proje, KOBİ'ler için geliştirilen yapay zeka destekli operasyon merkezinin (KOBI Command Center) Core Backend servisidir. Sipariş, stok ve kargo yönetimini tek bir merkezde toplar ve AI ajanının (Gemini) kararlar alabilmesi için gerekli veri altyapısını sağlar.

## Teknolojiler
* Framework: FastAPI
* Veritabanı: SQLite & SQLAlchemy
* Veri Doğrulama: Pydantic
* Dil: Python 3.x

## Kurulum ve Çalıştırma (Takım Arkadaşım İçin Notlar)

Projeyi bilgisayarına çektikten sonra şu adımları izleyerek ayağa kaldırabilirsin:

1. Sanal ortamı oluştur ve aktif et:
python -m venv venv
Windows için: venv\Scripts\activate
Mac/Linux için: source venv/bin/activate

2. Gerekli kütüphaneleri (bağımlılıkları) kur:
pip install -r requirements.txt

3. Sistemi başlat:
uvicorn main:app --reload

(Not: Sistemi ilk çalıştırdığında kobi_command.db dosyası otomatik oluşacak ve içine test verileri (mock data) basılacaktır.)

## API Portları (AI Agent İçin Tool Entegrasyon Noktaları)
Sistem çalıştığında http://127.0.0.1:8000/docs adresinden tüm endpointleri Swagger üzerinden test edebilirsin.

Gemini Tool Calling için kullanabileceğin ana portlar:
* GET /api/v1/orders - Tüm siparişleri getirir.
* GET /api/v1/orders/{id} - Tekil sipariş detayını getirir.
* GET /api/v1/inventory/critical - Stok seviyesi 10'un altında olan kritik ürünleri listeler.
* GET /api/v1/cargo/{tracking_id} - Kargo durumunu sorgular.
* GET /api/v1/dashboard/summary - Sistemin genel özetini (toplam sipariş, kritik stok sayısı vb.) döner.
