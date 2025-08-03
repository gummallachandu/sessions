# highest occurance 
stack = [1,1,3,3,3,4,4,4,4,4,4]
def highestoccurance(arr):
    major_len = len(arr)/2
    for i in range(len(arr)):
        counter = 1
        print(arr[i])
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                counter += 1
            print(f"{arr[j]} --- {counter}")
        if counter > major_len:
            return print("here is the ans ",arr[i])

print(highestoccurance(stack))

def highestoccurance2(arr):
    major_len = len(arr)//2
    print(major_len)
    badsi = {}
    divya_bucket = set()
    for i in arr:
        if i in divya_bucket:
            badsi[i] += 1
        else:
            badsi[i] = 1
            divya_bucket.add(i)

    print(divya_bucket)
    print(badsi)
    res = []
    for k, v in badsi.items():
        if v > major_len:
            res.append(k)
    return res

print(highestoccurance2(stack))
