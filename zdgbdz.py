def gigi(sia):
    res=0
    for i in sia:
        res += int(i)
    return res
arr = [1, 2, 3, 4, 5, "6", '7']
print(gigi(arr))
