"""
给定一个字符串，找出字符串中的最长回文子串
"""

def longpalindrome(string):
    #字符串等于反转后的字符串，则直接输出
    if len(string) <= 1 or string == string[::-1]:
        return string

    max_len = 1
    res_str = string[0]

    #从第二个字符串开始做判断
    for i in range(1,len(string)):

        if max_len > len(string[i + 1::]):
            break
        #从第i+max_len个字符开始判断
        for j in range(i + max_len,len(string)):
            if string[i:j+1] == string[i:j+1][::-1] and j-i+1 > max_len:
                max_len = j - i + 1
                res_str = string[i:j+1]

    return res_str,max_len

string = 'cabasd'
print(longpalindrome(string))






