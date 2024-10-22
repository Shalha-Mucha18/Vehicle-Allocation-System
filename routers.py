from fastapi import APIRouter, HTTPException
from app.crud import create_allocation, update_allocation, delete_allocation, get_allocation_history
from app.models import AllocationCreate, AllocationUpdate


router = APIRouter()  # Initialize an APIRouter

@router.post("/allocate/")
async def allocate_vehicle(allocation: AllocationCreate):
    result = await create_allocation(allocation.employee_id, allocation.vehicle_id, allocation.allocation_date)
    if not result:
        raise HTTPException(status_code=400, detail="Vehicle already allocated for the day")
    return result  # Return the allocation details


@router.put("/allocate/{allocation_id}")   #Endpoint to update a vehicle allocation
async def update_vehicle_allocation(allocation_id: str, update_data: AllocationUpdate):
    if await update_allocation(allocation_id, update_data.allocation_date):
        return {"status": "updated"}  # Return success response
    raise HTTPException(status_code=400, detail="Update failed")

# Endpoint to delete an allocation before the allocation date
@router.delete("/allocate/{allocation_id}")
async def delete_allocation(allocation_id: str):
    if await delete_allocation(allocation_id):
        return {"status": "deleted"}  # Return success response
    raise HTTPException(status_code=400, detail="Delete failed")

# Endpoint to get the allocation history with optional filters
@router.get("/allocations/")
async def get_allocation_report(employee_id: str = None):
    return await get_allocation_history(employee_id)  # Return filtered or all allocation history

