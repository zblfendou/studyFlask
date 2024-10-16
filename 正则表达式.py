import re

text = 'hello world 我们都是中国人 ,1235!!!@3#'
pattern = r'[\u4e00-\u9fa5a-zA-Z0-9]+'
result = re.findall(pattern, text)
print(result)
print('------替换中文-----')
sub = re.sub(pattern, '替换', text)
print(sub)

print('------判断字符串是否全部为中文-----')


def is_all_chinese(text):
    pattern = r'^[\u4e00-\u9fa5]+$'
    return re.match(pattern, text) is not None


text1 = '你好'
text2 = '你好中国a'
print(is_all_chinese(text1))
print(is_all_chinese(text2))
