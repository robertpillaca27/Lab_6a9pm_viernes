
l1 = [("one", 1), ("two", 2), ("three", 3), ("four", 4), ("five", 5)] 
l2 = [("one", 1), ("two", 2), ("six", 6)]

s1 = set(l1)
s2 = set(l2)
print(s1)
print(s2,'\n')

s3 = s1 & s2
print(s3,'\n')

s4 = (s1 - s2) | (s2 - s1)
print(s4)
