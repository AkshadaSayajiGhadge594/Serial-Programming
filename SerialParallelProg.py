print("----------Serial Parallel Programming-----------");

def square(n):
	return (n*n);

#input list:
arr=[1,2,3,4,5]

#empty list to store result:
result=[];

for num in arr:
	result.append(square(num));

print(result)
