import sys
import heapq

def dijkstra(graph, start):
    dist = [float('inf')] * len(graph)
    dist[start] = 0
    pq = [(0, start)]
    
    while pq:
        curr_dist, curr_node = heapq.heappop(pq)
        
        if curr_dist > dist[curr_node]:
            continue
        
        for neighbor, weight in graph[curr_node]:
            new_dist = curr_dist + weight
            
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
    
    return dist

def main():
    T = int(input())
    
    for _ in range(T):
        n = int(input())
        graph = [[] for _ in range(10**9 + 5)]
        total_cost = 0
        
        for i in range(n):
            ai, ci = map(int, input().split())
            graph[0].append((ai, ci))
        
        dist = dijkstra(graph, 0)
        
        for i in range(1, 10**9 + 5):
            if dist[i] != float('inf'):
                total_cost += dist[i]
                break
        else:
            print(-1)
            continue
        
        for i in range(1, 10**9 + 5):
            for ai, ci in graph[i]:
                if dist[i] + ai < dist[i - ai]:
                    total_cost += ci
                    break
            else:
                continue
            break
        
        print(total_cost)

if __name__ == "__main__":
    main()