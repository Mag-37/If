x = 35
print('hello')
if x < 0:
    print('less than zero')
print('goodbye')
# examples
a, b = 18, 21
if a < b:
    print('b > a')
if a + b < 40 and a + b > 0:
    print('success')
if (a < b) and (a < 25 or b > 25):
    print('success')
ace, king = 11, 10
if (ace + king) == 21:
    print('win')
# comparative data
if '25' > '231':
    print('OK')
if '251' > '25':
    print('OK')
if [3, 1] < [2, 2]:
    print('OK')
if [3, 1] >= [2, 2]:
    print('OK')
a = 21
if 21 <= a > 20:
    print('WIN')
if a != 22:
    print('WIN')
# no comparison: diff data type
# if 3 > '1':
#     print("OK")
# if [1, 3] < '3':
#     print('OK')
