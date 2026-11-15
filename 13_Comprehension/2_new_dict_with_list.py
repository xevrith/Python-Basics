key = [1,2,3,4,5]
value = ["a","b","c","d","e"]

new_dict = {k:v for k,v in zip(key,value)}
print(new_dict)