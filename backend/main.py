from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "PyTorch backend is running!"}

@app.get("/test")
def test():
    return {"message": "Hello from Python!"}