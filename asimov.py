def give_asimov_hint():

    noten_str = open("notenliste.txt").read()
    if "5" in noten_str:
        print("Bewertungen mit 5 werden mit 'keine Wertung' ersetzt.")
    text = noten_str.replace("5", "keine Wertung")
    with open("notenliste.txt", "w") as noten_replace:
        noten_replace.write(text)
