def second_largest():
    nums = list(map(int, input("Enter nums: ").split(" ")))

    largest = second_largest = nums[0]

    for i in range(1, len(nums)):
        if nums[i] > largest:
            second_largest = largest
            largest = nums[i]
        elif nums[i] > second_largest and nums[i] != largest:
            second_largest = nums[i]

    return second_largest

#print(second_largest())



def vowels():
    str = input().lower()
    counter = 0
    
    for letter in str:
        if letter in ["a","e","i","o","u"]:
            counter += 1
            
    return counter

#print(vowels())
            
            
import re
def password_validate():
    password = input()

    if len(password) >= 8 and re.search('[A-Z]+', password) and re.search('[0-9]+', password):
        return "Valid Password"
    else:
        return "Invalid Password"

#print(password_validate())


def palindrome():
    str = input().lower().strip()
    
    if str[0:] == str[::-1]:
        return "Palindrome"
    else:
        return "Not palindrome"
    
#print(palindrome())



def missing():
    nums = list(map(int, input("Enter nums: ").split(" ")))
    
    n = len(nums)+1
    expected = (n*(n+1))/2
    
    return int(expected - sum(nums))

#print(missing())


def prime():
    num = int(input())
    
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return "Not prime"
        else:
            return "Prime"

#print(prime())



def main():
    sentence = input()
    frequency(sentence)

def frequency(sentence):
    words = {}
    
    for word in sentence.lower().strip().split(" "):
        if word in words:   
            words[word] +=1
            
        else:
            words[word] = 1
        
    for key, value in words.items():
        print(f"{key}: {value}")
        
        
            
            
main()

        
    
            
        
        
