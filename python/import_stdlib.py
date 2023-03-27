"""there many functions that have been written already and can be reused by any programmer as long as they are availble. you can however recreate your own version of these functions and call them in modules."""

import random
subject = ['history', 'maths', 'science', 'literature', 'geology']

run_sub = random.choice(subject)
print(run_sub)
#in the above code, the choice function is in the random module and can be used anytime it is called.
from random import choice
sub = random.choice(subject)
print(sub)
#the second importation method works just as the first one just that in the case the choice function was imported directly
