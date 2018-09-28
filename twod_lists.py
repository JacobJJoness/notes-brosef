a = [[1,2,3],
     [4,5,6]]
def print_2d_list(lst):
    for i in range(len(lst)):
        for j in range (len(lst[i])):
            print(lst[i][j], end=' ')
            print()


#for row in a:
#    for element in row:
#        print(element,end= ' ')
#        print()

# add all elements in a list

#sum = 0
#for i in range(len(a)):
#    for j in range(len(a[i])):
#        sum+= a[i][j]
#        
#print(sum)
#sum = 0
#for row in a:
#    for element in row:
#        sum += element
#        
#print(sum)

#for i in range(len(a)):
#    for j in range(len(a[i])):
#        a[i][j]
#creating a 2d list
#x = [[0]*5]*8 doesnt work

x =[[0]*5 for i in range (800)]
x[0][0] = 100
print(x)
