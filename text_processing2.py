#######################
# Test Processing II  #
#######################


def digits_to_words(input_string):
    numbers = '0123456789'
    names = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    digit_string = ''
    for c in input_string:
        if c in numbers:
            digit_string += names[int(c)] + ' '
    digit_string = digit_string.strip()

    return digit_string


"""
컴퓨터 프로그래밍에 많은 명명 규칙이 있지만, 두 규칙이 특히 흔히 쓰입니다. 
첫번째로는, 변수 이름을 'underscore'로 나눠준다거나, (ex. under_score_variable)
두번째로는, 변수 이름을 대소문자 구별해 구분자 (delimiter)없이 쓰는 경우가 있습니다. 
이 두번째의 경우에는 첫번째 단어는 소문자로, 그 후에 오는 단어들의 첫번째 글자들은 대문자로 쓰입니다 (ex. camelCaseVariable). 
"""


def to_camel_case(underscore_str):
    words = underscore_str.split('_')
    tmp = []
    for word in words:
        if word != '':
            tmp.append(word)
    words = tmp

    camelcase_str = words[0]
    if len(words) > 1:
        camelcase_str = camelcase_str.lower()
        for word in words[1:]:
            word = word[0].upper() + word[1:].lower()
            camelcase_str += word

    return camelcase_str
