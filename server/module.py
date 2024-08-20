from pydantic import BaseModel
from typing import Optional


class Troops(BaseModel):
    id: int
    name: str
    idx: int
    type: str
    priority: int
    role_number: int
    base: str


class TroopsTemplate(BaseModel):
    id: int
    type: Optional[str]
    name: Optional[str]
    aos: Optional[str]
    level: Optional[str]
    g1: Optional[str]
    g1_s1: Optional[str]
    g1_s2: Optional[str]
    g2: Optional[str]
    g2_s1: Optional[str]
    g2_s2: Optional[str]
    g3: Optional[str]
    g3_s1: Optional[str]
    g3_s2: Optional[str]


class UserStrategy(BaseModel):
    id: int
    role_number: int
    troops_level: int
    barracks_level: int
    max_defenders: int
    land_level: int


class UserTroops(BaseModel):
    id: int
    role_number: int
    type: str
    name: Optional[str]
    aos: Optional[str]
    level: Optional[str]
    g1: Optional[str]
    g1_s1: Optional[str]
    g1_s2: Optional[str]
    g2: Optional[str]
    g2_s1: Optional[str]
    g2_s2: Optional[str]
    g3: Optional[str]
    g3_s1: Optional[str]
    g3_s2: Optional[str]
