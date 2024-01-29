def bfs(res_cap, source, destination):
    visited = [-1 for i in range(len(res_cap))]
    visited[source] = source
    queue = [source]
    # Determin blowing flow
    while len(queue) > 0:
        top = queue.pop(0)
        for i in range(len(res_cap)):
            if (res_cap[top][i][1] - res_cap[top][i][0]) != 0 and visited[i] == -1:
                if i == destination:
                    # Get bunny route
                    visited[destination] = top
                    paths = [destination]
                    temp = destination
                    while temp != source:
                        temp = visited[temp]
                        paths.append(temp)
                    paths.reverse()
                    # Get flow value and update augmented graph
                    temp = 1
                    result = float("inf")
                    cur = source
                    while temp != len(paths):
                        entry = res_cap[cur][paths[temp]]
                        diff = abs(entry[1]) - entry[0]
                        result = min(result, diff)
                        cur = paths[temp]
                        temp += 1
                    temp = 1
                    cur = source
                    while temp != len(paths):
                        entry = res_cap[cur][paths[temp]]
                        if entry[1] < 0:
                            entry[1] += result
                        else:
                            entry[0] += result
                        entry = res_cap[paths[temp]][cur]
                        if entry[1] <= 0:
                            entry[1] -= result
                        else:
                            entry[0] += result
                        cur = paths[temp]
                        temp += 1
                    return True
                else:
                    visited[i] = top
                    queue.append(i)
    return False

def solution(ents, exits, paths):
    # Max flow problem solved using Dinic's algorithm

    # Find the maxium amount of bunnies that can be in all paths
    max_val = sum(list(map(sum, paths)))

    # Create network of edges
    res_cap = []
    for i in range(len(paths)):
        res_cap.append([])
        for j in range(len(paths[i])):
            res_cap[i].append([0, paths[i][j]])
        res_cap[i].append([0, 0])
        if i in exits:
            res_cap[i].append([0, max_val])
        else:
            res_cap[i].append([0, 0])
    res_cap.extend([[],[]])

    for i in range(len(paths[0]) + 2):
        if i in ents:
            res_cap[-2].append([0, max_val])
        else:
            res_cap[-2].append([0, 0])
        res_cap[-1].append([0, 0])

    # Calculate until False
    while bfs(res_cap, source=len(res_cap)-2, destination=len(res_cap)-1):
        pass

    # Add the maxium in paths together to get max flow
    result = 0
    for i in range(len(res_cap)):
        result += res_cap[-2][i][0]

    return result

if __name__ in '__main__':
    result = solution([0], [3], 
                        [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]])
    print(result)