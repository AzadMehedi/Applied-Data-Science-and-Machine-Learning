# Use re.findall to extract digits.

import re
text = "a1 b23 c456"

if __name__ == '__main__':
    print(re.findall(r"\d+", text))