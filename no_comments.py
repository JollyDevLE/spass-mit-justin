
prime_file = "prime-numbers.txt"

def create_prime_file():
    import os

    if os.path.isfile(prime_file):
        os.remove(prime_file)
    for number in range(1, 1001):
        if number > 1:
            for i in range(2, number):
                if (number % i) == 0:
                    break
            else:
                file = open(prime_file, "a")
                file.write(str(number) + "\n")
                file.close()

def get_prime_numbers():
    try:
        return open(prime_file, "r").read()
    except OSError as err:
        print("Got error while reading prime-numbers file.")

create_prime_file()
print(get_prime_numbers())


versuch = 0
geheimzahl = 1701
zaehler = 0
while versuch != geheimzahl:
    versuch = int(input("Dein Tipp: "))
    zaehler += 1
    if versuch > geheimzahl:
        print("Zu groß!")
    elif versuch < geheimzahl:
        print("Zu klein!")
    else:
        print("Erraten! Anzahl Versuche: ", zaehler)
