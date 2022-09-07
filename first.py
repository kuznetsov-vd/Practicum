import datetime as dt


class Record:
    def __init__(self, amount, comment, date = ''):
        self.amount = amount
        self.comment = comment
        self.date = date
        if self.date == '':
            self.date = dt.datetime.now().date()
        else:
            self.data = dt.datetime.strptime(date, '%d.%m.%Y').date()
        self.comment = comment

class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []
    def add_record(self, record):
        self.records.append(record)
    def get_today_stats(self):
        today_count = 0
        for r in self.records:
            if r.date == dt.datetime.now().date():
                today_count += r.amount
        return today_count
    def get_week_stats(self):
        week_count = 0
        today = dt.datetime.today()
        week_ago = today - dt.timedelta(days=7)
        for r in self.records:
            if week_ago <= r.date <= today:
                week_count += r.amount
        return week_count
    def get_available_limit(self):
        return self.limit - self.get_today_stats()

    
class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        stats = Calculator.get_available_limit()
        if stats > 0:
            return (f"Сегодня можно съесть что-нибудь еще, но с общей калорийностью не более {stats} Ккал")
        else:
            return ('Хватит есть!')

class CashCalculator(Calculator):
    USD_RATE = 61.18
    EURO_RATE = 60.52
    RUB_RATE = 1

    currencies = {'usd': [USD_RATE, 'USD'],
                  'euro': [EURO_RATE, 'EURO'],
                  'rub': [RUB_RATE, 'RUB']}


    def get_today_cash_remained(self, currency):
        today_stats = Calculator.get_available_limit(self)
        stat = today_stats/self.currencies[currency][0]
        currency_name = self.currencies[currency][1]

        if stat == 0:
            return('Денег нет, но вы держитесь')
        elif stat > 0:
            return(f'На сегодня осталось {stat:.2f} {currency_name}')
        else:
            return(f"Денег нет, но вы держитесь. Ваш долг: {stat:2f} {currency_name}")