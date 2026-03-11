from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv()
from .routes import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",    # React default
    "http://localhost:5173",    # Vite default
    "https://your-production-site.com",
]

# 2. Add the middleware to the app
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            # List of allowed domains
    allow_credentials=True,           # Allow cookies/auth headers
    allow_methods=["*"],              # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],              # Allow all headers
)

app.include_router(router)

@app.get("/")
def read_root():
    return {"Hello": "World"}