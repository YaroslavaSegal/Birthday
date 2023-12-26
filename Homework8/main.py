from datetime import date, datetime, timedelta

current_date = date.today()
current_year = current_date.year


def get_birthdays_per_week(users):

    if users == []:
        #якщо у списку немає користувачів, повертаємо пустий словник
        return dict()
    else:
        current_date = date.today()
        current_year = current_date.year

        celebrate = {'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': []}
        for user in users:
            user_date = user['birthday'].replace(year=current_year)
            # переверіємо всі дні народження в цьому році
            if timedelta(days=0) <= (user_date - current_date) <= timedelta(days=7):
                # якщо день народження співпадає з тестовим днем або більше в межах тижня
                if user_date.weekday() == 0 or user_date.weekday() == 5 or user_date.weekday() == 6:
                    # якщо це понеділок, субота або неділя, додаємо користувача до списку по ключу 'Monday'
                    celebrate['Monday'].append(user['name'])
                elif user_date.weekday() == 1:
                    # якщо це вівторок, додаємо користувача до списку по ключу 'Tuesday'
                    celebrate['Tuesday'].append(user['name'])
                elif user_date.weekday() == 2:
                    celebrate['Wednesday'].append(user['name'])
                elif user_date.weekday() == 3:
                    celebrate['Thursday'].append(user['name'])
                elif user_date.weekday() == 4:
                    celebrate['Friday'].append(user['name'])

            user1_date = user['birthday'].replace(year=current_year + 1)
            # переверіємо всі дні народження в наступному році
            if timedelta(days=0) <= (user1_date - current_date) <= timedelta(days=7):
                if user1_date.weekday() == 0 or user1_date.weekday() == 5 or user1_date.weekday() == 6:
                    celebrate['Monday'].append(user['name'])
                elif user1_date.weekday() == 1:
                    celebrate['Tuesday'].append(user['name'])
                elif user1_date.weekday() == 2:
                    celebrate['Wednesday'].append(user['name'])
                elif user1_date.weekday() == 3:
                    celebrate['Thursday'].append(user['name'])
                elif user1_date.weekday() == 4:
                    celebrate['Friday'].append(user['name'])
        users = dict()
        # створюємо словник іменинників тижня
        for key, value in celebrate.items():
            if value != []:
                users[key] = celebrate[key]

        return users


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]
    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
        # виводимо іменинників по дням тижня
