from collections import deque
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1
        
        visited = set(startGene)
        choices = ['A', 'C', 'G', 'T']
        q = deque([(startGene, 0)])
        while q:
            gene, t = q.popleft()
            for i in range(len(gene)):
                for a in choices:
                    if gene[i] != a:
                        new_gene = gene[:i] + a + gene[i+1:]
                        if new_gene == endGene:
                            return t + 1
                        if new_gene in bank and new_gene not in visited:
                            q.append((new_gene, t + 1))
                            visited.add(new_gene)
        
        return -1