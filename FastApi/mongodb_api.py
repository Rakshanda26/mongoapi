from fastapi import FastAPI
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
import os
from dotenv import load_dotenv

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")
client = AsyncIOMotorClient(MONGO_URI)
db = client["radhikadb"]
radhika_data = db["radhika_coll"]

app = FastAPI()

class radhikadata(BaseModel):
    name : str
    city : str
    phone : int

@app.post("/radhika/insert")
async def radhika_data_insert_helper(data:radhikadata):
    result = await radhika_data.insert_one(data.dict())
    #return {"message" : "data inserted successfully"}
    return str(result.inserted_id)

def radhika_helper(doc):
    doc["id"] = str(doc["_id"])
    del doc["_id"]
    return doc

@app.get("/radhika/getdata")
async def get_radhika_data():
    items = []
    cursor = radhika_data.find({})
    async for document in cursor:
        items.append(radhika_helper(document))
    return items

