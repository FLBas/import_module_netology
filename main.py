from application import salary
from application.db import people
from datetime import datetime, date, time
import requests

def main():
    return requests.get('https://www.google.ru/')


d = date(2023, 6, 16)
t = time(19, 30)

if __name__ == '__main__':
    print(datetime.combine(d, t))
    salary.calculate_salary()
    people.get_employees()
