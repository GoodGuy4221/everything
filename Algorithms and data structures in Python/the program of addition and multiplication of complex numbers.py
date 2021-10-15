# 12 + 5i
# 1) a + b*i
# 2) c + d*i

# 1+2 - (a+c) + (b+d)*i
# 1*2 - (a*c - d*b) + (a*d + b*c) * i

# a_comp = complex(3, 5)
# b_comp = complex(2, 4)
#
# print(a_comp + b_comp)
# print(a_comp * b_comp)


# class MyCompNumb:
#
#     def __init__(self, real, image):
#         self.real = real
#         self.image = image
#
#     def __add__(self, other):
#         real = self.real + other.real
#         image = self.image + other.image
#         return MyCompNumb(real, image)
#
#     def __mul__(self, other):
#         real = self.real * other.real - self.image * other.image
#         image = self.real * other.image + self.image * other.real
#         return MyCompNumb(real, image)
#
#     def __repr__(self):
#         if self.image >= 0:
#             return f'{self.real} + {self.image}*i'
#         return f'{self.real} - {self.image}*i'
#
#
# number_a = MyCompNumb(3, 4)
# number_b = MyCompNumb(1, 2)
# print(number_a + number_b)
# print(number_a * number_b)


a_number = [3, 4]
b_number = [1, 2]

add_a = a_number[0] + b_number[0]
add_b = a_number[1] + b_number[1]
add_number = [add_a, add_b]

mul_a = a_number[0] * b_number[0] - a_number[1] * b_number[1]
mul_b = a_number[1] * b_number[0] + a_number[0] * b_number[1]
mul_number = [mul_a, mul_b]
print(add_number)
print(mul_number)
