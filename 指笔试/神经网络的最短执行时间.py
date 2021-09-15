import sys
class Solution():
    def mintimeop(self, n):
        for i in range(n):
            # 读取每一行
            line = sys.stdin.readline().strip()
            # 把每一行的数字分隔后转化成int列表
            line = list(line.split())
            ops = line[0]
            values = list(map(int, line[1:]))
            val_ops.append(values)
            allops.append(values[1:])
        # print(val_ops)

        listnode = {}
        for i in range(n):
            if not allops[i]:
                listnode[i] = "#"
                continue

            listnode[i] = allops[i]
        # print(listnode)

        queue = [(0,0)]
        maxres = val_ops[0][0]
        while queue:
            # print("queue", queue)
            nownode, nowval = queue.pop()
            # print("nownode",nownode, nowval)

            # print("maxres", nowval+val_ops[nownode][0])

            nowval = nowval+val_ops[nownode][0]

            nodes = listnode[nownode]
            # print("nodes____", nodes)
            for i in range(len(nodes)):
                if '#' ==nodes[i]:
                    continue
                maxres = max(maxres, nowval+val_ops[nodes[i]][0])
                # print("aa", (nodes[i],nowval+val_ops[nodes[i]][0]))
                queue.append((nodes[i],nowval))
        # print(allops)
        print(maxres)

if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    ans = 0
    allops = []
    val_ops = []
    if n==0:
        print(0)
    else:
        a = Solution()
        a.mintimeop(n)

