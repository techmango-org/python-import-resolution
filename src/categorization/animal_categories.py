from src.utils import constants as const

animal_scores = {
    const.DOG: 100,
    const.CAT: 300
}


def get_animal_score(animal_name):
    if animal_name in animal_scores:
        return animal_scores[animal_name]

    return const.DEFAULT_ANIMAL_SCORE
