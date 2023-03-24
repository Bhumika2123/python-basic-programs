import functools
factorial =[5,4,3,2,1]
result= functools.reduce(lambda x, y : x*y, factorial)
print(f"factorialof 5 is {result}")

"""working ==> 5*4
              4*3
              3*2
              2*1"""