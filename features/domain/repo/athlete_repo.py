from abc import ABC, abstractmethod

from features.domain.entities.athlete_entity import Athlete

class AthleteRepo(ABC):
    
    @abstractmethod
    def get_athletes(self) -> list[Athlete]:
        pass

    @abstractmethod
    def create_athlete(self, athlete: Athlete) -> None:
        pass

    @abstractmethod
    def get_athlete_by_id(self, id: str) -> Athlete:
        pass