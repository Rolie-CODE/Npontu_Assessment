from pydantic import BaseModel

class InputData(BaseModel):
    age: int
    sleep_hours: float
    stress_level: int
    anxiety_level: int
    physical_activity: int
    academic_performance: int