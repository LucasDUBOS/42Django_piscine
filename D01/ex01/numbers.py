def print_nbr_script(file):
    nbr_file = open(file, "r")
    content_file = nbr_file.read()
    print(content_file.replace(",", "\n"))
    nbr_file.close()

if __name__ == '__main__':
    print_nbr_script("numbers.txt")