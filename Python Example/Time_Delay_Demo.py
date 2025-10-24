# Show time.sleep for demonstration (short pause).

import time

if __name__ == '__main__':
    print("Counting 3...")
    for i in range(1,4):
        print(i)
        time.sleep(0.1)
    print("Done")