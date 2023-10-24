
# try:
#     num = int(input('Int: '))
#     print(f'num = {num}')
# except ValueError:
#     print('Feeeeeeel')


# from modules import square

# print(square(9))

def is_palindrome(n):
    return str(n) == str(n)[::-1]
    

num = 0
look = []
for y in range(10, 100):
    for x in range(10, 100):
        num = y * x
        num = str(num)
        if is_palindrome(num):
            look.append(num)

        
print(look[-1])