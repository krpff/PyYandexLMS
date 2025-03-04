from datetime import date, time
from typing import List, Optional, Union

from PyYandexLMS.models.base import BaseModel, BaseUser, Group


class SchedulePlanItem(BaseModel):
    id: int
    schedule_plan: int
    day_of_week: int
    start_time: time


class SchedulePlan(BaseModel):
    id: int
    group: int
    study_period: int
    start_date: date
    items: List[SchedulePlanItem]


class Progress(BaseModel):
    num_tasks: Optional[int]
    num_passed: Optional[int]
    num_rework: Optional[int]


class Course(BaseModel):
    id: int
    title: str
    teacher: Union[BaseUser, None]
    teachers_list: Union[List[BaseUser], None]
    group: Group
    rating: float
    bonus_score: float
    progress: Progress
    use_bonus_score: bool
    max_bonus_score: float
    certificate_id: Union[int, None]
    pass_type: str
    certificate_number: Union[str, None]
    logo: Union[str, None]
    logo_height: Union[int, None]
    logo_width: Union[int, None]
    is_archive: bool
    is_active: bool
    status: str
    events_count: int
    visited_attendances_count: int
    schedule_plan: SchedulePlan


class CoursesSummary(BaseModel):
    student: Union[List[Course], None]
    teacher: Union[List[BaseUser], None]
