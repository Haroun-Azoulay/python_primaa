from fastapi import APIRouter, HTTPException
from uuid import UUID, uuid4
import schemas


router = APIRouter()


# Redis memory
JOBS = {}


@router.post("/job-submission", tags=["Job"])
async def create_job(job_data: schemas.JobCreate):
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
    
    return {"msg": f"we got data successfully {job_id}"}

@router.get("/status/{job_id}", tags=["Job"])
async def get_status(job_id: UUID):
    if job_id not in JOBS:
        raise HTTPException(status_code=404, detail="Job not found")
    return {"job_id": job_id, "status": JOBS[job_id]["status"]}
