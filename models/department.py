from __future__ import annotations

from typing import Optional, Annotated, List
from uuid import UUID, uuid4
from datetime import datetime
from pydantic import BaseModel, Field, StringConstraints

from .course import CourseBase

DeptCode = Annotated[str, StringConstraints(pattern=r"^[A-Z]{2,6}$")]

class DepartmentBase(BaseModel):
    code: DeptCode = Field(
        ...,
        description="Persistent Department ID .",
        json_schema_extra={"example": "COMS"},
    )
    name: str = Field(
        ...,
        description="Department name.",
        json_schema_extra={"example": "Computer Science"},
    )
    
    chair: Optional[str] = Field(
        None,
        description="Department head.",
        json_schema_extra={"example": "Dr. Smith"},
    )
    courses: List[CourseBase] = Field(
        default_factory=list,
        description="Courses in this department (each carries a persistent Course ID).",
        json_schema_extra={
            "example": [
                {
                    "course_code": "COMS 4153",
                    "title": "Cloud Computing",
                    "professor": "Professor Ferguson",
                    "semester": "Fall 2025"
                }
            ]
        },
    )
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "code": "COMS",
                    "name": "Computer Science",
                    "chair": "Professor Carloni",
                    "courses": [
                        {
                            "course_code": "COMS 4153",
                            "title": "Cloud Computing",
                            "professor": "Professor Ferguson",
                            "semester": "Fall 2025",
                        }
                    ],
                }
            ]
        }
    }

class DepartmentCreate(DepartmentBase):
    """Creation payload for a Department."""
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "code": "COMS",
                    "name": "Computer Science",
                    "chair": "Professor Carloni",
                    "courses": [
                        {
                            "course_code": "COMS 4153",
                            "title": "Cloud Computing",
                            "professor": "Professor Ferguson",
                            "semester": "Fall 2025",
                        }
                    ],
                }
            ]
        }
    }
class DepartmentUpdate(BaseModel):
    """Update payload; all fields optional."""
    code: Optional[DeptCode] = Field(
        None, description="Department Code.", json_schema_extra={"example": "HIST"}
    )
    name: Optional[str] = Field(
        None,
        description="Department name.",
        json_schema_extra={"example": "History"},
    )
    chair: Optional[str] = Field(
        None,
        description="Department head.",
        json_schema_extra={"example": "Dr. Smith"},
    )
    courses: Optional[List[CourseBase]] = Field(
        None,
        description="Replace the entire set of courses with this list.",
        json_schema_extra={
            "example": [
                {
                    "course_code": "COMS 4153",
                    "title": "Cloud Computing",
                    "professor": "Professor Ferguson",
                    "semester": "Fall 2025",
                }
            ]
        },
    )
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "code": "COMS",
                    "name": "Computer Science",
                    "chair": "Professor Carloni",
                }
            ]
        }
    }

class DepartmentRead(DepartmentBase):
    id: UUID = Field(
            default_factory=uuid4,
            description="Server-generated Department ID.",
            json_schema_extra={"example": "99999999-9999-4999-8999-999999999999"},
    )
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="Timestamp when the department was created (UTC).",
        json_schema_extra={"example": "2024-10-01T12:00:00Z"},
    )
    updated_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="Timestamp when the department was last updated (UTC).",
        json_schema_extra={"example": "2024-10-01T12:00:00Z"},
    )
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": "99999999-9999-4999-8999-999999999999",
                    "code": "COMS",
                    "name": "Computer Science",
                    "chair": "Professor Carloni",
                    "courses": [
                        {
                            "course_code": "COMS 4153",
                            "title": "Cloud Computing",
                            "professor": "Professor Ferguson",
                            "semester": "Fall 2025",
                        }
                    ],
                    "created_at": "2024-10-01T12:00:00Z",
                }
            ]
        }
    }