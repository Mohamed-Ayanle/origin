name = input("What's your name? ")

match name:
    case "Mohamed" | "Ahmed" | "Kamal":
        print("Ayanle")
    case "Safiyo":
        print("Mohamed")
    case _:
        print("Who?")
