class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

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
                

        if '0000' in deadends:
            return -1

        q = deque()
        q.append(["0000", 0])
        visit = set(deadends)

        while q:
            lock, turns = q.popleft()
            if lock == target:
                return turns
            for child in create_permutations(lock):
                if child not in visit:
                    visit.add(child)
                    q.append([child, turns+1])
        
        return -1

            



