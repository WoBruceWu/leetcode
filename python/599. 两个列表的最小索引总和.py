class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        hash_map = dict()
        res_sum = 0xffffffff
        res = []
        for idx, s in enumerate(list1):
            hash_map[s] = idx
        for idx, s in enumerate(list2):
            if s in hash_map:
                if res_sum > idx + hash_map[s]:
                    res_sum = idx + hash_map[s]
                    res = [list2[idx]]
                elif res_sum == idx + hash_map[s]:
                    res.append(list2[idx])
        return res