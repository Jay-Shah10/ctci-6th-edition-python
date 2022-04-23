"""
Implement an algorithm to determine if a string has all unique characters. What if you cannot
use a datastructure? 
"""

def isUnique(strs):
    
    if len(set(strs)) == len(strs):
        return True
    return False

def main() -> None: 
    strs = "tes"
    result = isUnique(strs)

    print(result)


if __name__ == '__main__':
    main()