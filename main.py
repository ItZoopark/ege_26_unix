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
week_time = 7 * 24 * 60 * 60
start_week = 1634515200
# start_time = 1633046400
res = [list(map(int, item.split(' '))) for item in data]
# test_range = [[2, 5], [5, 6], [1, 2], [3, 6]]
# res = [[1634515199, 1635120001], [1634515198, 1635110000], [1634515210, 1635115000], [1634515100, 1634515150],
#        [1635120010, 1635120050], [1635110000, 1635130000]]
# merge_time(test_range)
# print(test_range)
time_process = [0] * week_time
end_week = start_week + week_time
ends = [0] * week_time
error = False
for pos, item in enumerate(res):
    try:
        print(pos)
        a, b = item[0], item[1]
        # b = week_time if b == 0 or b > end_week else b
        if b == 0:
            b = week_time
        elif b > start_week:
            if b > end_week:
                b = week_time
            else:
                b -= start_week
        else:
            b = -1

        # a = 0 if a == 0 or a < start_week else a - start_week
        if a < start_week:
            a = 0
        else:
            if a > end_week:
                b = -1
            else:
                a -= start_week

        if b - a >= 0:
            if ends[a] == 1:
                ends[a] = 0
                if b == week_time:
                    b -= 1
                ends[b] = 1
                a += 1
            elif ends[a] == 0:
                if b == week_time:
                    b -= 1
                ends[b] = 1
            for i in range(a, b):
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
