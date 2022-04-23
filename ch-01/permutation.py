"""
Given two strings, write a method to decide if one is a 
permutation of the other. 
"""


def isPermutation(str1, str2) -> bool: 
    n1 = len(str1)
    n2 = len(str2)

    if n1 != n2: 
        return False
    
    a = sorted(str1)
    str1 = " ".join(a)
    b = sorted(str2)
    str2 = " ".join(a)

    for i in range(0, n1, 1):
        if str1[i] != str2[i]:
            return False
        return True

def main() -> None: 
    
    str1 = "dog"
    str2 = "bca"

    result = isPermutation(str1=str1, str2=str2)
    print(result)

if __name__ == '__main__':
    main()