

def compare(filename1, filename2):
	file1 = open(filename1, "r").readlines()
	file2 = open(filename2, "r").readlines()

	return file1 == file2

if __name__ == '__main__':
	print(compare("output.txt", "output 1.txt"))