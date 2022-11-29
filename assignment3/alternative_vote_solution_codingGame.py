c = int(input())
names = [input() for _ in range(c)]

dict = {i+1 : element for i,element in enumerate(names)}

v = int(input())
votes = [list(map(lambda x: int(x),input().split())) for _ in range(v)]

while len(dict) > 0:
    counts = {i : 0 for i in dict}

    for i in range(v):
        if votes[i][0] in dict:
            counts[votes[i][0]]+=1
        else:
            while len(votes[i]) > 0 and votes[i][0] not in dict:
                votes[i].pop(0)
            if len(votes[i]) > 0:
                counts[votes[i][0]]+=1

    sorted_countings = sorted(counts.items(),key=lambda tup: tup[1])
    
    candidates = sorted(filter(lambda x: x[1] == sorted_countings[0][1], sorted_countings), key=lambda tup: tup[0])

    if len(dict) == 1:
        print("winner:",end="")
    print(dict.pop(candidates[0][0]))