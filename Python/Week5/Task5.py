# 5. Generate a lottorow  (try to use an array here).
import random

values = []

for i in range(1,41):
    values.append(i)

lotto = random.sample(values, k=7)
lotto.sort()


# lotto = random.sample(range(1,41), k=7)
# lotto.sort()
print("Your lottorow is:",lotto)


