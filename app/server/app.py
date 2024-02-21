from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from .libraries.maxmind import MaxMind

app = FastAPI()

@app.get("/")
async def root(request: Request):
    try:
        ip = request.client.host
        maxmind = MaxMind()
        response = maxmind.get_location(ip)
        return JSONResponse(content=response, status_code=200)
    except Exception as e:
        return JSONResponse(
            content={
                "status": "error",
                "message": str(e),
            },
            status_code=500,
        )


@app.get("/{ip}")
async def get_ip(ip: str):
    try:
        validate_ip(ip)
        maxmind = MaxMind()
        response = maxmind.get_location(ip)

        return JSONResponse(content=response, status_code=200)
    except Exception as e:
        return JSONResponse(
            content={
                "status": "error",
                "message": str(e),
            },
            status_code=500,
        )


def validate_ip(ip):
    if not ip:
        raise ValueError("IP address is required")
    parts = ip.split(".")
    if len(parts) != 4:
        raise ValueError("Invalid IP address")
    for part in parts:
        if not part.isdigit():
            raise ValueError("Invalid IP address")
        num = int(part)
        if num < 0 or num > 255:
            raise ValueError("Invalid IP address")
