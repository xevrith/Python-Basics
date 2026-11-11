msg = "hello world"


msg_count = {}
for char in msg:
    if char in msg_count:
        msg_count[char] += 1
    else:
        msg_count[char] = 1


print(msg_count)