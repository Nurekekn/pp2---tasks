#1
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
#2
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))
#3
def myFunction() :
  return True

print(myFunction())
#4
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")
#5
x = 200
print(isinstance(x, int))