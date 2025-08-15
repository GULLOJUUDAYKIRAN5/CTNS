import time
for i in reversed(range(10)):
    print(f'\r{i}',end="")
    time.sleep(1)