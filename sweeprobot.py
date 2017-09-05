import time


def findpath(N):
    start = (0,0)
    path = [start]
    actions = [(0,1),(0,-1),(-1,0),(1,0)] #上下左右
    valid_path = [path]
    for i in range(N):
        pathlist = valid_path
        valid_path = []
        for path in pathlist:
            for step in actions:
                #判断下一点是已经在路径中
                next_point = (path[-1][0] + step[0], path[-1][1] + step[1])
                if  next_point not in path:
                    newpath = path[:]
                    newpath.append(next_point)
                    valid_path.append(newpath)
    return len(valid_path)







if __name__ == '__main__':
    start = time.clock()

    b = findpath(12)
    print(b)
    spend = time.clock() -start
    print(spend, 's')