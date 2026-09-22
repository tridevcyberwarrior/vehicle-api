from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests
import os
from pydantic import BaseModel

app = FastAPI(title="Vehicle Info API", version="1.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class VehicleRequest(BaseModel):
    registration_number: str

@app.get("/")
async def root():
    return {"message": "Vehicle Info API is running", "docs": "/docs"}

@app.get("/search/{registration_number}")
async def search_vehicle(registration_number: str):
    """
    Search vehicle by registration number
    """
    url = "https://api-ct.vehicleinfo.app/gw/plt/bffctsvc/api/v1/garage/rc-search"
    
    params = {
        'registration_number': registration_number.upper()
    }
    
    headers = {
        'User-Agent': os.getenv("USER_AGENT", "okhttp/4.12.0"),
        'Accept': "application/json, text/plain, */*",
        'Accept-Encoding': "gzip",
        'authorization': f"Bearer {os.getenv('AUTH_TOKEN')}",
        'x-user-city-id': os.getenv("CITY_ID", "777"),
        'super_app_source': "vehicleinfo_consumerapp",
        'x-api-key': os.getenv("API_KEY"),
        'x_app_instance_id': os.getenv("DEVICE_ID", "547247478ea8e416185d98fbeb629954"),
        'x-device-id': os.getenv("DEVICE_ID", "547247478ea8e416185d98fbeb629954"),
        'x-tenant-id': "VI_INDIA",
        'userid': os.getenv("USER_ID", "6f4ad9f9-8db3-44ee-aa45-f2e3d5a616d1"),
        'x_experiment_id': "252935e1-2b91-4b74-9734-9a40037cd09f",
        'clientid': "vehicleinfo_consumerapp",
        'appversion': "323",
        'osname': "android",
        'useragent': "vehicleinfo_consumerapp/323",
        'source': "MobileApp",
        'x_country': "IN",
        'x-tenant-slug': "vehicleinfo"
    }
    
    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"External API error: {str(e)}")

@app.post("/search")
async def search_vehicle_post(request: VehicleRequest):
    """
    Search vehicle by registration number (POST method)
    """
    url = "https://api-ct.vehicleinfo.app/gw/plt/bffctsvc/api/v1/garage/rc-search"
    
    params = {
        'registration_number': request.registration_number.upper()
    }
    
    headers = {
        'User-Agent': os.getenv("USER_AGENT", "okhttp/4.12.0"),
        'Accept': "application/json, text/plain, */*",
        'Accept-Encoding': "gzip",
        'authorization': f"Bearer {os.getenv('AUTH_TOKEN')}",
        'x-user-city-id': os.getenv("CITY_ID", "777"),
        'super_app_source': "vehicleinfo_consumerapp",
        'x-api-key': os.getenv("API_KEY"),
        'x_app_instance_id': os.getenv("DEVICE_ID", "547247478ea8e416185d98fbeb629954"),
        'x-device-id': os.getenv("DEVICE_ID", "547247478ea8e416185d98fbeb629954"),
        'x-tenant-id': "VI_INDIA",
        'userid': os.getenv("USER_ID", "6f4ad9f9-8db3-44ee-aa45-f2e3d5a616d1"),
        'x_experiment_id': "252935e1-2b91-4b74-9734-9a40037cd09f",
        'clientid': "vehicleinfo_consumerapp",
        'appversion': "323",
        'osname': "android",
        'useragent': "vehicleinfo_consumerapp/323",
        'source': "MobileApp",
        'x_country': "IN",
        'x-tenant-slug': "vehicleinfo"
    }
    
    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"External API error: {str(e)}")
