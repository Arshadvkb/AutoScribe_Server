from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv()
from src.app.routes import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",   
    "http://localhost:5173",    
    "https://your-production-site.com",
]



app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,           
    allow_credentials=True,          
    allow_methods=["*"],            
    allow_headers=["*"],
    expose_headers=["Content-Disposition"],
)

app.include_router(router)

@app.get("/")
def read_root():
    return {"Hello": "World"}