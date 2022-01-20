def merge_time(data):
    for pos, item in enumerate(data):
        print(f"->{pos}")
        a1, b1 = item[0], item[1]
        for next_pos, next_item in enumerate(data):
            a2, b2 = next_item[0], next_item[1]
            if b1 == a2:
                del data[pos]
                del data[next_pos - 1]
                data.append([a1, b2])
            elif a1 == b2:
                del data[pos]
                del data[next_pos - 1]
                data.append([a2, b1])


data = open("26.txt").read().splitlines()[1:]
# print(data)
week_time = 7 * 24 * 60 * 60  # 604800
start_week = 1634515200
time_process = [0] * week_time  # 0...604799
end_week = start_week + week_time
ends = [0] * week_time  # 0...604799
error = False
# start_time = 1633046400
# res = [list(map(int, item.split(' '))) for item in data]
# test_range = [[2, 5], [5, 6], [1, 2], [3, 6]]
res = [[start_week - 10, start_week + 10], [start_week - 10, start_week - 9], [start_week - 10, end_week + 10],
       [start_week + 10, start_week + 20], [start_week + 20, start_week + 30],
       [end_week - 10, end_week + 10], [start_week + 10, end_week + 10]]

# [-10, 10] -> [0, 10]
# [-10, -9] ->
# [-10, 604800] -> [0, 604799]
# [10, 20] -> [10, 20]
# [604790, 604800] -> [604790, 604800]
# [10, 604800] -> [10, 604800]
#
# merge_time(test_range)
# print(test_range)

for pos, item in enumerate(res):
    try:
        print(pos)
        a, b = item[0], item[1]
        if b == 0:
            b = week_time - 1
        elif b > start_week:
            if b >= end_week:
                b = week_time - 1
            else:
                b -= start_week
        else:
            b = -1

        if a <= start_week:
            a = 0
        else:
            if a > end_week:
                b = -1
            elif a == end_week:
                a = end_week - 1
            else:
                a -= start_week

        if b - a >= 0:
            if ends[a] == 1:
                ends[a] = 0
                # if b == week_time:
                #     b -= 1
                ends[b] = 1
                a += 1
            elif ends[a] == 0:
                # if b == week_time:
                #     b -= 1
                ends[b] = 1
            for i in range(a, b + 1):
                time_process[i] += 1
    except Exception as ex:
        print(pos)
        print(ex)
        print(item)
        print(a, b)
        error = True
        break

if not error:
    max_time_process = max(time_process)
    max_time_process_count = time_process.count(max_time_process)
    print(max_time_process, max_time_process_count)
