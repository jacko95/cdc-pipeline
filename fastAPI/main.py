from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional, Any, Dict
import uvicorn
import json
import datetime

app = FastAPI(title="Debezium Event Receiver")

PORT = 3000
# HOST = "127.0.0.1"
HOST = "0.0.0.0"

# Modelli (opzionali, per validazione leggera)
class DebeziumPayload(BaseModel):
    op: Optional[str] = None
    before: Optional[Any] = None
    after: Optional[Any] = None
    source: Optional[Dict] = None
    ts_ms: Optional[int] = None

class DebeziumEvent(BaseModel):
    payload: Optional[DebeziumPayload] = None

@app.middleware("http")
async def log_requests(request: Request, call_next):
    if request.method == "POST" and request.url.path == "/events":
        print("\n" + "═" * 80)
        print("📨 RICEVUTA RICHIESTA HTTP POST su /events")
        print("🕐 Timestamp:", datetime.datetime.utcnow().isoformat() + "Z")
        print("═" * 80)
    response = await call_next(request)
    return response

@app.post("/events")
async def receive_events(request: Request):
    try:
        body_bytes = await request.body()
        if not body_bytes:
            raise HTTPException(status_code=400, detail="Empty body")
        body_str = body_bytes.decode("utf-8")
        payload = json.loads(body_str)
    except json.JSONDecodeError as e:
        print("❌ ERRORE PARSING JSON:", e.msg)
        print("Body ricevuto (primi 500 caratteri):")
        print(body_str[:500])
        print("═" * 80 + "\n")
        raise HTTPException(status_code=400, detail="Invalid JSON")
    
    inner_payload = payload.get("payload", {})
    op = inner_payload.get("op", "N/A")
    after = inner_payload.get("after", "N/A")
    before = inner_payload.get("before", "N/A")
    ts_ms = inner_payload.get("ts_ms", "N/A")
    source = inner_payload.get("source", {})
    
    print("✅ JSON parsato correttamente")
    print(body_str)
    # print("🔄 Tipo operazione:", op)
    print("📊 Dati (after):", json.dumps(after, indent=2, ensure_ascii=False))
    # if op == "d":
    #     print("🗑️  Dati (before):", json.dumps(before, indent=2, ensure_ascii=False))
    # print("🕖 Timestamp evento:", ts_ms)
    # db_name = source.get("db") or source.get("schema") or "N/A"
    # print("🏭 Sorgente:", db_name)
    # print("═" * 80 + "\n")
    
    return JSONResponse({
        "status": "ok",
        "received": True,
        "processed_at": datetime.datetime.utcnow().isoformat() + "Z",
        "operation": op
    })

@app.exception_handler(404)
async def not_found_handler(request: Request, exc):
    return JSONResponse(status_code=404, content={
        "error": "Not Found",
        "message": f"Endpoint {request.method} {request.url.path} non esistente"
    })

if __name__ == "__main__":
    print("\n🚀 Server FastAPI avviato con successo!")
    print(f"📍 In ascolto su: http://localhost:{PORT}")
    print(f"📌 Endpoint principale: POST http://localhost:{PORT}/events")
    print("⏳ In attesa di eventi dai container Docker (es. Debezium)...\n")
    
    uvicorn.run("main:app", host=HOST, port=PORT, reload=True, log_level="info")