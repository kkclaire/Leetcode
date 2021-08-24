
class Solution:
    def openLock(self, deadends, target):
        from collections import deque
        bases = [1, 10, 100, 1000]
        deads = set(int(x) for x in deadends)
        start, goal = int('0000'), int(target)
        if start in deads: return -1
        if start == goal: return 0
        q = deque([(start, 0)])
        visited = set([start])
        while q:
            node, step = q.popleft()
            for i in range(0, 4):
                # take individual digit from the lowest to the highest
                r = (node // bases[i]) % 10
                for j in [-1, 1]:
                    # -r is used to recover the 4 digit, because r can only add or minus 1, so use the changed digit - r will get 1 or -1, then multiply the base we can recover each bit
                    nxt = node + ((r + j + 10) % 10 - r) * bases[i]
                    if nxt == goal: return step + 1
                    if nxt in deads or nxt in visited: continue
                    q.append((nxt, step + 1))
                    visited.add(nxt)
        return -1

test = Solution()
print(test.openLock(["0201","0101","0102","1212","2002"], "0202"))