# import line by line all numbers and lists
len_frst = int(input())
frst_lst = input().split()
len_scnd = int(input())
scnd_lst = input().split()
len_thrd = int(input())
thrd_lst = input().split()

# find similar value

similar_value = list(set(frst_lst) & set(scnd_lst) & set(thrd_lst))

print(len(similar_value))