from pydantic import BaseModel
from datetime import date
from typing import Optional

class Vehicle(BaseModel):  ## Model for vehicle information
    vehicle_id: str
    driver_name: str  # Each vehicle has a pre-assigned driver

# Model for employee information
class Employee(BaseModel):
    employee_id: str
    name: str  # Name of the employee


class AllocationCreate(BaseModel):  ## Model for creating a new vehicle allocation
    employee_id: str
    vehicle_id: str
    allocation_date: date  # The date for which the vehicle is allocated

# Model for updating an existing allocation
class AllocationUpdate(BaseModel):
    allocation_date: Optional[date]  # New allocation date (optional)

# Model for representing an allocation record
class Allocation(BaseModel):
    employee_id: str
    vehicle_id: str
    allocation_date: date
    status: str
