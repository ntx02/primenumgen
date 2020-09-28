from datetime import datetime

print("Specify the value up to which you would like to calculate prime numbers lower than it")
y = int(input())
numlist = [x for x in range(2,y)]
def primenumfinder(numberlist):
    start_time = datetime.now()
    for num in numberlist:
        for item in numberlist:
            if item % num == 0 and item != num:
                numberlist.pop(numberlist.index(item))
    end_time = datetime.now()
    time_taken = end_time - start_time
    print(numberlist)
    print("It took this program this long to calculate primes up to " + str(y) + ": " + str(time_taken) + " Format: Hours:Minutes:Seconds:Milliseconds.")


primenumfinder(numlist)

def run():
      print("Provide new upper value")
      i = int(input())
      newnumlist = [x for x in range(2,i)]
      primenumfinder(newnumlist)

while 1 == 1:
  print("Run again? y/n")
  answer = input()
  if answer != 'y':
    break
  run()
