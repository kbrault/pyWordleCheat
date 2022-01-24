def main():
    num_lines = sum(1 for _ in open('words.txt'))
    print(num_lines)

if __name__ == '__main__':
    main()