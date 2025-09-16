"""Have to print the number of times that the substring occurs in the given string. 
String traversal will take place from left to right, not from right to left."""

def count_substring(string, sub_string):
    count = 0
    for i in range(0, len(string) + 1):
        if string[i:i + len(sub_string)] == sub_string:
            count = count + 1
    return count

print(count_substring("ABCDCDC", "CDC"))

String = "ABCDCDC"
Sub_string = "CDC"

print(String[7:7 + len(Sub_string)])