def create_permutations(s):
        children = []

        for i in range(len(s)):
            decimal = int(s[i])
            move_up_char = str((decimal + 1) % 10)
            move_down_char = str((decimal + 9) % 10)

            move_up_str, move_down_str = s, s
            move_up_str = s[:i] + move_up_char + s[i+1:]
            move_down_str = s[:i] + move_down_char + s[i+1:]

            children.append(move_up_str)
            children.append(move_down_str)
        return children

print(create_permutations("0000"))