"""
1. Plus One 
Given a non-negative number represented as a list of digits, add 1 to the number
(increment the number represented by the digits). The digits are stored such
that the most significant digit is the first element of the array.

Example 1:

Input: 
N = 3
arr[] = [1, 2, 4]
Output: 
1 2 5
Explanation:
124+1 = 125, and so the Output

Example 2:

Input: 
N = 3
arr[] = [9, 9, 9]
Output: 
1 0 0 0
Explanation:
999+1 = 1000, and so the output

Your Task:
You don't need to read input or print anything. You only need to complete the
function increment() that takes an integer N and an array arr of size N as input
and returns a list of integers denoting the new number which we get after adding
one to the number denoted by the array arr.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1 <= N <= 105
0 <= arri <= 9
"""

class Solution:
    def increment(self, N, arr):
        # Add 1 to the last digit and find carry
        arr[N - 1] += 1
        carry = arr[N - 1] // 10
        arr[N - 1] = arr[N - 1] % 10
        
        # Traverse from the second last digit
        for i in range(N - 2, -1, -1):
            if carry == 1:
                arr[i] += 1
                carry = arr[i] // 10
                arr[i] = arr[i] % 10
        
        # If carry is 1, we need to add a 1 at the beginning of the array
        if carry == 1:
            arr.insert(0, 1)
        
        return arr

# Example usage:
if __name__ == "__main__":
    t = int(input("Enter the number of test cases: "))
    for _ in range(t):
        N = int(input())
        arr = list(map(int, input().split()))
        solution = Solution()
        result = solution.increment(N, arr)
        print(*result)
