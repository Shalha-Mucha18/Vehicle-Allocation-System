from motor.motor_asyncio import AsyncIOMotorClient


client = AsyncIOMotorClient('mongodb://localhost:27017') # Establish a connection to MongoDB using Motor


db = client['vehicle_allocation_db'] ## Select the database for the vehicle allocation system


employees_collection = db['employees'] ## collections for employees, vehicles, and allocations
vehicles_collection = db['vehicles']
allocations_collection = db['allocations']

