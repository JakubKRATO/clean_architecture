from features.data.datasources.athlete_remote_data import AthleteRemoteData
from features.data.models.athlete_model import AthleteModel
from features.domain.entities.athlete_entity import Athlete
from features.domain.repo.athlete_repo import AthleteRepo


class AthleteRepoImpl(AthleteRepo):
    def __init__(self, datasource: AthleteRemoteData):
        super().__init__()
        self.datasource = datasource

    def get_athletes(self) -> list[Athlete]:
        return [athlete.to_entity() for athlete in self.datasource.get_athletes()]

    def create_athlete(self, athlete):
        return self.datasource.create_athlete(AthleteModel.from_entity(athlete))
    
    def get_athlete_by_id(self, id):
        return self.datasource.get_athlete_by_id(id)


