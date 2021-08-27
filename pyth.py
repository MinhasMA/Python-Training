#def return_sum(c,y):
 #   return c+y
#r = return_sum(8,450)
#print(r)

def averageOfList(num):
    sumOfNumbers = 0
    for t in num:
        sumOfNumbers = sumOfNumbers + t
    avg = sumOfNumbers / len(num)
    return avg


x = [3,4,5,2,3,2,333,2,5,6,4]

y = averageOfList(x)
print(y)

#print("The average of List is", averageOfList([19, 21, 46, 11, 18]))

#def avg(x,y):
 #   return (x+y) / 2
#er = avg(45,44)
#print(er)
