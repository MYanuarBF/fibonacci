from browser import document

input = document['input']
button = document['btn']
output = document['output']

fibonacci_cache={}
              
def fibonacci(n):
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    if n == 1:
        value=1
    elif n == 2:
        value=1
    elif n>2: 
        value =fibonacci(n-1)+ fibonacci(n-2)
        fibonacci_cache[n]=value
    return value 
            
def main():
    result = fibonacci(input.value)
    output.textContent = str(result)

button.bind('click', main)