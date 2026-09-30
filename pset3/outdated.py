months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    date = input("Date: ").strip()
    try:
        if "/" in date:
            month, day, year = date.split("/")
            month = int(month)
            day = int(day)
            year = int(year)
        else:
            month_name, day, year = date.split(" ")
            if not day.endswith(","):
                raise ValueError
            month = months.index(month_name) + 1
            day = int(day.replace(",", ""))
            year = int(year)

        if month < 1 or month > 12 or day < 1 or day > 31:
            raise ValueError

        print(f"{year}-{month:02}-{day:02}")
        break
    except ValueError:
        pass
    