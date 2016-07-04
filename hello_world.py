# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while b < 10:
     print(b)
     a, b = b, a+b

if 5<3:
    print("Things might be a little off..")
else:
    print("Yep, math works today.")
if 5<3:
    print("Things might be a little off...")
elif 5 ==3:
    print("Maybe we should stay inside.")
else:
    print("Yep, math works today.")

    beatles = ("John", "Paul","George","Ringo")
    for beatles in beatles:
        print(beatles)

for n in range(1,100):
    if n % 3 ==0:
        print(n)
else:
    print("The loop is over")

actors = {
    'Kyle MacLachlan' : "Dale Cooper",
    "Sheryl Lee": "Laura Palmer",
    "Lara Flynn Boyle" : "Donna Hayward",
    "Sherilyn Fenn" : "Audrey Horne"
}

miles_run =0
running = True

while running:
    if miles_run <= 10:
        print("Still running! On mile {}" .format(miles_run))
        miles_run +=1
    else:
        running = False
else:
    print("Whew! I'm tired")

a=1
b=0
try:
    a/b
except ZeroDivisionError:
    print("Cannot divide by zero.")

phone_book = {"Sarah Hughes": "01234 567890",
              "Tim Taylor": "02345 678901",
              "Sam Smith": "03456 789012"}

for i in range(1,10):
    print(i)

number_list = [1,1,2,2,2,2,3,3,4,4,5,5,5,5,5,5,6,7,8,8,8,8,9,9,9,9]
count_dict = collections.defaultdict(int)
for i in number_list:
    count_dict[i] += 1

    a=2
    a+=2
    print(a)

