import array

int_array = array.array('i',[0,1,2,3,1,2])
int_array[0] = -1
int_array[1] = -2
print(int_array)

try:
    int_array[10]= -10
except IndexError as ie:
    print(ie)