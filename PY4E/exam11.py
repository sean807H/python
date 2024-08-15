def guest(guest_book):
    entries = guest_book.split("\n")
    invalid_entries = []

    for entry in entries:
        name, phone_number = entry.split(',')
        phone_number = phone_number.strip()

        if not phones_number(phone_number):
            invalid_entries.append((name, phone_number))

    for entry in invalid_entries:
        print(f"잘못 쓴 사람: {entry[0]}")
        print(f"잘못 쓴 번호: {entry[1]}\n")

def phones_number(phone_number):
    if len(phone_number) != 13 or not phone_number.startswith("010") or \
       not phone_number[3] == "-" or not phone_number[7] == "-":
        return False
    return True

guest_book = """김갑,123456789
이을,010-1234-5678
박병,010-5678-111
최정,111-1111-1111
정무,010-3333-3333"""

guest(guest_book)
