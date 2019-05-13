# python3
def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    if n == 2:
        index_1, index_2 = 0, 1
    else:
        index_1 = 0
        for i in range(1, n):
            if(numbers[index_1] < numbers[i]):
                index_1 = i

        index_2 = 0
        for i in range(1, n):
            if(i != index_1):
                if(numbers[index_2] < numbers[i]):
                    index_2 = i

    max_product = numbers[index_1] * numbers[index_2]


    return max_product


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))

