# 3376. Minimum Time to Break Locks I : Runtime 2805ms Beats 58.60%

class Solution:
    def findMinimumTime(self, strength: List[int], k: int) -> int:
        time = 0
        x = 1
        energy = 0
        strength.sort(reverse=True)
        hq = []
 
        def find(strength, energy, x, k, time, hq):
            while strength:
                # breakable
                if strength[-1] <= energy:
                    # find max value
                    for i in reversed(range(len(strength))):
                        if strength[i] > energy:
                            i += 1
                            break
 
                    # 다음 값을 먼저 고른 결과 저장
                    if i > 0:
                        wait_cnt = (strength[i - 1] - energy) // x
                        if (strength[i - 1] - energy) % x != 0:
                            wait_cnt += 1
                        tmp_time = time + wait_cnt
                        tmp_energy = energy + (x * wait_cnt)
                        find(strength[:], tmp_energy, x, k, tmp_time, hq)
 
                    strength.pop(i) # break
                    if not strength:
                        break
 
                    energy = 0
                    x += k
 
                wait_cnt = (strength[-1] - energy) // x
                if (strength[-1] - energy) % x != 0:
                    wait_cnt += 1
 
                time += wait_cnt
                energy += (x * wait_cnt)
 
                if hq and hq[0] <= time:
                    return
 
            heapq.heappush(hq, time)
 
        find(strength[:], energy, x, k, time, hq)
 
        return heapq.heappop(hq)