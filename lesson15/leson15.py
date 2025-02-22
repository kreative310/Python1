import pandas as pd
import matplotlib.pyplot as plt

w = pd.read_csv('weatherdata.csv')

avg_temperature = w.groupby('day')['temperature'].mean()

w['date'] = pd.to_datetime(w['date'])
w['month'] = w['date'].dt.month
w['day'] = w['date'].dt.day

temperatures_per_month = [group['temperature'].tolist() for _, group in w.groupby('month')]

average_temperatures = []
for month_temperatures in temperatures_per_month:
    average_temperature = sum(month_temperatures) / len(month_temperatures)
    average_temperatures.append(average_temperature)

for i, avg_temp in enumerate(average_temperatures, 1):
    print(f"Month {i}: Average Temperature = {avg_temp:.2f}°C")

for month_index, month_temperatures in enumerate(temperatures_per_month, 1):
    hottest_temp = max(month_temperatures)
    coldest_temp = min(month_temperatures)

plt.figure(figsize=(15,8))

filtered_df = w.groupby('month')['temperature'].mean().reset_index()
bars = plt.bar(filtered_df['month'], filtered_df['temperature'], color="black")

plt.title("Average temperature of each month", fontsize=16)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Temperature', fontsize=14)

plt.xticks(rotation=90, fontsize=12)
plt.yticks(fontsize=12)

plt.grid(axis='y', linestyle='--', alpha=0.8)

plt.bar_label(bars, fmt='%.2f', fontsize=12, color='black')

plt.tight_layout()

plt.show()
