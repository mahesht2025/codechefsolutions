# Julius Caesar was warned by a soothsayer to be wary of the ides of March
# — namely, the 15-th of March.
# Today is the N-th day of March. Your task is to tell Caesar whether it is the 
# ides of March, so that he can take extra safety precautions if necessary.
def idea_of_march(n):
    if n == 15:
        return "Yes"
    else:
        return "No"    
n = int(input("enter number :"))
res = idea_of_march(n)
print(res)