def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "خطا: تقسیم بر صفر مجاز نیست"
    return x / y

print("ماشین حساب ساده")
print("عملیات موجود: + , - , * , /")

while True:
    operation = input("عملیات مورد نظر خود را وارد کنید (+, -, *, /) یا 'q' برای خروج: ")
    
    if operation == 'q':
        print("خروج از برنامه...")
        break
    
    if operation in ('+', '-', '*', '/'):
        try:
            num1 = float(input("عدد اول: "))
            num2 = float(input("عدد دوم: "))
        except ValueError:
            print("لطفاً یک عدد معتبر وارد کنید.")
            continue
        
        if operation == '+':
            print("نتیجه:", add(num1, num2))
        elif operation == '-':
            print("نتیجه:", subtract(num1, num2))
        elif operation == '*':
            print("نتیجه:", multiply(num1, num2))
        elif operation == '/':
            print("نتیجه:", divide(num1, num2))
    else:
        print("عملیات نامعتبر است. لطفاً دوباره تلاش کنید.")
