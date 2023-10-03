"""
6. Remove duplicate elements from a sorted Array
Given a sorted array A of size N, delete all the duplicate elements from A.
Note: Don't use a set or dictionary to solve the problem.

Example 1:

Input:
N = 5
Array = [2, 2, 2, 2, 2]
Output: [2]
Explanation: After removing all the duplicates, only one instance of 2 will remain.

Example 2:

Input:
N = 3
Array = [1, 2, 2]
Output: [1, 2]

Your Task:
You don't need to read input or print anything. Complete the function remove_duplicate() which takes the array A[] and its size N as input parameters and modifies it in place to delete all the duplicates. The function must return an integer X denoting the new modified size of the array.
Note: The generated output will print all the elements of the modified array from index 0 to X-1.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ N ≤ 104
1 ≤ A[i] ≤ 106
"""

class Solution:
    def remove_duplicate(self, A, N):
        if N == 0:
            return 0

        i = 0
        for j in range(1, N):
            if A[j] != A[i]:
                i += 1
                A[i] = A[j]

        return i + 1

# Example usage:
if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        solution = Solution()
        new_size = solution.remove_duplicate(A, N)
        for i in range(new_size):
            print(A[i], end=" ")
        print()
