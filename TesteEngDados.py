import pandas as pd


orders1 = pd.read_csv('Retail_Data_Orders_Merge.csv')
orders2 = pd.read_csv('Retail_Data_W23_Merge.csv')
orders3 = pd.read_csv('Retail_Unlabeled_Data_Concat.csv')
merge = pd.read_csv('Store_Merge.csv')

all_orders = pd.concat([orders1, orders2, orders3])

final_orders = pd.merge(all_orders, merge, on='Store', how='left')

final_orders.to_csv('final_orders.csv', index=False)

print(final_orders)
