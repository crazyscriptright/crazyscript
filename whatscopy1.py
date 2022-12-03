import pyfiglet
print(pyfiglet.FigletFont.getFonts()) #FOR TO KNOW FONTS AVAILBLE IN pyfiglet

for i in range(0, 26):
    K = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
         'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    wish = pyfiglet.figlet_format(K[i], font="ascii___")
    print(wish)
