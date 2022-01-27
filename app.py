from browser import document, alert

input = document['input']
button = document['btn']
output = document['output']

def getNum(x):
    temp = x
    try:
        temp = int(x)
    except ValueError:
        temp = float(x)
    finally:
        if temp != '' and type(temp) is str:
            alert('Harap masukkan angka')
            temp = ''
            input.value = temp
            return temp
        else:
            return temp

FibArray = [0, 1]
def fibonacci(n):
    if n<0:
        print("Incorrect input")
    elif n<= len(FibArray):
        return FibArray[n-1]
    else:
        temp_fib = fibonacci(n-1)+fibonacci(n-2)
        FibArray.append(temp_fib)
        return temp_fib

def main(ev):
    num = getNum(input.value)
    result = fibonacci(num+1)
    output.textContent = str(result)
button.bind('click', main)
