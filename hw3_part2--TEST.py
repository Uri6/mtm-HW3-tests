# Test for the 2nd part of HW3 in mtm (2022a)
# Written by Uri Sivani

from hw3_part2 import *

class static_vars:
    firstFunCnt = 0
    secondFunCnt = 0

def test(fun_num, input, output):

    passed = 0

    if fun_num == 1:
        static_vars.firstFunCnt += 1
        cnt = static_vars.firstFunCnt
        user_output = get_palindrom_dict(input)
        if output == str(user_output):
            passed = 1

    if fun_num == 2:
        static_vars.secondFunCnt += 1
        cnt = static_vars.secondFunCnt
        user_output = check_match(input)
        if output == user_output:
            passed = 1

    if passed == 0:
        print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("Test Num. " + str(cnt) + "Failed")
        print("Input: " + input)
        print("Excepted Output: " + str(output))
        print("Your Output: " + str(user_output))
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")

    else:
        print("Test Num." + str(cnt) + " Passed")

def match_input_preparation(first, second):
    res = ""

    for i in range(0, len(first)):
        res = res + first[i:i+1:1] + second[i:i+1:1]

    return res


print("----------Palindrom-Func-Test-Results----------\n")
test(1, "AbbAcaBBa", "{1: ['A', 'b', 'b', 'A', 'c', 'a', 'B', 'B', 'a'], 2: ['bb', 'BB'], 4: ['AbbA', 'aBBa']}")
test(1, "", "{}")
test(1, "0100abba0010", "{1: ['0', '1', '0', '0', 'a', 'b', 'b', 'a', '0', '0', '1', '0'], 2: ['00', 'bb', '00'], 3: ['010', '010'], 4: ['abba'], 6: ['0abba0'], 8: ['00abba00'], 10: ['100abba001'], 12: ['0100abba0010']}")
test(1, "JimboJ", "{1: ['J', 'i', 'm', 'b', 'o', 'J']}")
test(1, "a b b a", "{1: ['a', ' ', 'b', ' ', 'b', ' ', 'a'], 3: [' b ', 'b b', ' b '], 5: [' b b '], 7: ['a b b a']}")
test(1, "&&##Uri*&^5^&*Sivani##&&", "{1: ['&', '&', '#', '#', 'U', 'r', 'i', '*', '&', '^', '5', '^', '&', '*', 'S', 'i', 'v', 'a', 'n', 'i', '#', '#', '&', '&'], 2: ['&&', '##', '##', '&&'], 3: ['^5^'], 5: ['&^5^&'], 7: ['*&^5^&*']}")

print("\n\n------------Match-Func-Test-Results------------\n")
test(2, match_input_preparation("door", "keep"), True)
test(2, "", True)
test(2, match_input_preparation("keep", "door"), True)
test(2, match_input_preparation("check", "help"), False)
test(2, match_input_preparation("xatal", "tpmpd"), True)
test(2, match_input_preparation("tpmpd", "xatal"), True)
test(2, match_input_preparation("sad", "dad"), True)
test(2, match_input_preparation("dad", "sad"), False)
test(2, match_input_preparation("AmitUlman", "aMITuLMAN"), True)
test(2, match_input_preparation("001101000", "110010111"), True)
test(2, match_input_preparation("abcdefgh", "ijklmnop"), True)
test(2, match_input_preparation("ABBA", "ACDC"), False)
test(2, match_input_preparation("LIVE", "KILL"), True)