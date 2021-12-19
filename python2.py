import pandas as pd
data1 = pd.read_csv('C:\Users\admin\Downloads\Customer-Rating-System-Datasets\customer_info.csv')
data2 = pd.read_csv('C:\Users\admin\Downloads\Customer-Rating-System-Datasets\customer_account_info.csv ')
output1 = pd.merge(data1, data2,on='customer_key',how='inner')
output1.to_csv('file1.csv')
print(output1)
