from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from agent import DigitalGrowthAgent

app = FastAPI(title="AI Digital Growth Agent")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

agent = DigitalGrowthAgent()

class BusinessInput(BaseModel):
    business_name: str
    business_type: str
    products_services: str
    location: str
    target_customers: str
    price_range: str
    current_presence: Optional[str] = "None"
    goals: str

@app.get("/")
def root():
    return {"message": "AI Digital Growth Agent API"}

@app.post("/generate-strategy")
async def generate_strategy(business: BusinessInput):
    strategy = agent.generate_strategy(business.dict())
    return strategy

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
