~~~python
w=4
h=4

mmap = [
    "#S..",
    "E#..",
    "#...",
    "...."
]

xx = [1, 0, 0, -1]
yy = [0, 1, -1, 0]

vis = []
for i in range(w):
    tmp = []
    for j in range(h):
        tmp.append([0]*5)
    vis.append(tmp)

queue = []
current_state = (0,1, 5)
endx = 1
endy = 0
vis[current_state[0]][current_state[1]][current_state[2]-1] = 1
queue.append(current_state)
time = 1
while queue:
    tmp_queue = []
    for current in queue:
        for t in range(5):
            if t == 4: # jump
                dx = h - current[0] -1 
                dy = w - current[1] -1
                djump = current[2] - 1
            else:
                dx = current[0] + xx[t]
                dy = current[1] + yy[t]
                djump = current[2]
            

            if dx >= 0 and dx < h and dy >= 0 and dy < w and djump >= 0 and not vis[dx][dy][djump-1] and mmap[dx][dy] != "#":
                if dx == endx and dy == endy:
                    print(time)
                    exit()
                vis[dx][dy][djump-1] = 1
                state = (dx, dy, djump)
                tmp_queue.append(state)
    queue = tmp_queue
    time += 1
~~~

