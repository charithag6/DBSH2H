import pandas as pd
data = pd.read_csv('C:\Users\admin\Downloads\Customer-Rating-System-Datasets\customer_transcations.csv')
arr = data["Account_Key"].unique()
from csv import writer
List1=[]
List2=[]
for acc in arr:
    l=[data[i] for i in range(len(data)) if acc==data[i]["Account_Key"]]
    List1.append(acc)
    inn=[l[i]["Transaction_Amount(in $)"] for i in range(len(l)) if l[i]["Transaction Type"]="INN"]
    
    outt=[l[i]["Transaction_Amount(in $)"] for i in range(len(l)) if l[i]["Transaction Type"]="OUT"]
    IN=sum(inn)
    OUT=sum(outt)
    if(IN>1000 or OUT>800 or (len(inn)+len(outt))>20):
        List2.append("High")
        print("high")
    elif((IN>600 && IN<1000)or(OUT>500 && OUT<800)or(((len(inn)+len(outt))>10 && (len(inn)+len(outt))<20))):
        List2.append("Mid")
        print("mid")
    else:
        List2.append("Low")
        print("low")
with open('C:\Users\admin\Downloads\Customer-Rating-System-Datasets\customer_account_info.csv', 'a') as f_object:
	writer_object = writer(f_object)
	writer_object.writerow(List1)
with open('C:\Users\admin\Downloads\Customer-Rating-System-Datasets\customer_account_info.csv', 'a') as f_object:
	writer_object = writer(f_object)
	writer_object.writerow(List2)
print(data)
