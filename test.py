import first

def main():
    cash_calculator = first.CashCalculator(2000)
    record = first.Record(amount = 2100, comment= 'shop')
    cash_calculator.add_record(record)
    ostatok = cash_calculator.get_today_cash_remained('euro')
    print(ostatok)

if __name__=='__main__':
    main()