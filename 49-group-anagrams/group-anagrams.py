class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26

            for ch in s:
                count[ord(ch) - ord('a')] += 1

            hashmap[tuple(count)].append(s)

        return hashmap.values()

# time: O(m * n)
# space: O(m * n)
