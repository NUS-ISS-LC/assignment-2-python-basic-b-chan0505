def find(s, n):
# write your implementation here
    for i in range(len(s)):
        for j in range(len(s)):
            if i != j and (s[i] + s[j] == n):
                return [i, j]
    return None

# -- TEST --
numlist_1 = [2,7,11,15]
target_1 = 9
print(find(numlist_1,target_1))
print("---")
numlist_2 = [3,2,4,5]
target_2 = 7
print(find(numlist_2,target_2))