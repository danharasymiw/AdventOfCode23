def is_num(some_chars):
    if some_chars[0].isnumeric():
        return int(some_chars[0])
    
    nums_map = {"one": 1,
                "two": 2,
                "three": 3,
                "four": 4,
                "five": 5,
                "six": 6,
                "seven": 7,
                "eight": 8,
                "nine": 9}
    
    for k, v in nums_map.items():
        if some_chars[0: len(k)] == k:
            return v
    return 0


def __main__():
    sum = 0
    with open('input.txt') as f:
        for line in f:
            nums = []
            for i in range(len(line)):
                if num := is_num(line[i:]):
                    nums.append(num)
                    
            sum += nums[0] * 10 + nums[len(nums) - 1]
            
    print(sum)

__main__()