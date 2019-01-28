import src.normalization.resolve_name as rn
import src.categorization.animal_categories as ac

test_name = 'DOGY'
resolved_name = rn.get_animal_name(test_name)

print('********ANIMAL CATEGORY IS:', ac.get_animal_score(resolved_name))
