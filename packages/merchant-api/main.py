# from fastapi import FastAPI, HTTPException
# from pymongo import MongoClient
# from pydantic import BaseModel
# from typing import List

# app = FastAPI()

# # Pydantic model to represent a merchant
# class Merchant(BaseModel):
#     name: str
#     address: str
#     contact: str

# class Location(BaseModel):
#     address: str
#     city: str
#     postal_code: str

# class Transaction(BaseModel):
#     amount: float
#     timestamp: str
#     description: str

# # In-memory storage for merchants (just for demonstration)
# merchants_db = []
# locations_db = {}
# transactions_db = {}

# client = MongoClient("mongodb://mongodb:27017/")
# db = client.mydatabase

# @app.get("/")
# async def read_root():
#     return {"Hello": "World"}

# @app.get("/merchants", response_model=List[Merchant])
# async def get_merchants():
#     return merchants_db

# @app.post("/merchants", response_model=Merchant)
# async def create_merchant(merchant: Merchant):
#     merchants_db.append(merchant)
#     return merchant

# @app.get("/merchants/{merchantId}", response_model=Merchant)
# async def get_merchant(merchantId: int):
#     if merchantId < 0 or merchantId >= len(merchants_db):
#         raise HTTPException(status_code=404, detail="Merchant not found")
#     return merchants_db[merchantId]

# @app.put("/merchants/{merchantId}", response_model=Merchant)
# async def update_merchant(merchantId: int, merchant: Merchant):
#     if merchantId < 0 or merchantId >= len(merchants_db):
#         raise HTTPException(status_code=404, detail="Merchant not found")
#     merchants_db[merchantId] = merchant
#     return merchant

# @app.delete("/merchants/{merchantId}", response_model=Merchant)
# async def delete_merchant(merchantId: int):
#     if merchantId < 0 or merchantId >= len(merchants_db):
#         raise HTTPException(status_code=404, detail="Merchant not found")
#     return merchants_db.pop(merchantId)

# @app.get("/merchants/{merchantId}/locations", response_model=List[Location])
# async def get_locations(merchantId: int):
#     return locations_db.get(merchantId, [])

# @app.post("/merchants/{merchantId}/locations", response_model=Location)
# async def add_location(merchantId: int, location: Location):
#     locations_db.setdefault(merchantId, []).append(location)
#     return location

# @app.get("/merchants/{merchantId}/locations/{locationId}", response_model=Location)
# async def get_single_location(merchantId: int, locationId: int):
#     locations = locations_db.get(merchantId, [])
#     if locationId < 0 or locationId >= len(locations):
#         raise HTTPException(status_code=404, detail="Location not found")
#     return locations[locationId]

# @app.get("/merchants/{merchantId}/transactions", response_model=List[Transaction])
# async def get_transactions(merchantId: int):
#     return transactions_db.get(merchantId, [])

# @app.post("/merchants/{merchantId}/transactions", response_model=Transaction)
# async def add_transaction(merchantId: int, transaction: Transaction):
#     transactions_db.setdefault(merchantId, []).append(transaction)
#     return transaction

# @app.get("/merchants/{merchantId}/transactions/{transactionId}", response_model=Transaction)
# async def get_single_transaction(merchantId: int, transactionId: int):
#     transactions = transactions_db.get(merchantId, [])
#     if transactionId < 0 or transactionId >= len(transactions):
#         raise HTTPException(status_code=404, detail="Transaction not found")
#     return transactions[transactionId]


import uvicorn

from core.config import config

if __name__ == "__main__":
    uvicorn.run(
        app="core.server:app",
        reload=True if config.ENVIRONMENT != "production" else False,
        workers=1,
        host="0.0.0.0",
        port=81,
    )
