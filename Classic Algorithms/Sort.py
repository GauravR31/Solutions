def bubble_sort(l):
	n = len(l)
	for i in range(n):
		for j in range(0, n-i-1):
			if l[j] > l[j+1]:
				l[j], l[j+1] = l[j+1], l[j]
	return l

def merge(arr, l, m, r):
	n1 = m - l + 1
	n2 = r - m

	L = [0] * n1
	R = [0] * n2

	for i in range(0, n1):
		L[i] = arr[l + i]
	for j in range(0, n2):
		R[j] = arr[m + 1 + j]

	i,j,k = 0,0,l

	while i < n1 and j < n2:
		if L[i] <= R[j]:
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = R[j]
			j += 1
		k += 1

	while i < n1:
		arr[k] = L[i]
		i += 1
		k += 1

	while j < n2:
		arr[k] = R[j]
		j += 1
		k += 1

def merge_sort(arr, l, r):
	if l < r:
		m = (l+r-1)/2
		
		merge_sort(arr, l, m)
		merge_sort(arr, m+1, r)
		merge(arr,l,m,r)

def main():
	input_list = []
	input_list = raw_input("Enter the numbers to be sorted ").split()
	input_list = [int(i) for i in input_list]
	n = len(input_list)
	
	print("1. Bubble Sort\n2. Merge Sort\n3. Exit")
	ch = input("Enter your choice ")

	while True:
		if ch == 1:
			print bubble_sort(input_list)
			break
		elif ch == 2:
			merge_sort(input_list, 0, n-1)
			print input_list
			break
		elif ch == 3:
			break
		else:
			print("Enter valid choice.")

if __name__ == '__main__':
	main()