def tinkerTailor(ls, skip):
    skip -= 1  
    idx = skip
    while len(ls) > 1:
        # print(skip)
        ls.pop(idx)  # delete num on idx
        idx = (idx + skip) % len(ls)
    print('the last number: ', ls[0])

def main():
	n = 5    # the size of the array
	k = 3  # index of number to delete
	numbers = list(range(1, n+1))
	tinkerTailor(numbers, k)

if __name__ == "__main_":
	main()
