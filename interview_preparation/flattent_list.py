a = [1, [2, 3, [2, 4]], 1, 5]

res = []
def flatten_list(a):
    for i in a:
        if type(i) == list:
            flatten_list(i)
        else:
            res.append(i)
flatten_list(a)
print(res)