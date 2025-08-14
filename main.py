from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from uuid import UUID, uuid4


app = FastAPI()


JOBS = {}


class JobCreate(BaseModel):
    image_url: str
    callback_url: str
    callback_token: str
    algorithm_name: str


@app.get("/ping", tags=["Monitoring"])
def ping():
    """Check that the API is alive"""
    return {"message": f"pong"}



@app.post("/job-submission")
async def create_job(job_data: JobCreate):
    job_id = uuid4()
    JOBS[job_id] = {"status": "wait"}
    if job_data.algorithm_name not in ["poi_detection", "roi_detection"]:
        raise HTTPException(
            status_code=404,
            detail="You must insert poi_detection or roi_detection"
        )


    data = {
        "image_url": job_data.image_url,
        "callback_url": job_data.callback_url,
        "callback_token": job_data.callback_token,
        "algorithm_name": job_data.algorithm_name,
        "status": "wait"
    }
    
    return {
        "msg": f"we got data successfully {job_id}"
    }

@app.get("/status/{job_id}")
async def get_status(job_id: UUID):
    if job_id not in JOBS:
        raise HTTPException(status_code=404, detail="Job not found")
    return {
        "job_id": job_id, "status": JOBS[job_id]["status"]
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
