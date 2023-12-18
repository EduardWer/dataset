import pandas as pd
import numpy as np


data = pd.read_csv("Mall_Customers.csv") # конект к файлу

#print(data.head()) # выводит первые n строчки
#
#
# print(data.tail()) # выводит последнии n строчки
#
# print(data.info()) # выводит информацию про сsv
#print(data.columns) # выводит названия коллон в csv


data.to_numpy() # конверт в numpy объект

#print(data.describe()) #возвращает основные статистические показатели для каждого числового столбца


#print(data.nunique()) # одсчёт уникальных значений в каждом столбце


#print(data["CustomerID"].unique()) # возвращает уникальные значения в порядке как в столбце

#print(data.drop_duplicates())  # Удаление дубликатов

#print(data.sort_values(by="CustomerID")) # сортирока значений по столбцу CustomerID


#print(data["CustomerID"])  # Вывод CustomerID



#print(data[data["CustomerID"] > 20]) # вывод CustomerId  где значение больше 20


# print(data.shape) # выводит кортеж размерность масива

# print(data.drop(columns=["CustomerID"])) # Удаляет коллону CustomerID

#print(data.replace({"CustomerID":1},"xz")) # меняет значение customerID где  =1 на xz

#print(data.loc[0]) # вывод данный по меткам

#print(data.loc[[0,1,2],['CustomerID','Genre','Spending Score (1-100)']]) # вывод опред столбцов и сторок

#print(data.loc[data['Spending Score (1-100)'] == 39])


# print(data.loc[0,"Spending Score (1-100)"]) # выбор опред ячейки данных
#
# data.loc[0,"Genre"] = 'Male'

#print(data.values.tolist()) # преобразование в LIst

data.to_csv("data.csv",index=False) # Сохранение в лист