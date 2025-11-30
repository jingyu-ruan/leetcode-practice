from collections import defaultdict

class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        # 1. 建图
        graph = defaultdict(dict)
        for (x, y), val in zip(equations, values):
            graph[x][y] = val
            graph[y][x] = 1.0 / val
        
        # 2. 定义 DFS 函数
        def dfs(current_node, target_node, visited):
            # 如果当前节点就是目标，返回 1.0 (乘法的单位元)
            if current_node == target_node:
                return 1.0
            
            visited.add(current_node)
            
            # 遍历邻居
            for neighbor, weight in graph[current_node].items():
                if neighbor not in visited:
                    result = dfs(neighbor, target_node, visited)
                    # 如果找到了路径 (result != -1.0)
                    if result != -1.0:
                        return weight * result
            
            return -1.0

        # 3. 处理每一个查询
        results = []
        for dividend, divisor in queries:
            if dividend not in graph or divisor not in graph:
                results.append(-1.0)
            elif dividend == divisor:
                results.append(1.0)
            else:
                visited = set()
                results.append(dfs(dividend, divisor, visited))
        
        return results