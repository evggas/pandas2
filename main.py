import pandas as pd

data = {
    'Математика': [85, 78, 92, 68, 90, 76, 88, 95, 84, 73],
    'Физика': [79, 83, 91, 74, 88, 82, 85, 80, 89, 77],
    'Химия': [69, 72, 81, 65, 78, 74, 82, 85, 80, 77],
    'Биология': [82, 75, 89, 90, 85, 78, 88, 92, 84, 80],
    'История': [76, 85, 80, 82, 87, 79, 83, 90, 88, 74]
}

df = pd.DataFrame(data)

print("Первые строки DataFrame:")
print(df.head())

summary_stats = pd.DataFrame({
    'Средняя оценка': df.mean(),
    'Медиана': df.median(),
    'Q1': df.quantile(0.25),
    'Q3': df.quantile(0.75),
    'Стандартное отклонение': df.std()
})

print("\nОсновные статистики по предметам:")
print(summary_stats)

IQR_math = summary_stats.loc['Математика', 'Q3'] - summary_stats.loc['Математика', 'Q1']
print(f"\nIQR по математике: {IQR_math}")



