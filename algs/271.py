def encode(strs):
    builder = ""
    for s in strs:
        builder += str(len(s)) + "#" + s

    return builder


def decode(s):
    res = []

    start_idx = 0

    while start_idx < len(s):

        print(start_idx)

        index_offset_builder = ""
        end_idx = start_idx
        while s[end_idx] != "#":
            end_idx += 1

        length = int(s[start_idx:end_idx])

        start_idx = end_idx + 1
        end_idx = start_idx + length

        res.append(s[start_idx:end_idx])
        
        start_idx = end_idx

    return res

# print(encode([":", "!@#$%^&*()", "ourlist"]))
print(decode("4#this2#is7#ourlist"))