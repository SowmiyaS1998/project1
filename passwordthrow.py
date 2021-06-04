# project1
import random as r
#generating simple password
a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','v','u','w','x','y','z','1','2','3','4','5','6','7','8','9','10','!','@','#','$','%','^','&','*','(',')']
b=(r.sample(a,5))
print(b)
print(*b,sep="")
