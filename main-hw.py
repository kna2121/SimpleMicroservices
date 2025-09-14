from __future__ import annotations

import os
import socket
from datetime import datetime

from typing import Dict, List
from uuid import UUID

from fastapi import FastAPI, HTTPException
from fastapi import Query, Path
from typing import Optional

from models.person import PersonCreate, PersonRead, PersonUpdate
from models.address import AddressCreate, AddressRead, AddressUpdate
from models.health import Health

from models.course import CourseCreate, CourseRead, CourseUpdate
from models.department import DepartmentCreate, DepartmentRead, DepartmentUpdate

port = int(os.environ.get("FASTAPIPORT", 8000))

# -----------------------------------------------------------------------------
# Fake in-memory "databases"
# -----------------------------------------------------------------------------

courses: Dict[UUID, CourseRead] = {}
departments: Dict[str, DepartmentRead] = {}

app = FastAPI(
    title="Person/Address API",
    description="Demo FastAPI app using Pydantic v2 models for Course and Department",
    version="0.1.0",
)


# -----------------------------------------------------------------------------
# Course endpoints
# -----------------------------------------------------------------------------
@app.post("/courses", response_model=CourseRead, status_code=201)
def create_course(course: CourseCreate):
    # Each person gets its own UUID; stored as PersonRead
    course_read = CourseRead(**course.model_dump())
    courses[course_read.id] = course_read
    return course_read

@app.get("/courses", response_model=List[CourseRead])
def list_courses(
    course_code: Optional[str] = Query(None, description="Filter by course code"),
    title: Optional[str] = Query(None, description="Filter by course title"),
    professor: Optional[str] = Query(None, description="Filter by professor"),
    semester: Optional[str] = Query(None, description="Filter by semester"),
):
    results = list(courses.values())

    if course_code is not None:
        results = [c for c in results if c.course_code == course_code]
    if title is not None:
        results = [c for c in results if c.title == title]
    if professor is not None:
        results = [c for c in results if c.professor == professor]
    if semester is not None:
        results = [c for c in results if c.semester == semester]

    return results



# -----------------------------------------------------------------------------
# Root
# -----------------------------------------------------------------------------
@app.get("/")
def root():
    return {"message": "Welcome to the Course/Department API. See /docs for OpenAPI UI."}

# -----------------------------------------------------------------------------
# Entrypoint for `python main.py`
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
