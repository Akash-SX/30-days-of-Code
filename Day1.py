def solve(meal_cost, tip_percent, tax_percent):
    tip =(tip_percent/100)*meal_cost
    tax=(tax_percent/100)*meal_cost
    total_cost =meal_cost+tip+tax
    return print(round(total_cost))

if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)
 
