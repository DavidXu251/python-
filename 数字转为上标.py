

import pyperclip
dic={x:y for x,y in zip('0123456789','₀₁₂₃₄₅₆₇₈₉')}

while True:
    line=input('>')
    line2=''.join([
        dic.get(char, char) for char in line
    ])
    pyperclip.copy(line2)
    print(line2)
