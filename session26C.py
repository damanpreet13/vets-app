#Decorator
# 1.create a function, which takes function as input.
# 2.create an inner function which should have same signature of the target function.
# 3.execute the passed function from the inner function.
# 4.return inner function from outer function.
# 5.t0 decorate any function use @function.
def compute_taxes(func):
    def inner(amount, taxes):
        if amount >0 and amount<=10000:
            taxes = 0.18 #update taxes
        elif amount > 10000:
            taxes = 0.25 # update taxes
        else:
            print("Invalid Amount")
        return func(amount, taxes)
    return inner
@compute_taxes
def pay(amount, taxes):
    return amount + (amount*taxes)


amount_to_pay = pay(50000, 0)
print("amount_to_pay:", amount_to_pay)