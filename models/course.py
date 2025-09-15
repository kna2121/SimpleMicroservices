from __future__ import annotations

from typing import Optional
from uuid import UUID, uuid4
from datetime import date, datetime
from pydantic import BaseModel, Field

class CourseBase(BaseModel):
    id: UUID = Field(
        default_factory=uuid4,
        description="Persistent Course ID (server-generated).",
        json_schema_extra={"example": "550e8400-e29b-41d4-a716-446655440000"},
    )
    title: str = Field(
        ...,
        description="Course title.",
        json_schema_extra={"example": "Introduction to Python"},
    )
    course_code: Optional[str] = Field(
        None,
        description="Unique course code.",
        json_schema_extra={"example": "COMS1004"},
    )
    professor: str = Field(
        ...,
        description="Course professor.",
        json_schema_extra={"example": "Professor Ferguson"},
    )
    semester: str = Field(
        ...,
        description="The semester the course is offered.",
        json_schema_extra={"example": "Fall 2024"},
    )
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": "550e8400-e29b-41d4-a716-446655440000",
                    "title": "Cloud Computing",
                    "course_code": "COMS4153",
                    "professor": "Professor Ferguson",
                    "semester": "Fall 2025",
                }
            ]
        }
    }

class CourseCreate(CourseBase):
    """Creation payload; ID is generated server-side but present in the base model."""
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "title": "Artificial Intelligence",
                    "course_code": "COMS4701",
                    "professor": "Professor Dear",
                    "semester": "Spring 2025",
                }
            ]
        }
    }
class CourseUpdate(BaseModel):
    """Update payload; all fields optional."""
    title: Optional[str] = Field(
        None,
        description="Course title.",
        json_schema_extra={"example": "Introduction to Python"},
    )
    course_code: Optional[str] = Field(
        None,
        description="Unique course code.",
        json_schema_extra={"example": "COMS1004"},
    )
    professor: Optional[str] = Field(
        None,
        description="Course professor.",
        json_schema_extra={"example": "Professor Ferguson"},
    )
    semester: Optional[str] = Field(
        None,
        description="The semester the course is offered.",
        json_schema_extra={"example": "Fall 2024"},
    )
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "title": "Artificial Intelligence",
                    "course_code": "COMS4701",
                    "professor": "Professor Dear",
                    "semester": "Spring 2025",
                }
            ]
        }
    }

class CourseRead(CourseBase):

    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="Timestamp when the course was created (UTC).",
        json_schema_extra={"example": "2024-10-01T12:00:00Z"},
    )
    updated_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="Timestamp when the course was last updated (UTC).",
        json_schema_extra={"example": "2024-10-01T12:00:00Z"},
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": "550e8400-e29b-41d4-a716-446655440000",
                    "title": "Cloud Computing",
                    "course_code": "COMS4153",
                    "professor": "Professor Ferguson",
                    "semester": "Fall 2025",
                    "created_at": "2024-10-01T12:00:00Z",
                    "updated_at": "2024-10-01T12:00:00Z",
                }
            ]
        }
    }