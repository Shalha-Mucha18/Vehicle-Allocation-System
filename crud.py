from datetime import date
from app.database import allocations_collection
from bson import ObjectId

async def create_allocation(employee_id: str, vehicle_id: str, allocation_date: date):
allocation = await allocations_collection.find_one({"vehicle_id": vehicle_id, "allocation_date": allocation_date})
    if allocation:
        return None  # Return None if the vehicle is already allocated

    # Prepare the new allocation document
    new_allocation = {
        "employee_id": employee_id,
        "vehicle_id": vehicle_id,
        "allocation_date": allocation_date,
        "status": "allocated"
    }


    result = await allocations_collection.insert_one(new_allocation ## Insert the new allocation into the MongoDB collection
    return new_allocation  # Return the created allocation


# Function to update an existing allocatio
async def update_allocation(allocation_id: str, new_date: date):
    allocation = await allocations_collection.find_one({"_id": ObjectId(allocation_id)})
    if allocation and new_date >= date.today():
        await allocations_collection.update_one(
            {"_id": ObjectId(allocation_id)},
            {"$set": {"allocation_date": new_date}}
        )
        return True  # Return success if update is valid
    return False


# Function to delete an allocation before the allocation date
async def delete_allocation(allocation_id: str):
    allocation = await allocations_collection.find_one({"_id": ObjectId(allocation_id)})
    # Only allow deletion if the allocation date is in the future or today
    if allocation and allocation['allocation_date'] >= date.today():
        await allocations_collection.delete_one({"_id": ObjectId(allocation_id)})
        return True  # Return success if deleted
    return False

async def get_allocation_history(employee_id: Optional[str] = None):
    query = {}
    if employee_id:
        query['employee_id'] = employee_id  # Filter by employee ID if provided
    allocations = await allocations_collection.find(query).to_list(1000)  # Limit to 1000 results
    return allocations

