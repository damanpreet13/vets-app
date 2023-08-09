#Nested Functions
# create function  inside the outer function
def outer():
    print("this is outer function")
    def inner():
        print("this is inner function")

        #inner()
    return inner
result = outer()
result()