from fastapi import FastAPI
from uuid import UUID, uuid4
import routes

app = FastAPI()

app.include_router(routes.router)



@app.get("/ping", tags=["Monitoring"])
def ping():
    """Check that the API is alive"""
    return {"message": f"pong"}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
