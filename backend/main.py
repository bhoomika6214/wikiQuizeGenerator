from fastapi.middleware.cors import CORSMiddleware
from models import Base
from fastapi import FastAPI
from database import engine

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine)
    try:
        connection = engine.connect()
        connection.close()
        print("✅ Database connected successfully")
    except Exception as e:
        print("❌ Database connection failed:", e)

@app.get("/")
def read_root():
    return {"message": "Wiki Quiz Backend + DB connected"}
