def a(x):
    if x <= 1200:
        y = 0.06
    elif x <= 4600:
        y = 0.15
    elif x <= 8800:
        y = 0.24
    elif x <= 15000:
        y = 0.35
    elif x <= 30000:
        y = 0.38
    elif x <= 50000:
        y = 0.4
    else:
        y = 0.42
    
    z=x*y
    return z

def main():
    monthly_payment=300
    yearly_salary=int(monthly_payment*12)
    b=int(a(yearly_salary))
    i=yearly_salary-b

    print(f"세전 연봉: {yearly_salary}만원")
    print(f"세후 연봉: {i}만원")

if __name__ == "__main__":
    main()
