
def main():
    firm_name = input("Kérem adja meg a cég nevét: ")
    db = int(input("Értékesített termékek: "))
    netto_price = int(input("Nettó egységár: "))
    brutto_price = netto_price*1.27
    print(f"Bruttó egységár:{brutto_price}")
    netto_income=db*netto_price
    brutto_income=db*brutto_price
    print("nettó bevétel:{:.2f} bruttó bevétel:{:.2f}".format(netto_income, brutto_income))
    working_days = 20
    dailyIncome = brutto_income/working_days
    dailyDb = db/working_days
    print("Átlagos napi nettó bevétel:{:.2f}".format(netto_income/working_days))
    print("Átlagos napi bruttó bevétel:{:.2f}".format(dailyIncome))
    if (dailyIncome >= 100000):
        print("Emelésre nem volt szükség")
    else: 
        print("A megnövelt eladási ár: {:.2f}".format(100000/dailyDb))


main()