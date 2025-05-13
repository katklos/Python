import os, csv

CSV_FILE = "contacts.csv"


def initialize_csv():
    if not os.path.exists(CSV_FILE):
        try:
            with open(CSV_FILE, "x", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Name", "Phone", "Email"])
        except FileExistsError:
            pass


def read_csv_file():
    with open(CSV_FILE, "r") as file:
        reader = csv.reader(file)
        return list(reader)


def write_csv_file(contacts):
    with open(CSV_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(contacts)


def display_contacts():
    contacts = read_csv_file()[1:]
    return [f"Imię: {row[0]}, Telefon: {row[1]}, Email: {row[2]}" for row in contacts]


def add_contact(name, phone, email):
    contacts = read_csv_file()
    contacts.append([name, phone, email])
    write_csv_file(contacts)
    return "Kontakt dodany"


def search_contact(name):
    contacts = read_csv_file()[1:]
    for row in contacts:
        if row[0].lower() == name.lower():
            return f"Znaleziono: Imię: {row[0]}, Telefon: {row[1]}, Email: {row[2]}"
    return "Kontakt nie istnieje"


def delete_contact(name):
    contacts = read_csv_file()
    filtered_contacts = [contacts[0]] + [row for row in contacts[1:] if row[0].lower() != name.lower()]
    if len(filtered_contacts) == len(contacts):
        return "Kontakt nie znaleziony"
    else:
        write_csv_file(filtered_contacts)
        return "Kontakt usunięty"


def main():
    initialize_csv()
    while True:
        print("\n")
        print("1.Dodaj kontakt")
        print("2.Wyświetl kontakty")
        print("3.Wyszukaj kontakt")
        print("4.Usuń kontakt")
        print("5.Wyjście")

        choice = input("Wybierz opcję: ")

        if choice == "1":
            print("Dodaj kontakt")
            name = input("Podaj imię: ")
            phone = input("Podaj numer telefonu: ")
            email = input("Podaj email")
            print(add_contact(name, phone, email))
        elif choice == "2":
            print("Wyświetl kontakty")
            contacts = display_contacts()
            for contact in contacts:
                print(contact)
        elif choice == "3":
            print("Wyszukaj kontakt")
            name = input("Podaj imię do wyszukania: ")
            print(search_contact(name))
        elif choice == "4":
            print("Usuń kontakt")
            name = input("Podaj imię do usunięcia: ")
            print(delete_contact(name))
        elif choice == "5":
            print("Zamykam program.")
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")


if __name__ == "__main__":
    main()