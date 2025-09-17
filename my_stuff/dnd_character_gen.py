# AS dnd random gen
import random
stat_1 = int(random.randint(1, 10))
stat_2 = int(random.randint(1, 10))
stat_3 = int(random.randint(1, 10))
stat_4 = int(random.randint(1, 10))
D6outcome = [num_1, num_2, num_3, num_4]
D6outcome.remove(min(D6outcome))
print(D6outcome)