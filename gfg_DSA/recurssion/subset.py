def find_subsets(arr,subset,i):
    if(i == len(arr)):
        for i in subset:
            print(i,end=" ")
        print()
        return
    
    subset.append(arr[i])
    find_subsets(arr,subset,i+1)
    
    subset.pop()
    find_subsets(arr,subset,i+1)

def main():
    arr = [1,2,3]
    i = 0
    subset = []
    find_subsets(arr,subset,i)
if __name__ == "__main__":
    main()