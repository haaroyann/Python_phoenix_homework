# #Xndir N1

# def foo(n):

#     if n==1:
#         return False
#     if n<=0:
#         return False
    
#     for i in range (2,int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True
# def prime_list(n):
#     ls=[]
#     for i in range(2,n):
#         if foo(i):  #es toxy chem haskanum
#             ls.append(i)
#     return ls
# print(prime_list(55))

# #Xndir N3  !!chem grel es xndiry!!
# ls=[]
# for i in range(1,7,2):  
#     for j in range(3):
#         ls.append(i)
# print(ls)        


# #Xndir N4
# fib=lambda n: 1 if n<=0 else fib(n-1)+(n-2)
# print(fib(55))


# #Xndir N5 !!xndiry grel em hndiki ognutyamb, returni pahy chem haskanum!!
# def Sum_of_digits(n):
#     if n==0:
#         return 0  #inchi a vor grum em "mutqagreq drakan tiv", error a talis
#     else:
#         mnacord = n%10
#         tiv = n//10
#         # print(mnacord, tiv)
#         return mnacord+Sum_of_digits(tiv)  
# print(Sum_of_digits(5555555))

# #Xndir N6 !!vochmiban chem haskanum!!
# a="bari yereko sireliss"
# def foo(a):
#     count={}
#     for char in a:
#         if count.get(char): #Get ov hasaneliutyun enq stanum "char" key-in?
#             count[char]+=1
#         else:
#             count[char]=1    
#     return(count)            
# print(foo(a))      



