from contacts import initialize_csv, add_contact, search_contact, delete_contact, display_contacts


def test_add_contact():
    initialize_csv()
    response = add_contact("Jan Kowalski", "123123123", "jan@gmail.com")
    assert response == "Kontakt dodany"


def test_search_contact():
    add_contact("Anna Nowak", "111111111", "aa@aa.pl")
    response = search_contact("Anna Nowak")
    assert "Anna Nowak" in response


def test_delete_contact():
    add_contact("Marek Nowak", "555666777", "marek@example.com")
    response = delete_contact("Marek Nowak")
    assert response == "Kontakt usunięty"


def test_display_contacts():
    add_contact("Adam Nowak", "444555666", "adam@example.com")
    contacts = display_contacts()
    assert any("Adam Nowak" in contact for contact in contacts)