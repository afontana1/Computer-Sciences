string = "AABBBCBCCCBBKLLLXPWWWPPXX"

string2 = "ACCCBBAC"


def candyy(string):
    def candy(string):
        """check for sequences of 3"""
        for i in range(len(string) - 2):
            if len(set(string[i : i + 3])) == 1:
                new = string.replace(string[i : i + 3], "")
                return new
        return False

    check = string
    while True:
        if candy(check):
            check = candy(check)
        else:
            return check


def candy(x):
    if len(x) == 0:
        return x
    temp = x[0]
    diff = len(x) - len(x.lstrip(temp))
    if diff >= 3:
        return candy(x.lstrip(temp))
    if diff < 3:
        return temp + candy(x[1:])


def candy_stevens(x):
    temp = ""
    i = 0
    while i < len(x):
        remainder = x[i:]
        firstletter = remainder[0]
        repeats = len(remainder) - len(remainder.lstrip(firstletter))
        print(i, repeats, firstletter)
        if repeats < 3:
            temp += firstletter
            i += 1
        else:
            i += repeats
    return temp


def left_strip_func(arr, condition):
    i = 0
    while arr[i] == condition:
        i += 1
    return {"remaining": arr[i:], "lettersRemoved": arr[:i]}


def check_for_sequence(sequence):
    j = 0
    # seqs = []
    for char in sequence:
        out = []
        i = j
        if i == len(sequence):
            break
        while sequence[i] == char:
            out.append(sequence[i])
            i += 1
            if i == len(sequence):
                break
        j = i
        # if out:
        # 	seqs.append((out[0],len(out)))
        if len(out) >= 3:
            return out
    return False


idk = "hhhiihhhhiEEEEaaaaaaaaaaaaaaHH"
seq = "aabccddd"


def crush(thatCandy):
    check = thatCandy[:]
    while True:
        seq = check_for_sequence(check)
        if seq:
            check = "".join([x for x in check if x not in seq])
        else:
            return check


print(crush(idk))


def remove_from_unsorted(arr):
    """while preserving order"""
    checked = []
    for i in arr:
        if i not in checked:
            checked.append(i)
    return checked


if __name__ == "__main__":
    import random

    # print("".join([random.choice('abcdefghijklmnopqrstuvwxyz').upper() for i in range(100)]))
    nums = [random.randrange(0, 20, 1) for i in range(1, 200)]
    for i in range(0, len(nums), 20):
        print(remove_from_unsorted(nums[i : i + 20]))
