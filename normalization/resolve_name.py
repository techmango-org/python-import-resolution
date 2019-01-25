import utils.constants as const
import categorization.animal_categories as animal_categories


animal_name_map = {
    'DOGY': const.DOG,
    'DOGGY': const.DOG,
    'PUMA': const.CAT,
    'TIGER': const.CAT
}


def get_animal_name(name):
    if name in animal_categories.animal_scores:
        return name

    if name in animal_name_map:
        return animal_name_map[name]

    return None

