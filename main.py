import os
import translators

print('''
#########################################################################
#                                                                       #
#                  Welcome to Text Translator                           #
#                                                                       #
#########################################################################
''')
Name = input("Please enter the name of the file: ")
if not os.path.exists(Name):
    print("Error file is not FOUND")
    exit()
text_file = open(Name, "r")
text = text_file.read()
text_japanese = open("text_ja.txt", 'w', encoding='utf-8')
text_german = open("text_de.txt", 'w', encoding='utf-8')
text_japanese.write(translators.google(text, from_language='en', to_language='ja'))
text_german.write(translators.google(text, from_language='en', to_language='de'))
text_german.close()
text_japanese.close()
text_file.close()
print(".......Finished translating.......")
