class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:

        groups = {}

        for idx, groupsize in enumerate(groupSizes):
            if str(groupsize) in groups:
                placed = False
                placement_key = str(groupsize)

                while not placed:
                    if placement_key in groups:
                        if len(groups[placement_key]) == groupsize:
                            placement_key += "_1"
                        else:
                            groups[placement_key].append(idx)
                            placed = True
                    else:
                        groups[placement_key] = [idx]
                        placed =True

            else:
                groups[str(groupsize)] = [idx]

        outlist = []

        for group in groups:
            outlist.append(groups[group])

        return outlist       