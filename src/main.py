from fastapi import FastAPI
from src.admin_panel import admin_router
from src.image_to_text import image_to_text_router
from src.config import HOST, PORT

app = FastAPI()

# Mount routers
app.include_router(admin_router, prefix="/admin")
app.include_router(image_to_text_router, prefix="/tasks")

@app.get("/")
async def root():
    return {"message": "Welcome to Captcha^Tract Standalone"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=HOST, port=PORT)