height =[156,178,167,171.5,187]
highest_height=0
for iter in height:
    if iter > highest_height:
        highest_height = iter
        

print("The Highest height among the list is :"+str(highest_height))
print(f"The highest height is: {highest_height}")  #f string can be only used in py 3
