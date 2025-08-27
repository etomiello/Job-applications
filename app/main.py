from fastapi import FastAPI
from app.routes import applications  # ⬅️ import your route file

app = FastAPI() #Creates the FastAPI app object

# Include the router
app.include_router(applications.router) #Registers the route so FastAPI knows about /applications
