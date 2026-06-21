from features.domain.entities.athlete_entity import Athlete
from injector import container

if __name__ == "__main__":

    print(container.get_athletes())
    container.create_athlete(Athlete("testing", "MenoBu", 50))
    container.create_athlete(Athlete("iny", "derName", 5))
    container.create_athlete(Athlete("tri", "meno", 40))
    print(container.get_athletes())


    # getting athlete by id
    print(container.get_athlete_by_id("iny"))
