import math
import os
from asimov import give_asimov_hint
# os.chdir("C:/Users/justink/OneDrive/Dokumente/HuFa/1_Sem/Python/exam")

# variablen und funktionsnamen einheitlich in englisch oder deutsch schreiben
# Vorname, Nachname, Matrikelnummer in Tupel speichern
def get_partial_comment(zeile, position):
    separated_line = lines[zeile].split()
    return separated_line[position]

# input ohne Kommentare speichern; Code-, Kommentarzeilen als Integer ausgeben
def delete_comments_and_count_lines():
    with open("no_comments.py", "w") as no_comments_file:
        for line in lines:
            if line.startswith("#"):
                continue
            no_comments_file.write(line)

    global num_codelines, num_commentlines

    num_codelines = len(open("no_comments.py").readlines())
    num_commentlines = len(lines) - num_codelines
    print(num_codelines)
    print(num_commentlines)

# Anzahl if-Anweisungen
def get_number_of_words(word):
    return input_str.count(word)

# Summe for- und while-Anweisungen
def get_sum_for_while():
    return get_number_of_words("for") + get_number_of_words("while")

# Ueberpruefung Klammern # Funktion überprüfen
def parentheses_match():
    speicher = []
    balanced = True
    index = 0
    while index < len(input_str) and balanced:
        token = input_str[index]
        if token == "(":
            speicher.append(token)
        elif token == ")":
            if len(speicher) == 0:
                balanced = False
            else:
                speicher.pop()
        index += 1
    return balanced and len(speicher) == 0

# Ueberpruefung, ob Matrikelnummer = Fibonacci-Zahl
def is_square(number):
    t = int(math.sqrt(number))
    return t*t == number


def is_fibonacci(number):
    return is_square(5*int(number)*int(number) + 4) or\
       is_square(5*int(number)*int(number) - 4)

# Benotung des Programmierbelegs
def get_cross_sum(number):
    cross_sum = sum(int(digit) for digit in str(number))
    return cross_sum if cross_sum < 10 else get_cross_sum(cross_sum)

# erklärung blie bla blubb
# parameters:
# isTrue - bli bla blubb
# num_true -
# num_false -
def give_number(isTrue, num_true, num_false):
    return num_true if isTrue else num_false

def get_calculated_grade():
    note_zaehler = (len(vorname) + num_codelines)//(num_commentlines **
                    give_number(is_fibonacci(matrikelnummer), 2, 1))
    note_ges = get_cross_sum(note_zaehler)/(2 +\
               give_number(parentheses_match(), 1, 0))

    if get_number_of_words("if") >= get_sum_for_while():
        note_rund = math.ceil(note_ges)
    else:
        note_rund = math.floor(note_ges)

    return (note_rund)

# Notenliste anhaengen
def save_grade_record():
    open("notenliste.txt", "a").write(
        vorname + ", "
         + nachname + ", "
         + matrikelnummer + ", "
         + str(get_calculated_grade()) +
         "\n"
     )


input = open("input.py", "r")
lines = input.readlines()
input_str = open("input.py", "r").read() # warum muss ich das extra oeffnen? --> ggf. hier mal schauen ob es ein aynchronitäts problem ist
input.close()

matrikelnummer = get_partial_comment(1, 1)
vorname = get_partial_comment(0, 1)
nachname = get_partial_comment(0, -1) # für den fall den fall das es mehrere vornamen gibt
personal_info_tuple = (vorname, nachname, matrikelnummer)
print(personal_info_tuple)

delete_comments_and_count_lines()

print("Anzahl if-Anweisungen: " + str(get_number_of_words("if")))

print("Summe aus for- und while-Schleifen: " + str(get_sum_for_while()))

print("Geoeffnete Klammern sind geschlossen: " + str(parentheses_match()))

print("Die Matrikelnummer ist eine Fibonacci-Zahl: " + str(is_fibonacci(matrikelnummer)))

print("Die gerundete Note lautet: " + str(get_calculated_grade()))

save_grade_record()

# Zusatzaufgabe Asimov
give_asimov_hint()
