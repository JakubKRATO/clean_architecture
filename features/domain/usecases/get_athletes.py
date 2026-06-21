from features.domain.entities.athlete_entity import Athlete
from features.domain.repo.athlete_repo import AthleteRepo


class GetAthletes:

    def __init__(self, athlete_repo : AthleteRepo):
        self.athlete_repo = athlete_repo

    def __call__(self) -> list[Athlete]:
        return self.athlete_repo.get_athletes()