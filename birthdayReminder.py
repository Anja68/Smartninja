import datetime
import json

BIRTHDAYS = {
    "Toni": datetime.datetime(1991, 2, 11),
    "Josephine": datetime.datetime(1993, 11, 11),
    "Karla": datetime.datetime(1983, 12, 25),
}


def write_birthdays_to_json(birthdays: dict, filename: str):

    tmp_dict = {}
    for name, birthdate in birthdays.items():
        print(name, birthdate)
        tmp_dict[name] = birthdate.isoformat()

    with open(filename, "w") as f:
        json.dump(tmp_dict, f)


def read_birthdays_from_json(filename: str) -> dict:
    with open(filename, "r") as f:
        content = json.load(f)

    for name in content:
        content[name] = datetime.datetime.fromisoformat(content[name])

    return content

def get_upcoming_




if __name__ == '__main__':
    #write_birthdays_to_json(BIRTHDAYS, "birthdays.json")
    my_birthdays = read_birthdays_from_json("birthdays.json")

    today = datetime.date.today()

    tmp_birthdate = my_birthdays.copy()

    for name in tmp_birthdate:
        tmp_date = my_birthdays[name].date()
        tmp_date = datetime.date(today.year, tmp_date.month, tmp_date.day)
        if tmp_date<today:
            del my_birthdays[name]

    print(my_birthdays)
