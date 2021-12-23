#Python function that checks whether a passed string is palindrome or not.
def isPalindrome(string):
    left_pos = 0
    right_pos = len(string) - 1

    while right_pos >= left_pos:
        if not string[left_pos] == string[right_pos]:
            return False
        left_pos += 1
        right_pos -= 1
    return True
print(isPalindrome('madam'))

#Python function that checks if the number is prime or not
def test_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True;
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True
print(test_prime(10))

#Python function to check whether a number is in a given range.
def test_range(n):
    if n in range(3,9):
        print( " %s is in the range"%str(n))
    else :
        print("The number is outside the given range.")
test_range(5)

#Python function to calculate the factorial of a number
def fact(n):
    factorial = 1
    if n < 0:
        print(" Factorial does not exist for negative numbers")
    elif n == 0:
        return factorial
    else:
        for i in range(1, n + 1):
            factorial = factorial * i
    return factorial
print(fact(10))

#Python program to reverse a string.
def reverse_string(str):
    str1 = ""   # Declaring empty string to store the reversed string
    for i in str:
        str1 = i + str1
    return str1
print(reverse_string("JavaTpoint"))

#Python function to sum all the numbers in a list.
def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print(sum((8, 2, 3, 0, 7)))

#Python function to find the Max of three numbers.
def maximum(a, b, c):
    if (a >= b) and (a >= c):
        largest = a

    elif (b >= a) and (b >= c):
        largest = b
    else:
        largest = c

    return largest
print(maximum(5,9,3))