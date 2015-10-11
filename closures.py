'''given N mobile numbers. Sort them in ascending order after which print them in standard format.
+91 xxxxx xxxxx
sample input :
3
07895462130
919875641230
9195969878

Sample Output:
+91 78954 62130
+91 91959 69878
+91 98756 41230'''


iters = int(input())
phone=[]
for i in range(0,iters):
    l=input()
    phone.append(l)

def wrapper(func):
    def inner(args):
        digits=len(args)
        if digits == 13:
            return(func(args[3:]))
        elif digits == 12:
            return(func(args[2:]))
        elif digits == 11:
            return(func(args[1:]))
        else:
            return(func(args))
    return(inner)

@wrapper
def std_mobile(number):
    return ('+91 '+number)

std_nums = []
for val in phone:
    std_nums.append(std_mobile(val))
    
std_nums.sort()
for val in std_nums:
    print(val[:9]+' '+val[9:])
