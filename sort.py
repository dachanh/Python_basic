
a = [ [['nông thôn'], [1,2,4,4]], [['doang nghiuep'], [1,1,2,2]] ,[['doang nghiuep'], [0,1,2,2]] ]
# def custom(a,b):
#     if a[0] < b[0]:
#         return a
#     if a[0] == b[0] and a[1] < b[1]:
#         return a 
#     return b
def custom(x):
    return x[1][0],x[1][1]
a = sorted(a,key=custom)
print(a)