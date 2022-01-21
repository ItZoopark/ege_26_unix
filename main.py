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


def unix_time1(file_name, start):
    data = open("26.txt").read().splitlines()[1:]
    week_time = 7 * 24 * 60 * 60 + 1  # 604800
    start_week = start
    time_process = [0] * week_time  # 0...604799
    end_week = start_week + week_time
    ends = [0] * week_time  # 0...604799
    error = False
    # start_time = 1633046400
    res = [list(map(int, item.split(' '))) for item in data]
    # test_range = [[2, 5], [5, 6], [1, 2], [3, 6]]
    # res = [[start_week - 10, start_week + 10], [start_week - 10, start_week - 9], [start_week - 10, end_week + 10],
    #        [start_week + 10, start_week + 20], [start_week + 20, start_week + 30],
    #        [end_week - 10, end_week + 10], [start_week + 10, end_week + 10]]

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
                    ends[b] = 1
                    a += 1
                elif ends[a] == 0:
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


def unix_time2(file_name, start, period):
    data = open(file_name).read().splitlines()[1:]
    week = period + 1  # 604801
    start_week = start
    proc = [0] * (week + 1)  # 0...604800
    ends = [0] * (week + 1)
    starts = [0] * (week + 1)

    data = [list(map(int, item.split(' '))) for item in data]

    for a, b in data:
        if a > start_week + week or (b < start_week and b != 0):
            continue

        if a < start_week or a == 0:
            a = start_week

        if b == 0 or b >= start_week + week:
            b = start_week + week

        starts[a - start_week] += 1
        ends[b - start_week] += 1

    proc[0] = starts[0] - ends[0]  # 100 - 10 = 90

    for i in range(1, week + 1):
        proc[i] = proc[i - 1] + (starts[i] - ends[i])  # 90 + 10 - 2 = 98

    mx = max(proc)
    print(mx, proc.count(mx))


# unix_time2("26.txt", 1634515200, 7 * 24 * 60 * 60)
# unix_time2("40742.txt", 1633305600, 7 * 24 * 60 * 60)
# unix_time1("40742.txt", 1633305600, 7 * 24 * 60 * 60)
unix_time2("26_4741.txt", 1236147000, 24 * 60 * 60)
