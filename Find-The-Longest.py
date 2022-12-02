def find_the_longest():
    k = []
    l = []
    for i in range(4):
        word = input("Enter 4 words:")
        k.append(word)
    # print(k)
    a = 0
    for i in k:
        if a < len(i):
            l.append(i)
            a = len(i)           
        # else:
        #     continue
    return f"{l[-1]} is the longest one."
print(find_the_longest())