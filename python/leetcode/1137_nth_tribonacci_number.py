class Solution:
    def tribonacciHelper(self, n: int, memory: dict) -> int:
        if n in memory: return memory[n]
        
        small_answer = self.tribonacciHelper(n-1, memory) + self.tribonacciHelper(n-2, memory) + self.tribonacciHelper(n-3, memory)
        memory[n] = small_answer
        return small_answer
        
    def tribonacci(self, n: int) -> int:
        memory = {0:0, 1:1, 2:1}
        return self.tribonacciHelper(n, memory)