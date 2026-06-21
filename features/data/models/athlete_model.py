from dataclasses import dataclass

from core.constants import DEFAULT_BELT
from features.domain.entities.athlete_entity import Athlete

@dataclass
class AthleteModel:
    id: str
    name: str
    points: int
    belt: str

    def from_json(data):
        return AthleteModel(
            id=str(data["id"]),
            name=data["name"],
            points=data["points"],
            belt=data["belt"]
        )
    
    def to_json(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "points": self.points,
            "belt": self.belt
        }
    
    def from_entity(entity: Athlete):
        return AthleteModel(
            id=entity.id,
            name=entity.name,
            points=entity.points,
            belt=DEFAULT_BELT
        )

    def to_entity(self):
        return Athlete(
            id=self.id,
            name=self.name,
            points=self.points,
        )
