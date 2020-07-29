global arr,casearray,x,con_1,con_2,largest,smallest
con_1=False
con_2=False
tot_case = int(input("Kitne Cases: "))
arr=[]
casearray=[]
for x in range(tot_case):
    tot_days = int(input("Enter Number Of Days: "))

    for y in range(tot_days):
        data=int(input())
        arr.append(data)
    
    if len(arr)<=1:
        casearray.append(data)
        string= "Case {} : {} Record Breaks".format(x+1,len(casearray))
        print(string)
        break
    
    elif len(arr)>=2:
        if arr[0] > arr[1]:
            casearray.append(arr[0])
            con_1=True
        
        #First_Largest occurance in the Middle of index 0(min) and index (max) of arr[]
        for i in range(len(arr)-2):
            if arr[i] < arr[i+1] and arr[i+1] > arr[i+2]:
                if con_1==True:
                    if casearray[0] == arr[i+1]:
                        break
                    else:    
                        casearray.append(arr[i+1])
                        con_2=True
                        break
                else:    
                    casearray.append(arr[i+1])
                    con_2=True
                    break

        print(con_1)
        print(con_2)

        #Now in accordance to con_1 and con_2 we will check The Largest as well as Last Largest in arr[]
        largest=max(arr)
        smallest=min(arr)
        if con_1==True and con_2==True:
            if largest > casearray[0] and largest > casearray[-1]:
                casearray.append(largest)
            else:
                pass

        elif con_1==True and con_2==False:
            if largest > casearray[0]:
                casearray.append(largest)
            else:
                pass
        
        elif con_1==False and con_2==True:
            if largest > casearray[-1]:
                casearray.append(largest)
            else:
                pass
        
        elif con_1==False and con_2==False:
            if largest==smallest:
                pass
            elif largest==arr[-1]:
                casearray.append(largest)
    print(casearray)
    string= "Case {} : {} Record Breaks".format(x+1,len(casearray))
    print(string)
    arr.clear()
    con_1=False
    con_2=False
    casearray.clear()

    

            

