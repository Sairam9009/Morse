from playsound import playsound
import time
print('''


███╗░░░███╗░█████╗░██████╗░░██████╗███████╗  ░█████╗░░█████╗░██████╗░███████╗
████╗░████║██╔══██╗██╔══██╗██╔════╝██╔════╝  ██╔══██╗██╔══██╗██╔══██╗██╔════╝
██╔████╔██║██║░░██║██████╔╝╚█████╗░█████╗░░  ██║░░╚═╝██║░░██║██║░░██║█████╗░░
██║╚██╔╝██║██║░░██║██╔══██╗░╚═══██╗██╔══╝░░  ██║░░██╗██║░░██║██║░░██║██╔══╝░░
██║░╚═╝░██║╚█████╔╝██║░░██║██████╔╝███████╗  ╚█████╔╝╚█████╔╝██████╔╝███████╗
╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚═╝╚═════╝░╚══════╝  ░╚════╝░░╚════╝░╚═════╝░╚══════╝

░█████╗░░█████╗░███╗░░██╗██╗░░░██╗███████╗██████╗░████████╗███████╗██████╗░
██╔══██╗██╔══██╗████╗░██║██║░░░██║██╔════╝██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
██║░░╚═╝██║░░██║██╔██╗██║╚██╗░██╔╝█████╗░░██████╔╝░░░██║░░░█████╗░░██████╔╝
██║░░██╗██║░░██║██║╚████║░╚████╔╝░██╔══╝░░██╔══██╗░░░██║░░░██╔══╝░░██╔══██╗
╚█████╔╝╚█████╔╝██║░╚███║░░╚██╔╝░░███████╗██║░░██║░░░██║░░░███████╗██║░░██║
░╚════╝░░╚════╝░╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝''')

morse_code_letter_dict = {
    'A': ".-", 'B': "-...", 'C': "-.-.", 'D': "-..", 'E': ".",
    'F': "..-.", 'G': "--.", 'H': "....", 'I': "..", 'J': '.---',
    'K': "-.-", 'L': ".-..", 'M': "--", 'N': "-.", 'O': "---",
    'P': ".--.", 'Q': "--.-", 'R': ".-.", 'S': '...', 'T': "-",
    'U': "..-", 'V': "...-", 'W': ".--", 'X': "-..-", 'Y': "-.--",
    'Z': "--..",
}
morse_code_number_dict = {
    '0': "-----", '1': ".----", '2': "..---", '3': "...--", '4': "....-", '5': ".....",
    '6': "-....", '7': "--...", '8': "---..", '9': "----."
}
morse_code_sound_dict = {
    'A': "MorseSounds/A.mp3", 'B': "MorseSounds/B.mp3", 'C': "MorseSounds/C.mp3", 'D': "MorseSounds/D.mp3",
    'E': "MorseSounds/E.mp3",
    'F': "MorseSounds/F.mp3", 'G': "MorseSounds/G.mp3", 'H': "MorseSounds/H.mp3", 'I': "MorseSounds/I.mp3",
    'J': 'MorseSounds/J.mp3',
    'K': "MorseSounds/K.mp3", 'L': "MorseSounds/L.mp3", 'M': "MorseSounds/M.mp3", 'N': "MorseSounds/N.mp3",
    'O': "MorseSounds/O.mp3",
    'P': "MorseSounds/P.mp3", 'Q': "MorseSounds/Q.mp3", 'R': "MorseSounds/R.mp3", 'S': 'MorseSounds/S.mp3',
    'T': "MorseSounds/T.mp3",
    'U': "MorseSounds/U.mp3", 'V': "MorseSounds/V.mp3", 'W': "MorseSounds/W.mp3", 'X': "MorseSounds/X.mp3",
    'Y': "MorseSounds/Y.mp3", 'Z': "MorseSounds/Z.mp3",
    '1': "MorseSounds/1.mp3", '2': "MorseSounds/2.mp3", '3': "MorseSounds/3.mp3", '4': "MorseSounds/4.mp3",
    '5': "MorseSounds/5.mp3", '6': "MorseSounds/6.mp3", '7': "MorseSounds/8.mp3", '8': "MorseSounds/8.mp3",
    '9': "MorseSounds/9.mp3", '0': "MorseSounds/0.mp3",
}
user_input = input("\nWrite your sentence. Please remember this takes only alphabets [A-Z] and numbers [0-9]\t")
user_input = user_input.upper()
to_convert_list = user_input.split()
for word in to_convert_list:
    for letter in word:
        try:
            morsed = morse_code_letter_dict[letter]
            sound = morse_code_sound_dict[letter]
        except KeyError:
            morsed = morse_code_number_dict[letter]
            sound = morse_code_sound_dict[letter]
        finally:
            playsound(sound)
            time.sleep(0.01)
            print(morsed + " ", end='', flush=True)



