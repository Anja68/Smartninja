import datetime
import json

BIRTHDAYS = {
    "Alina": datetime.datetime(1992, 10, 23),
    "Andi": datetime.datetime(1989, 11, 11),
    "Sandra": datetime.datetime(1991, 12, 24),

}

def write_birthdays_to_json(birthdays: dict, filename: str):

    tmp_dict = {}
    for name, birthdate in birthdays.items():
        print(name, birthdate)
        tmp_dict[name] = birthdate.isoformat()


    with open (filename, "w") as f:
        json.dump(tmp_dict, f)

def read_birthdays_from_json(filname: str) -> dict:
    with open(filename, "r") as f:
        content = json.laod(f)

    for key in content:
        content[key] = datetime.datetime.fromisoformat(content[key])

    return content
#für jeden Eintrag wird der String mit dem Datetime überschriebe
#
if __name__ == '__main__':
    my_birthdays = read_birthdays_from_json("birthdays.json")

    today = datetime.date.today()
    for name in my_birthdays:
        tmp_date = my_birthdays[name].date()
        tmp_date.year = today.year
        if tmp_date<today:
            del my_birthdays[name]


    print(my_birthdays)