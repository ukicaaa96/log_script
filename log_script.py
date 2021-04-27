arrayOfFileNames = []
arrayOfFiles = []
arrayOfErrors = []
with open('log-example.txt') as f:
    #read log file
    lines = f.readlines()
    cnt = 0
    allUndefined = 0
    
    for i in lines:
        
        cnt+=1
        a = i.split()
        #check if error contains "Undefined" 
        if(("Undefined" in a) and (a[16].split("/")[-1]+a[14] not in arrayOfFiles)):
            allUndefined += 1
            arrayOfFiles.append(a[16].split("/")[-1]+a[14])
            tempArr = []

            file = a[16].split("/")[-1]
            error = "Error: " +a[12] + " " +a[13] + " " + a[14]
            line = "Line: "+a[19].replace(",", "")

            tempArr.append(file)
            tempArr.append(error)
            tempArr.append(line)

            arrayOfErrors.append(tempArr)
            if(a[16].split("/")[-1] not in arrayOfFileNames):
                arrayOfFileNames.append(file)
            
    for file in arrayOfFileNames:
        
        print(file)
        #print all error sorted by filename
        for errors in arrayOfErrors:
            if(errors[0] == file):
                print("-"+errors[1] + " || " + errors[2])
        
        print("")


print("Counted all Undefinded variable: " + str(allUndefined))



            


            
