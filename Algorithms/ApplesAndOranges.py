def countApplesAndOranges(s, t, a, b, apples, oranges):
    print(sum(s<=a+i<=t for i in apples))
    print(sum(s<=b+i<=t for i in oranges))
    