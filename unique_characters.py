# Implement an algorithm to determine if a string has all unique characters , without using additional data structures

def string_unique_characters(s):
    s = s.lower()
    if (len(s) < 127) :
        bool_list = [False] * 127
        for i in s:
            value = ord(i)
            if bool_list[value] is not True:
                bool_list[value] = True
            else:
                return False
        return True
    else:
        return False

if __name__ == "__main__" :

    s = "Pradeep"
    u ="abr"
    t = "Abrac"

    result = string_unique_characters(t)

    if result:
        print("Unique String")
    else:
        print("Not a unique String")