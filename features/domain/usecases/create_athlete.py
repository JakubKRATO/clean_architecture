

from features.domain.entities.athlete_entity import Athlete
from features.domain.repo.athlete_repo import AthleteRepo


class CreateAthlete():

    def __init__(self, athlete_repo: AthleteRepo):
        self.athlete_repo = athlete_repo

    def __call__(self, athlete: Athlete):
        return self.athlete_repo.create_athlete(athlete)