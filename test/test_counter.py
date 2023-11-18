from models import Counter

varrs = [[1,2,3,4,5],[1,2,3],[1,2,3,4],[1,2,3,4,5,6,7]]
counter = Counter(varrs)

print(counter.counter)
while(counter.increment()):
    print(counter.counter)