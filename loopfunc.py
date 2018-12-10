import sys
print(sys.version)

# Function that makes a for loop
def sm_functionalized_forloop(x,y,z):

    beginValue = x  # the value the for loop starts on
    endValue   = y  # the value the for loop ends before
    str_state  = z  # if used, prints a string with the loop

    for index in range(beginValue,endValue): # prints all the way from the first value to the last. Excludes the last value itself!!!
        if z != 0:
            print (str_state, index)


sm_functionalized_forloop(0,4, "hello :")
