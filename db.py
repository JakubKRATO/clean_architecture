class DB:

    athletes = list()

    def get_athletes(self) -> list[dict]:
        return self.athletes
    
    def create_athlete(self, athlete) -> None:
        self.athletes.append(athlete)

    def get_athlete_by_id(self, id) -> dict:
        for item in self.athletes:
            if item["id"] == id:
                return item
            
        return None