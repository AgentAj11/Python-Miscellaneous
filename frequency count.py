def freq_count(nums):
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return freq


def main():
    nums = input("Enter number : ").rstrip().split(' ')
    print(nums)
    # print("Nums : ")
    freq = freq_count(nums)

    for key in freq:
        print(key, freq[key])


main()
