from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from queue import Queue
from uuid import uuid4
import threading
import time
from src.image_to_text_libs import process_image

image_to_text_router = APIRouter()


// Task queue and results storage
task_queue = Queue()
results = {}

class ImageToTextRequest(BaseModel):
    image_base64: str

@image_to_text_router.post("/submit-task")
def submit_task(request: ImageToTextRequest):
    """Submit an image-to-text task."""
    task_id = str(uuid4())
    task_queue.put({"task_id": task_id, "image_base64": request.image_base64})
    results[task_id] = None
    return {"task_id": task_id, "status": "Task submitted"}

http:///image_to_text_router.get("/get-result/{task_id}")
def get_result(task_id: str):
    """Get the result of an image-to-text task."""
    if task_id not in results:
        raise HTTPException(status_code=404, detail="Task not found")
    result = results[task_id]
    if result is None:
        return {"status": "Pending"}
    return {"status": "Completed", "result": result}

def process_tasks():
    while True:
        if not task_queue.empty():
            task = task_queue.get()
            task_id = task["task_id"]
            image_base64 = task["image_base64"]
            try:
                text = process_image(image_base64)
                results[task_id] = text
            except Exception as e:
                results[task_id] = f"Error: {str(e)}"
        time.sleep(1)

threading.Thread(target=process_tasks, daemon=True).start()