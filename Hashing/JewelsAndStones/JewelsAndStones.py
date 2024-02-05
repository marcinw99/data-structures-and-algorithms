def numJewelsInStones(jewels, stones):
    jewelsSet = set(jewels)
    return sum(s in jewelsSet for s in stones)
