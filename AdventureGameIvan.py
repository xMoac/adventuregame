import random

def main():
    print("Välkommen till häxans hus!")
    print("Du är i en skog och ser ett hus gjort av godis, din hunger gör att du närmar dig...!")

    name = input("Vad heter du? ")
    print(f"Hej, {name}! Du har tre val , endas den ena leder ut.")

    while True:
        print("\nVad vill du göra:")
        print("1. Gå in i huset genom att äta en sida av vägen gjort av lussekat")
        print("2. Gå genom det öppna fönstret på baksidan.")
        print("3. Knacka på dörren")

        choice = input("Ange ditt val (1/2/3): ")

        if choice == "1":
            explore_wall(name)
        elif choice == "2":
            explore_window(name)
        elif choice == "3":
            print("En häxa möter dig med en stor säck öppen. Otäckt slut!")
            break
        else:
            print("Ogiltigt val.")

def explore_wall(name):
    print(f"{name} går in genom vägen...")
    result = random.choice([True, False])

    if result:
        print("Grattis! Du åt dig full med lussekatt och lämnade huset däreefter! hipphipp hurra!!!")
    else:
        print(f"Du åt för mycket lussekatt och blev dålig i magen. {name} blev tagen av häxan. Spelet är över.")

def explore_window(name):
    print(f"{name} går in genom fönstret...")
    result = random.choice([True, False])

    if result:
        print(f"En godis påse fyld med guld , {name} tar den och springer hem!")
    else:
        print(f"{name} faller över fönsterkanten och väcker häxan. SPRING!!! Ahhhhh!!!.")

if __name__ == "__main__":
    main()

