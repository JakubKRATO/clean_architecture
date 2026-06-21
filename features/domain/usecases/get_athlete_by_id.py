
from features.domain.repo.athlete_repo import AthleteRepo


class GetAthleteById:
    def __init__(self, athelete_repo: AthleteRepo):
        self.athelete_repo = athelete_repo

    def __call__(self, id: str):
        return self.athelete_repo.get_athlete_by_id(id)