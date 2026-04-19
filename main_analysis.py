import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = {
    'MFI_Name': ['Chhimek', 'Nirdhan', 'Swabalamban', 'Sana Kisan', 'Forward', 
                 'Deprosc', 'Jeevan Bikas', 'NIC Asia MF', 'First Micro', 'Nerude'],
    'Net_Loan_Cr': [2800, 2650, 1950, 3200, 1450, 1700, 2100, 1300, 950, 1100],
    'Net_Profit_Cr': [95, 88, 62, 110, 45, 58, 75, 30, 25, 40],
    'Dividend_Percent': [25, 20, 15, 27, 10, 12, 22, 5, 10, 8]
}
df = pd.DataFrame(data)
print(df)


# 2. Sort by Loan (Highest to Lowest) for a professional look

df = df.sort_values(by='Net_Loan_Cr', ascending=False)

# 3. Create the Bar Chart

plt.figure(figsize=(12, 6))
loan_plot = sns.barplot(x='MFI_Name', y='Net_Loan_Cr', data=df, palette='viridis')

# 4. Add Titles and Labels

plt.title('Nepal Microfinance Institutions: Loan Portfolio Position', fontsize=14)
plt.xlabel('Microfinance Name', fontsize=12)
plt.ylabel('Total Loan (in Crore)', fontsize=12)

# 5. Add Data Labels (Numbers) on top of each bar

for p in loan_plot.patches:
    loan_plot.annotate(format(p.get_height(), '.0f'), 
                       (p.get_x() + p.get_width() / 2., p.get_height()), 
                       ha='center', va='center', 
                       xytext=(0, 9), 
                       textcoords='offset points')

# 6. Clean up and Show
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('mfi_loan_position.png', dpi=300, bbox_inches='tight')
# Average Dividend calculate garne (Benchmark ko lagi)
avg_dividend = df['Dividend_Percent'].mean()

# # --- FIGURE 1: BAR CHART (Comparison) ---
plt.figure(figsize=(12, 6))
# Dividend mathi bhayeka lai 'Green' ra muni bhayeka lai 'Red' dekhaune logic
colors = ['green' if x >= avg_dividend else 'red' for x in df['Dividend_Percent']]

sns.barplot(x='MFI_Name', y='Dividend_Percent', data=df, palette=colors)
plt.axhline(avg_dividend, color='blue', linestyle='--', label=f'Average ({avg_dividend}%)')

plt.title('Investment Analysis: Good vs Risky Dividend (Green = Above Avg)')
plt.xticks(rotation=45)
plt.legend()
plt.savefig('dividend_bar_chart.png', dpi=300)
plt.show()

# --- FIGURE 2: HISTOGRAM (Distribution) ---
plt.figure(figsize=(10, 6))
sns.histplot(df['Dividend_Percent'], bins=5, kde=True, color='purple')

plt.title('Dividend Distribution (How many MFIs give what range?)')
plt.xlabel('Dividend Percentage Range')
plt.ylabel('Number of Microfinances')
plt.savefig('dividend_histogram.png', dpi=300)
plt.show()




