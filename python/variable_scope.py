x_global = 'global variable'

def training():
    t1 = 'transport'
    t2 = 'medicine'
    print(x_global)
    print(t1, t2)
    
training()
print(x_global)

#global variables are defined outside of a function and can be used both within and outside of a function
#local variables on the contrary are defined inside of a function and can only be used within that function

m = min([43, 10, 55, 29, 9])
print(m)

k = [43, 10, 55, 29, 9]
print(max(k))

#built-in functions are those that come with python and can be used by the developer by importing it.
#built-in functions can be used as either global or local variables.

def outer():
    rb = 'original function'
    def inner():
        nb = 'nested function'
        print(nb)
    inner()
    print(rb)
outer()

#The encloing scope allows for a function to be nested within a function. so there is a main function within which other functions work.
