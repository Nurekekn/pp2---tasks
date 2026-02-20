
# 1. *args
def sum_all(*numbers):
    print(sum(numbers))

sum_all(1, 2, 3, 4)

# 2. **kwargs
def print_info(**info):
    for key, value in info.items():
        print(key, ":", value)

print_info(name="Anna", age=25)

# 3. args + kwargs
def combined(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

combined(1, 2, name="Tom")