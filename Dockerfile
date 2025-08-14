FROM debian:trixie

RUN apt update && apt upgrade -y && apt install -y --no-install-recommends \
    python3 \
    python3-pip \
    python3-pydantic \
    python3-pytest \
    python3-setuptools \
    uvicorn \
    python3-httpx \
    uvicorn \
    python3-requests 
RUN apt clean

RUN pip install --break-system-packages fastapi==0.115.6


WORKDIR /app



COPY . .

EXPOSE 8000
CMD ["python3", "-m", "uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]

