from collections import deque

def solution(maps):
    row = len(maps)
    col = len(maps[0])
    
    visited = [[1] * col for _ in range(row)]
    
    def bfs():
        q = deque([(0, 0, 1)])
        visited[0][0] = 0
        while q:
            x, y, count = q.popleft()
            
            if x == row - 1 and y == col - 1:
                return count
            
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < row and 0 <= ny < col and visited[nx][ny] and maps[nx][ny]:
                    q.append((nx, ny, count + 1))
                    visited[nx][ny] = 0
    
        return -1
    
    return bfs()