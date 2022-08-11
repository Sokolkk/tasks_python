#1. Напишите функцию, которая на вход принимает строку, состоящую из строчных и заглавных латинских символов, а возвращает кортеж из двух элементов: символа, который встречается в строке чаще всего (без учета регистра!), и числа вхождений этого символа в строку. Если таких символов несколько, функция должна вернуть любой из них. Например, для строки "aaaAAAbc" результатом работы функции будет ('a', 6).
def countC(string1):
    string1 = string1.lower()
    list1=[]
    list2=[]
    for i in string1:
        if i not in list1:
            list1.append(i)#appending unique characters of string
            list2.append(string1.count(i))   
    a=max(list2) #finding maximum in the list
    b=list1[list2.index(a)]
    c = list()#create list for insert element tuple for result
    c.insert(0, a)
    c.insert(0, b)
    c = tuple(c)
    print(c)

#2. Напишите функцию, которая на вход принимает единственное целое число N, а возвращает целый квадратный корень из этого числа, если такой существует, или None, если такого корня нет. При решении задачи можно использовать только операторы цикла, условного перехода и встроенную функцию range(). Нельзя использовать функцию sqrt() из модуля math для извлечения квадратного корня.
def sqrt(number):
   number = round(number ** (0.5))
   print(number)
   
#3. Напишите функцию, которая принимает на вход строку, состояющую из символов '(' и ')', задающих скобочную последовательность, и возвращает True, если последовательность корректна, иначе False.
def bracket(str):
    count = [] 
    for i in str: #check "(" and ")" in string, if true append 1 to count
        if i == "(":
            count.append(1)
        elif i == ")":
            count.append(1)      
        else:
            count.append(0)
    if 0 in count: #check another elements in count
        print(False)
    else:
        print(True)
