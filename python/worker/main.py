import asyncio
import os
import uvicorn
from fastapi import FastAPI, WebSocket
from typing import List, Dict, Any
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("worker")

app = FastAPI()

class ModelWorker:
    def __init__(self, worker_id: str):
        self.worker_id = worker_id
        self.models = {}
        self.queue = asyncio.Queue()
        logger.info(f"Worker {worker_id} initialized")
    
    async def load_model(self, model_name: str):
        logger.info(f"Loading model: {model_name}")
        # Simulate loading
        self.models[model_name] = "LOADED"
        return True
    
    async def process_request(self, request: Dict[str, Any]) -> Dict[str, Any]:
        logger.info(f"Processing request: {request}")
        # Simulate inference
        await asyncio.sleep(0.1)
        return {"result": [0.1, 0.9], "model": request.get("model")}

worker = ModelWorker(worker_id=os.getenv("WORKER_ID", "worker-1"))

@app.on_event("startup")
async def startup_event():
    await worker.load_model("default-model")

@app.get("/health")
async def health():
    return {"status": "ok", "models": list(worker.models.keys())}

@app.post("/predict")
async def predict(request: Dict[str, Any]):
    result = await worker.process_request(request)
    return result

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
