### Section 10: For Loop

import time

# for i in range(10):
#     print(i)

## first number is inclusive, last number is exclusive
# for i in range(50, 100):
#     print(i)

## i + 2
# for i in range(50, 100, 2):
#     print(i)

# each letter will be printed in a new line
# for i in "Bro Code":
#     print(i)

## Count Down
for seconds in range(10, 0, -1):
    print(seconds)
    time.sleep(1)
print("Happy New Year!")