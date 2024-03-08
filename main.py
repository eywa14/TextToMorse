import pyperclip

DOT = '▄'
DASH = '▄▄▄'
SPACE = ' '
SPACE_LETTER = '   '
SPACE_WORD = '       '

char_in_morse = {'A': f'{DOT}{SPACE}{DASH}',
                 'B': f'{DASH}{SPACE}{DOT}{SPACE}{DOT}{SPACE}{DOT}',
                 'C': f'{DASH}{SPACE}{DOT}{SPACE}{DASH}{SPACE}{DOT}',
                 'D': f'{DASH}{SPACE}{DOT}{SPACE}{DOT}',
                 'E': f'{DOT}',
                 'F': f'{DOT}{SPACE}{DOT}{SPACE}{DASH}{SPACE}{DOT}',
                 'G': f'{DASH}{SPACE}{DASH}{SPACE}{DOT}',
                 'H': f'{DOT}{SPACE}{DOT}{SPACE}{DOT}{SPACE}{DOT}',
                 'I': f'{DOT}{SPACE}{DOT}',
                 'J': f'{DOT}{SPACE}{DASH}{SPACE}{DASH}{SPACE}{DASH}',
                 'K': f'{DASH}{SPACE}{DOT}{SPACE}{DASH}',
                 'L': f'{DOT}{SPACE}{DASH}{SPACE}{DOT}{SPACE}{DOT}',
                 'M': f'{DASH}{SPACE}{DASH}',
                 'N': f'{DASH}{SPACE}{DOT}',
                 'O': f'{DASH}{SPACE}{DASH}{SPACE}{DASH}',
                 'P': f'{DOT}{SPACE}{DASH}{SPACE}{DASH}{SPACE}{DOT}',
                 'Q': f'{DASH}{SPACE}{DASH}{SPACE}{DOT}{SPACE}{DASH}',
                 'R': f'{DOT}{SPACE}{DASH}{SPACE}{DOT}',
                 'S': f'{DOT}{SPACE}{DOT}{SPACE}{DOT}',
                 'T': f'{DASH}',
                 'U': f'{DOT}{SPACE}{DOT}{SPACE}{DASH}',
                 'V': f'{DOT}{SPACE}{DOT}{SPACE}{DOT}{SPACE}{DASH}',
                 'W': f'{DOT}{SPACE}{DASH}{SPACE}{DASH}',
                 'X': f'{DASH}{SPACE}{DOT}{SPACE}{DOT}{SPACE}{DASH}',
                 'Y': f'{DASH}{SPACE}{DOT}{SPACE}{DASH}{SPACE}{DASH}',
                 'Z': f'{DASH}{SPACE}{DASH}{SPACE}{DOT}{SPACE}{DOT}',
                 '1': f'{DOT}{SPACE}{DASH}{SPACE}{DASH}{SPACE}{DASH}{SPACE}{DASH}',
                 '2': f'{DOT}{SPACE}{DOT}{SPACE}{DASH}{SPACE}{DASH}{SPACE}{DASH}',
                 '3': f'{DOT}{SPACE}{DOT}{SPACE}{DOT}{SPACE}{DASH}{SPACE}{DASH}',
                 '4': f'{DOT}{SPACE}{DOT}{SPACE}{DOT}{SPACE}{DOT}{SPACE}{DASH}',
                 '5': f'{DOT}{SPACE}{DOT}{SPACE}{DOT}{SPACE}{DOT}{SPACE}{DOT}',
                 '6': f'{DASH}{SPACE}{DOT}{SPACE}{DOT}{SPACE}{DOT}{SPACE}{DOT}',
                 '7': f'{DASH}{SPACE}{DASH}{SPACE}{DOT}{SPACE}{DOT}{SPACE}{DOT}',
                 '8': f'{DASH}{SPACE}{DASH}{SPACE}{DASH}{SPACE}{DOT}{SPACE}{DOT}',
                 '9': f'{DASH}{SPACE}{DASH}{SPACE}{DASH}{SPACE}{DASH}{SPACE}{DOT}',
                 '0': f'{DASH}{SPACE}{DASH}{SPACE}{DASH}{SPACE}{DASH}{SPACE}{DASH}'}


def word_to_morse(string: str) -> str | None:
    """
    :param string: Any word or number
    :return: A string of that word or number in International Morse Code
    """
    word_in_morse = ''
    for idx, char in enumerate(string):
        try:
            if idx == len(string) - 1:
                word_in_morse += f'{char_in_morse[char]}'
            else:
                word_in_morse += f'{char_in_morse[char]}{SPACE_LETTER}'
        except KeyError:
            print(f'\033[91m Error: "{char}" not translatable into Morse Code. \033[0m')
            exit(1)
    return word_in_morse


print(
    r'''
     _________  _______      ___    ___ _________        _________  ________     
    |\___   ___\\  ___ \    |\  \  /  /|\___   ___\     |\___   ___\\   __  \    
    \|___ \  \_\ \   __/|   \ \  \/  / ||___ \  \_|     \|___ \  \_\ \  \|\  \   
         \ \  \ \ \  \_|/__  \ \    / /     \ \  \           \ \  \ \ \  \\\  \  
          \ \  \ \ \  \_|\ \  /     \/       \ \  \           \ \  \ \ \  \\\  \ 
           \ \__\ \ \_______\/  /\   \        \ \__\           \ \__\ \ \_______\
            \|__|  \|_______/__/ /\ __\        \|__|            \|__|  \|_______|
                            |__|/ \|__|                                          
                                                                                 
                                                                                 
     _____ ______   ________  ________  ________  _______                        
    |\   _ \  _   \|\   __  \|\   __  \|\   ____\|\  ___ \                       
    \ \  \\\__\ \  \ \  \|\  \ \  \|\  \ \  \___|\ \   __/|                      
     \ \  \\|__| \  \ \  \\\  \ \   _  _\ \_____  \ \  \_|/__                    
      \ \  \    \ \  \ \  \\\  \ \  \\  \\|____|\  \ \  \_|\ \                   
       \ \__\    \ \__\ \_______\ \__\\ _\ ____\_\  \ \_______\                  
        \|__|     \|__|\|_______|\|__|\|__|\_________\|_______|                  
                                          \|_________|                                                                         
    '''
    )

text = input('Input: ').upper()
split_text = text.split()
output = ''

for idx, word in enumerate(split_text):
    if idx == len(split_text) - 1:
        output += word_to_morse(word)
    else:
        output += f'{word_to_morse(word)}{SPACE_WORD}'

print(f'Output: {output}')

pyperclip.copy(output)
print('Output copied to clipboard!')
