def add(*l) :
    sum = 0
    for p in l :
        sum += p
    return sum

test = 100

print("caldLib2 name", __name__)
if __name__ == "__main__" :
    r = add(1,2,3,4)
    print(r)

