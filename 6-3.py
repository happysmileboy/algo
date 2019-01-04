import sys


# def cur(pair_ls, check_ls, check, num):
#     print('pair:{}'.format(pair_ls))
#     print(check_ls)
#     if check in check_ls:
#         cur(pair_ls, check_ls, check+1, num)
#     else:
#         if check in pair_ls:
#             position = pair_ls.index(check)
#             if position % 2 == 0 and pair_ls[position+1] != 0:
#                 check_ls.append(pair_ls[position])
#                 check_ls.append(pair_ls[position+1])
#                 pair_ls = [0 if x == pair_ls[position] else x for x in pair_ls]
#                 pair_ls = [0 if x == pair_ls[position+1] else x for x in pair_ls]
#             elif position % 2 == 1 and pair_ls[position-1] != 0:
#                 check_ls.append(pair_ls[position])
#                 check_ls.append(pair_ls[position-1])
#                 pair_ls = [0 if x == pair_ls[position] else x for x in pair_ls]
#                 pair_ls = [0 if x == pair_ls[position - 1] else x for x in pair_ls]
#             pair_ls[position] = 0
#             cur(pair_ls, check_ls, check, num)
#         else:
#             return 0
#     if len(check_ls) == num:
#         return 1
#
#     return cur(pair_ls, check_ls, check+1, num)

# def cur(pair_ls, rest_ls, check_ls, num, p, check_cur):
#     if pair_ls == []:
#         print(p)
#         return
#     if pair_ls[0] not in check_ls and pair_ls[1] not in check_ls:
#         cur(pair_ls[2:], pair_ls[2:], check_ls, num, p, check_cur)
#         check_ls.append(pair_ls[0])
#         check_ls.append(pair_ls[1])
#     else:
#         if rest_ls != []:
#             first = rest_ls[0]
#             second = rest_ls[1]
#             if len(check_ls) == num:
#                 cur(pair_ls[2:], pair_ls[2:], [], num, p + 1, 0)
#             elif first in check_ls or second in check_ls:
#                 if len(rest_ls) / 2 >= check_cur:
#                     cur(pair_ls, rest_ls[2:] + rest_ls[:2], check_ls, num, p, check_cur+1)
#                 else:
#                     cur(pair_ls[2:], pair_ls[2:], [], num, p, 0)
#             else:
#                 check_ls.append(first)
#                 check_ls.append(second)
#                 cur(pair_ls, rest_ls[2:], check_ls, num, p, 0)
#         else:
#             if len(check_ls) == num:
#                 cur(pair_ls[2:], pair_ls[2:], [], num, p + 1, 0)
#             else:
#                 cur(pair_ls[2:], pair_ls[2:], [], num, p, 0)


def cur(arefriend, taken, num):
    check = num
    for i in range(num):
        if taken[i] == 0:
            check = i
            break

    if check == num:
        return 1

    pair = check + 1
    ret = 0
    while pair < num:
        if arefriend[check][pair] == 1 and taken[pair] == 0:
            taken[check] = taken[pair] = 1
            ret += cur(arefriend, taken, num)
            taken[check] = taken[pair] = 0
        pair += 1

    return ret


game_n = int(input())

for _ in range(game_n):
    ls = list(map(int, input().split()))
    num = ls[0]
    arefriend = [[-1 for _ in range(num)] for _ in range(num)]
    pair_ls = list(map(int, input().split()))
    for n in range(ls[1]):
        if pair_ls[2*n] < pair_ls[2*n+1]:
            arefriend[pair_ls[2*n]][pair_ls[2*n+1]] = 1
        else:
            arefriend[pair_ls[2*n+1]][pair_ls[2*n]] = 1
    taken = [0 for _ in range(num)]
    print(cur(arefriend, taken, num))


