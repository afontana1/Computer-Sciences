'''
Objective -> Write a function that takes in calendar availability and outputs non overlapping times
sample input:
Two items representing a persons calendar availability
-> a list of lists containing unavailable times
-> a time slot representing the duration of availability (ie, no meetings before or after the bounds)

Person1:
[["9:00","10:30"],["12:00","13:00"],["16:00","18:00"]]
["9:00","20:00"]

Person2:
[["10:00","11:30"],["12:30","14:30"],["14:30","15:00"],["16:00","17:00"]]
["10:00","18:30"]

sample output: [["11:30","12:00"],["15:00","16:00"],["18:00","18:30"]]

assume you cant have meetings less than 30 minutes, 
ie: the inputs all are in at least 30 min intervals
'''

def construct_interval(interval):
    unavailable = []
    start = interval[-1]
    last = start
    unavailable.append(interval[-1])
    while last != interval[0]:
        check = last.split(":")
        if check[-1] == "00":
            hour = int(check[0]) - 1
            last = str(hour) + ":30"
            unavailable.append(last)
        else:
            last = check[0] + ":00"
            unavailable.append(last)
    return unavailable


def feasible_availability(availability1, availability2):
    """Determine range of time in which both parties are available
    if one time range is strictly a subset of another, that will be the time range
    """
    start = (
        availability1[0] if availability1[0] < availability2[0] else availability2[0]
    )
    end = availability1[1] if availability1[1] < availability2[1] else availability2[1]
    return [start, end]


def available_interval(schedule):
    """return times where person is available"""
    possible_times = construct_interval(feasible_availability(**available))
    available_times = []
    out = []
    for block in schedule:
        block_n = construct_interval(block)
        available_times += block_n
    for times in possible_times:
        if times not in available_times:
            continue
        out.append(times)
    return out


def convert_to_map(lstoftimes):
    out = {}
    for time in lstoftimes:
        if time[:2] not in out:
            out[time[:2]] = []
        out[time[:2]].append(time)
    return out


def get_acceptable_times(available):
    availability = construct_interval(feasible_availability(**available))
    availability_mapped = convert_to_map(availability)
    return availability


def filter_bad_times(acceptable_times, *args):
    cannotExceed, tooSmall = (
        acceptable_times[0].split(":")[0],
        acceptable_times[1].split(":")[1],
    )
    final = []
    for arg in args:
        for mat in arg:
            temp = []
            for sublst in mat:
                interval = construct_interval(sublst)
                vals = [interval[i].split(":")[0] for i in range(len(interval))]
                removeVals = [
                    idx
                    for idx, i in enumerate(vals)
                    if (i > cannotExceed or i < tooSmall)
                ]
                leftoverindex = [i for i in range(len(interval)) if i not in removeVals]
                leftovervalues = [interval[i] for i in leftoverindex]
                temp += leftovervalues
            final += temp
    if max(final) < acceptable_times[0]:
        final.append(acceptable_times[0])
    return final

'''
first attempt above didnt work, trying second
'''
def merge_schedules(*args):
    """merge in increasing order based on the first element"""
    merged = []
    for arg in args:
        for lst in arg:
            for l in lst:
                merged.append(l)
    return merged


def sort_schedules(*args):
    merged = merge_schedules(*args)
    for i in range(len(merged) - 1):
        temp1 = merged[i][0].split(":")[0] + merged[i][0].split(":")[1]
        comparison_value1 = int(temp1)
        for j in range(i + 1):
            temp2 = merged[j][0].split(":")[0] + merged[j][0].split(":")[1]
            comparison_value2 = int(temp2)
            if comparison_value2 > comparison_value1:
                merged[i], merged[j] = merged[j], merged[i]
    return merged


def insert_feasible_block_range(lstoflsts):
    """insert additional block if necessary"""
    feasible_range = feasible_availability(**available)
    min_block, max_block = "", ""
    if int(lstoflsts[0][0].split(":")[0]) < int(feasible_range[0].split(":")[0]):
        min_block = None
    else:
        min_block = [lstoflsts[0][0], feasible_range[0]]

    tempmax = 0
    lastposition = None
    for idx, lst in enumerate(lstoflsts):
        check = int(lst[-1].split(":")[0])
        if check > tempmax:
            tempmax = check
            lastposition = idx
    if int(lstoflsts[lastposition][-1].split(":")[0]) > int(
        feasible_range[1].split(":")[0]
    ):
        max_block = None
    else:
        max_block = [lstoflsts[lastposition][-1], feasible_range[1]]
    if min_block:
        lstoflsts.insert(min_block, 0)
    if max_block:
        lstoflsts.append(max_block)
    return lstoflsts


def convert_to_digit(s):
    s_as_digit = []
    for lst in s:
        temp = []
        for element in lst:
            els = element.split(":")
            el = int(els[0] + els[1])
            temp.append(el)
        s_as_digit.append(temp)
    return sorted(s_as_digit, key=lambda x: (x[0], x[1]))


def determine_schedule(*args):
    """get schedules"""
    schedules = sort_schedules(*args)
    check = insert_feasible_block_range(schedules)
    as_digits = convert_to_digit(check)
    give = []
    for i in range(len(as_digits) - 1):
        first = as_digits[i][-1]
        second = as_digits[i + 1][0]
        if first < second:
            give.append((first, second))
    # insert whatever was put in the feasible block
    return give + check[-1]

if __name__ == "__main__":
	available = {
    "availability1":["9:00","20:00"],
    "availability2":["10:00","18:30"]
}

	p1 = [["9:00","10:30"],["12:00","13:00"],["16:00","18:00"]]
	p2 = [["10:00","11:30"],["12:30","14:30"],["14:30","15:00"],["16:00","17:00"]]

	# int1,int2 = available_interval(p1), available_interval(p2)
	# filtered_badbois = filter_bad_times(x,(p1,p2))
	# set(filtered_badbois)
	print(determine_schedule((p1,p2)))