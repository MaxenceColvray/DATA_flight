import pandas as pd 

df = pd.read_csv("D:/Combined_Flights_2021.csv", sep=",")

df_min = df.sample(100000)


df_min = df_min[['FlightDate', 'Year', 'Month', 'DayOfWeek', 'Airline',
       'Origin', 'Dest', 'Cancelled', 'Diverted', 'CRSDepTime', 'DepTime',
       'DepDelayMinutes', 'DepDelay', 'CRSArrTime', 'ArrTime',
       'ArrDelayMinutes', 'ArrDelay', 'AirTime', 'Distance',
       'IATA_Code_Operating_Airline', 'Flight_Number_Operating_Airline',
       'Tail_Number', 'OriginStateName', 'DestStateName']]


df_min.to_csv("D:/Flights_data_2021.csv")

print(df_min)