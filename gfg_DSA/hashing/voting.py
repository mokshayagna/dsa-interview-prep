n = 13
arr = ["john", "johnny", "jackie", "johnny", "john",
       "jackie", "jamie", "jamie", "john", "johnny",
       "jamie", "johnny", "john"]

my_dict = {}
l = []
max_vote = 0
ans = 0
for i in range(len(arr)):
    if arr[i] in my_dict:
        my_dict[arr[i]] += 1
    else:
        my_dict[arr[i]] = 1
        
    if my_dict[arr[i]] > max_vote:
        max_vote = my_dict[arr[i]]
        ans = arr[i]
    elif my_dict[arr[i]] == max_vote:
        if(arr[i] < ans):
            ans = arr[i]
print(ans,max_vote)