from django.shortcuts import render
import math

def display_factorials(request):
    numbers = range(3, 9)  
    factorials = []

    for num in numbers:
        factorial_result = math.factorial(num)
        factorials.append(f"Factorial of {num} is {factorial_result}")

    context = {
        'factorials': factorials
    }
    
    return render(request, 'factorials.html', context)
