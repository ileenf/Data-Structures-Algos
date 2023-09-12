class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        def split_group(group, size):
            groups = []
            curr_group = []
            for i, p in enumerate(group):
                if i % size == 0:
                    if curr_group:
                        groups.append(curr_group)
                    curr_group = [p]
                else:
                    curr_group.append(p)
            groups.append(curr_group)
            return groups

        groups = defaultdict(list)
        split_groups = []

        for p, group_size in enumerate(groupSizes):
            groups[group_size].append(p)
        

        for size, group in groups.items():
            if len(group) > size:
                for g in split_group(group, size):
                    split_groups.append(g)
            else:
                split_groups.append(group)

        return split_groups
