#User function Template for python3

# class Solution:
#     def sum(self, N, M):
#         # code here
#         G = 1
#         for i in range(1,min(N,M)+1):
#             if(N%i == 0 and M%i == 0):
#                 G = i
#         return (int(N/G + M/G))

class Solution:
    def sum(self, N, M):
        # code here
        G = self.gcd(N,M) if(min(N,M)==M) else self.gcd(M,N)
        return (int(N/G) + int(M/G))
        
    def gcd(self, A, B):
        while B != 0:
            A, B = B, int(A%B)
        return A

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N,M = map(int,input().strip().split())

        ob = Solution()
        print(ob.sum(N, M))

# } Driver Code Ends
