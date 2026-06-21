from abc import ABC, abstractmethod

from db import DB
from features.data.models.athlete_model import AthleteModel
from features.domain.entities.athlete_entity import Athlete

class AthleteRemoteData(ABC):

    @abstractmethod
    def get_athletes(self) -> list[AthleteModel]:
        pass

    @abstractmethod
    def create_athlete(self, athlete: AthleteModel) -> None:
        pass

    @abstractmethod
    def get_athlete_by_id(self, id: str) -> Athlete:
        pass


class AthleteRemoteDataImpl(AthleteRemoteData):
    def __init__(self, db: DB):
        super().__init__()
        self.db = db

    def get_athletes(self) -> list[AthleteModel]:
        athletes_dict = self.db.get_athletes()

        athletes = list()
        for athlete_dict in athletes_dict:
            athletes.append(AthleteModel.from_json(athlete_dict))

        return athletes

    def create_athlete(self, athlete):
        self.db.create_athlete(athlete.to_json())

    def get_athlete_by_id(self, id):
        return self.db.get_athlete_by_id(id)

