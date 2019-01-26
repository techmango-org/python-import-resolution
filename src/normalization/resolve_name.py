from src.utils import constants as const
from src.categorization import animal_categories as ac

animal_name_map = {
    'DOGY': const.DOG,
    'DOGGY': const.DOG,
    'PUMA': const.CAT,
    'TIGER': const.CAT
}


def get_animal_name(name):
    if name in ac.animal_scores:
        return name

    if name in animal_name_map:
        return animal_name_map[name]

    return None
