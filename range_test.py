print ('Hello! Welcome to fizzbuzz. Please first enter a number to start counting at, and the number you would like us to end on! We will always count up!')
print ('First, the start:')
start = input()
while start.isdigit() == False:
    print ('no, a number please...')
    start = input()

print ('And now, the end. It must be bigger than the last one!')
end = input()
while end.isdigit() == False:
    print ('no, a bigger number please...')
    end = input()

if (int(start) < int(end)):
    x = range(int(start), (int(end)+1), 1)
    for i in x:
        if i % 3 == 0 and i % 5 == 0:
            print ('fizzbuzz')
        elif i % 3 == 0:
            print ('fizz')
        elif i % 5 == 0:
            print ('buzz')
        else:
           print (i)

elif (int(end) < int(start)): 
    x = range(int(start), (int(end)-1), -1)
    for i in x:
        if i % 3 == 0 and i % 5 == 0:
            print ('fizzbuzz')
        elif i % 3 == 0:
            print ('fizz')
        elif i % 5 == 0:
            print ('buzz')
        else:
            print (i)
else: 
    print ('Those numbers are the same, there is no range to print')
print ('Press the "e" key to leave...')
leave = input()
if leave == 'e':
    print ('bye bye')
else:
    print ('You dumb...')
