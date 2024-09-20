st= [2,32,43,5,5,24,2,1,20,4,5,45,6,67,87,76,5,6,5,3,34,3,43,32,3,554,23,7,87,78,78,90]
print(f'List of Input: {st}\n')
print(f'Size of String: {len(st)}\n')
str=[]
print('Even Numbers are: ', end = ' ')
i=0

#  with while loop without  duplicates
while(i< len(st)):
    
    if(st[i]%2 == 0):
        if not(st[i] in str):
            print(st[i], end=" ")
            str.append(st[i])
    i+=1
    
    
    
#  with for loop without removing duplicates
# for i in st:    
    # if i % 2 == 0:
    #     print(i, end= " ")
        
    #     str.append(i)

print("\n")
print(f'Lenght of only even numbers String: {len(str)}\n')
print(f'New even string: {str}\n')