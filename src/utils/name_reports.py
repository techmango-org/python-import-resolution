from src.normalization import resolve_name as rn
from src.categorization import animal_categories as ac

test_name = 'DOGY'
resolved_name = rn.get_animal_name(test_name)

print('********ANIMAL CATEGORY IS:', ac.get_animal_score(resolved_name))
