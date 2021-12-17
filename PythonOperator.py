# Arthematic Operators    [  + ,  - ,  *,   /,   %,  **,  // ]
print(10 + 5)
print(10 - 5)
print(10 * 5)
print(10 / 5)
print(10 % 5)
print(10 ** 5)
print(12 // 5) 

# Assignment operator  [ = , += , -=, *=, /=, %=, //=, **=, &=, |=, ^=, >>=, <<= ]
b1= 10
print(b1)
b2 = 10
b2 +=10 # b2 = b2+10
print(b2)
b3 = 11
b3 -= 10 # b3 = b3-10
print(b3)
b4 = 12
b4 *= 10 # b4 = b4*10
print(b4)
b5 = 12
b5 /= 10 # b5 = b5/10
print(b5)
b6 = 12
b6 %= 10 # b6 = b6%10
print(b6)
b7 = 12
b7 //= 10 # b7 = b7//10
print(b7)
b8 = 12
b8 **= 10 # b8 = b8**10
print(b8)
b9 = 12
b9 &= 10 # b9 = b9&10
print(b9)
b10 = 12
b10 |= 10 # b10 = b10|10
print(b10)
b11 = 12
b11 ^= 10 # b11 = b11^10
print(b11)
b12 = 12
b12 ^= 10 # b12 = b12^10
print(b12)
b13 = 12
b13 >>= 10 # b13 = b13>>10
print(b13)
b14 = 12
b14 <<= 10 # b13 = b14<<10
print(b14)

## Comparision operators    [ ==, !=, >, <, >=, <= ]
if 10 == 5 :
    print("True")
else:
    print("False")

if 10 != 5 :
    print("True")
else:
    print("False")

if 10 > 5 :
    print("True")
else:
    print("False")

if 10 < 5 :
    print("True")
else:
    print("False")

if 10 <= 5 :
    print("True")
else:
    print("False")

if 10 >= 5 :
    print("True")
else:
    print("False")

# Logical operator  [ and, or , not ]

if 10 >= 5 and  10 > 5:
    print("True")
else:
    print("False")

if 10 >= 5 or 10 > 5:
    print("True")
else:
    print("False")

a = 10
if not a:
    print("True")
else:
    print("False")

# Identity operators  [ is, is not ]
a = ""
if a is None:
    print("True") 
else:
    print("False")

a1 = ""
if a1 is not  None:
    print("True") 
else:
    print("False")

# Membership operators [ in , not in ]
a = ["a", "b", "c"]
if "a" in a:
    print("True") 
else:
    print("False")

if "a" not in a:
    print("True") 
else:
    print("False")

# Bitwise operators (used to compare binary)  [ & ,  | ,  ^,  ~, <<, >> ]
a = 60            # 60 = 0011 1100 
b = 13            # 13 = 0000 1101 
c = 0

c = a & b;        # 12 = 0000 1100
print (c) 

c = a | b;        # 61 = 0011 1101 
print (c) 

c = a ^ b;        # 49 = 0011 0001
print (c) 

c = ~a;           # -61 = 1100 0011
print (c) 

c = a << 2;       # 240 = 1111 0000
print (c) 

c = a >> 2;       # 15 = 0000 1111
print (c) 