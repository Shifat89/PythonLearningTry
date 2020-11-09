#def cnt_substring(string, sub_string):
    #length=len(string)
    #count=0
    #for i in range(0,length):
        #flag=0
        #if(string[i]==sub_string[0]):
            #for j in range(1,len(sub_string)):
               # if(string[i+j]!= sub_string[j]):
                    #break
               # else:
                    #flag=1
            #if(flag==1):
              #  count=count+1
   # return count

def count_substring(string, sub_string):
    countFunc= 0
    for i in range(0,len(string)):
        if string[i:].startswith(sub_string):
            countFunc=countFunc+1
    return countFunc


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)