arr=[]
dummy_arr=[]
count=0
string= "Case {} : {} Record Breaks"
tot_case=int(input("Enter Number of Cases: "))

for x in range(tot_case):
    days= int(input("Enter Number of Days: "))

    for y in range(days):
        data=int(input())
        arr.append(data)

    if len(arr) == 1:
        count +=1
        
    elif len(arr) >= 2:
        if arr[0] > arr[1]:
            count +=1
        
        for i in range(len(arr)-2):
            dummy_arr.append(arr[i])
            if arr[i] < arr[i+1] and arr[i+1] > arr[i+2]:
                if arr[i+1] <= max(arr) and arr[i+1] > max(dummy_arr):
                    if arr.index(arr[i+1]) < arr.index(max(arr)):
                        count +=1
        dummy_arr.clear()
        if arr.index(max(arr))==arr.index(arr[-1]):
            if max(arr) != min(arr):
                count +=1

    print(string.format(x+1,count))
    arr.clear()
    count=0
