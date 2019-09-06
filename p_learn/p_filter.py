def is_palindrome(n):
    # 将字符串反转后和原字符串进行比较,相同时返回
    #print(str(n))
    #print(str(n)[::-1])
    return str(n) == str(n)[::-1]
#[::1]中省略起止位置，步进为-1
#python中步进为正，从左往右取，步进为负，从右往左取
#str(n)[::-1]实现字符串翻转

output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
print(is_palindrome(1234))
line = "abcdeghigk"
print(line[::-1])
print(line[2:4])
print(line[2::4])
print(line[6::-1])
L = list(filter(lambda n:n%2 == 1,range(1,20)))
print(L)