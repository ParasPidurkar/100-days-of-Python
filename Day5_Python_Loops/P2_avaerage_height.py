height =[156,178,167,171.5,187]
x= len(height)
print(x);
sum =0;
count =0 
# for y in height:
#     count +=1
# for iter in range(0 ,count):
#     print(height[iter])
#     sum+= height[iter]
# average = sum/x
# print("Ther average is "+str(average))

for y in height:
    sum +=y
average = round(sum/x)   #rounding off a value in python
print("Ther average is "+str(average))