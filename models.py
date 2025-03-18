from dataclasses import dataclass
from typing import Optional

@dataclass
class Driver:
    name: str
    age: int
    pole_positions: int
    race_wins: int
    points_scored: int
    world_titles: int
    fastest_laps: int
    team: str
    id: Optional[str] = None

@dataclass
class Team:
    name: str
    year_founded: int
    pole_positions: int
    race_wins: int
    constructor_titles: int
    previous_season_position: int
    id: Optional[str] = None
