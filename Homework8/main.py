from datetime import date, datetime, timedelta


current_date = date.today()
current_year = current_date.year


def get_birthdays_per_week(users):

    if not users:
        # if no user in users, we return empty dict
        return dict()
    else:
        today_date = date.today()
        my_year = today_date.year

        celebrate = {'Monday': [], 'Tuesday': [], 'Wednesday': [],
                     'Thursday': [], 'Friday': []}
        for user in users:
            user_date = user['birthday'].replace(year=my_year)
            # check all birthdays in this year
            delta = user_date - today_date
            if timedelta(days=0) <= delta <= timedelta(days=7):
                # if birthday in on week with my day
                day = user_date.weekday()
                if day == 0 or day == 5 or day == 6:
                    # if birthday is Monday, Saturday or Sunday
                    celebrate['Monday'].append(user['name'])
                elif day == 1:
                    celebrate['Tuesday'].append(user['name'])
                elif day == 2:
                    celebrate['Wednesday'].append(user['name'])
                elif day == 3:
                    celebrate['Thursday'].append(user['name'])
                elif day == 4:
                    celebrate['Friday'].append(user['name'])

            user1_date = user['birthday'].replace(year=current_year + 1)
            # check all birthdays in next year
            delta1 = user1_date - current_date
            if timedelta(days=0) <= delta1 <= timedelta(days=7):
                day = user1_date.weekday()
                if day == 0 or day == 5 or day == 6:
                    celebrate['Monday'].append(user['name'])
                elif day == 1:
                    celebrate['Tuesday'].append(user['name'])
                elif day == 2:
                    celebrate['Wednesday'].append(user['name'])
                elif day == 3:
                    celebrate['Thursday'].append(user['name'])
                elif day == 4:
                    celebrate['Friday'].append(user['name'])
        users = dict()
        for key, value in celebrate.items():
            if value:
                users[key] = celebrate[key]

        return users


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]
    result = get_birthdays_per_week(users)
    print(result)

    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
