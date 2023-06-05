import sys

def compare_files(file1, file2):
    with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
        if f1.read() == f2.read():
            return True
        return False

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python compare_files.py <file1> <file2>")
        sys.exit(1)

    file1 = sys.argv[1]
    file2 = sys.argv[2]

    if compare_files(file1, file2):
        print("The files are identical.")
    else:
        print("The files are not identical.")
