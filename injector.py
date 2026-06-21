from db import DB
from features.data.datasources.athlete_remote_data import AthleteRemoteData, AthleteRemoteDataImpl
from features.data.repo.athlete_repo_impl import AthleteRepoImpl
from features.domain.repo.athlete_repo import AthleteRepo
from features.domain.usecases.create_athlete import CreateAthlete
from features.domain.usecases.get_athlete_by_id import GetAthleteById
from features.domain.usecases.get_athletes import GetAthletes


class Container:
    def __init__(self) -> None:
        # Endpoints
        self.db: DB = DB()

        # Datasources
        self.athlete_remote_data: AthleteRemoteData = AthleteRemoteDataImpl(self.db)

        #Repositories
        self.athlete_repo: AthleteRepo = AthleteRepoImpl(self.athlete_remote_data)

        # JE TOTO HORE AGREGACIA ?? (mame jeden repo kde su remote data a v nasom pripade by bol ten firebaseData object?)

        # UseCases
        self.get_athletes: GetAthletes = GetAthletes(self.athlete_repo)
        self.create_athlete: CreateAthlete = CreateAthlete(self.athlete_repo)
        self.get_athlete_by_id: GetAthleteById = GetAthleteById(self.athlete_repo)

container: Container = Container()