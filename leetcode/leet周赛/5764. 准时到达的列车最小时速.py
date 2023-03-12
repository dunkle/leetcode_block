class Solution:
    def minSpeedOnTime(self, dist, hour: float):
        # 至少需要len(dist)-1小时 时速最小为1h 至多需要sum(dist)
        minhour = len(dist)-1
        # 最小的速度就是 最小路程 除以 每段路程需要的最大时间 一小时。 1/1 = 1
        #
        minspeed = int(sum(dist)/int(hour))
        minspeed = max(minspeed, 1)
        # 最大时速 依据 hour 最小单位值，0.01 因此，最后一段路程花费的最小时间也就是 0.01 最大路程 1 <= dist[i] <= 10^5
        # 因此速度 dist[i]/ min hour = 10^7 最大也就是 这么大的速度
        max_speed = 10**7
        if minhour>hour:
            return -1
        n = len(dist)
        def is_valid(minspeed):
            hourstart = 0
            for i in range(n-1):
                if dist[i]%minspeed==0:
                    hourstart+=dist[i]//minspeed
                else:
                    hourstart = hourstart+ dist[i]//minspeed + 1
            hour_final = dist[n-1]*1.0/minspeed
            hourstart+=hour_final
            if hourstart<=hour:
                return True
            return False
        l = minspeed
        r = max_speed
        while l<r:
            mid = (l+r)//2
            if is_valid(mid):
                r = mid-1
            else:
                l = mid+1
        return l

a = Solution()
dist = [1,3,2]
hour = 2.7
# dist = [1,3,2,5]
# hour = 6
# dist = [1,3,2]
# hour = 1.9
# dist = [2,1,5,4,4,3,2,9,2,10]
# hour = 75.12
res = a.minSpeedOnTime(dist, hour)
print(res)