'''Sam was recently gifted an array a of n integers. Sam being fond of mathematics decided to count the number of beautiful pairs in the array a.

A pair of integers (i, j) is considered beautiful if i < j and lcm(a[i], a[j]) = max(a[i], a[j]).

Sadly the array is too large and Sam wants to know the number of beautiful pairs quickly. Can you help him out?

We define lcm(x, y) as the smallest positive integer (greater than zero) that is divisible by both x and y. We can show that such integer always exists.

Input Format
The first line contains an integers n - The number of elements in a.
The second line contains n integers a[1], a[2], ..., a[n] - The elements of a.
Output Format
Print a single integer - The number of beautiful pairs.
Constraints
1 ≤ n ≤ 2 * 10^5.
1 ≤ a[i] ≤ 10^5.
Sample 0
Input
3
1 3 6
Output
3
Explanation
Beautiful pairs are:
(1, 2).
(1, 3).
(2, 3).
Sample 1
Input
2
2 3
Output
0
Explanation
The only possible pair is (1, 2), which is not a beautiful pair, so the answer is 0.'''



def lcm(a,b):
	for i in range(max(a,b),1+(a*b)):
		if i%a==i%b==0:
			lcm=i
			break
	return lcm

n=int(input())
count=0
a=list(map(int,input().split(' ')))
for i in range(n):
	for j in range(n):
		if j>i:
			if lcm(a[i],a[j])==max(a[i],a[j]):
				count+=1
print(count)