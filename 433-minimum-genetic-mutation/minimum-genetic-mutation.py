from collections import deque
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)
        visited = set(startGene)
        if endGene not in bank:
            return -1
        q = deque([(startGene, 0)])
        choices = ['A', 'C', 'G', 'T']
        while q:
            gene, step = q.popleft()
            if gene == endGene:
                return step
            for i in range(len(gene)):
                original_char = gene[i]

                for char in choices:
                    if char == original_char:
                        continue
                    
                    next_gene = gene[:i] + char + gene[i+1:]

                    if next_gene in bank and next_gene not in visited:
                        visited.add(next_gene)
                        q.append((next_gene, step + 1))
        
        return -1
