import pandas as pd

data = {
    'Drink_Name': [
        'Espresso', 'Americano', 'Latte', 'Cappuccino', 'Mocha',
        'Flat White', 'Macchiato', 'Cold Brew', 'Iced Latte', 'Chai Latte',
        'Matcha Latte', 'Cortado', 'Affogato', 'Irish Coffee', 'Nitro Cold Brew'
    ],
    'Base': [
        'Coffee', 'Coffee', 'Coffee', 'Coffee', 'Coffee',
        'Coffee', 'Coffee', 'Coffee', 'Coffee', 'Tea',
        'Tea', 'Coffee', 'Coffee', 'Coffee', 'Coffee'
    ],
    'Calories': [5, 15, 190, 120, 290, 170, 15, 5, 130, 240, 200, 25, 210, 210, 5],
    'Price_USD': [2.50, 3.25, 4.50, 4.25, 5.00, 4.50, 3.75, 4.00, 4.75, 4.50, 4.95, 3.50, 5.50, 7.00, 5.25],
    'Popularity_Score': [8, 7, 10, 9, 8, 7, 6, 9, 10, 8, 7, 6, 5, 4, 8]
}

custom_index = [f'MENU-{i:03d}' for i in range(1, 16)]
coffee_df = pd.DataFrame(data, index=custom_index)

print(coffee_df)
