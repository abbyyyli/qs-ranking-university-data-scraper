import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('first.csv',encoding='latin1')

# List of columns to add ranking columns for
columns_to_rank = [
    'Academic Reputation', 'Citations per Faculty', 'Faculty Student Ratio',
    'Employer Reputation', 'Employment Outcomes', 'International Student Ratio',
    'International Research Network', 'International Faculty Ratio', 'Sustainability Score'
]

# Add ranking columns
for col in columns_to_rank:
    ranking_col = f'Ranking on {col}'
    df[ranking_col] = df[col].rank(ascending=False, method='min')

# Replace NaN values with the least rank
for col in columns_to_rank:
    ranking_col = f'Ranking on {col}'
    df[ranking_col].fillna(df[ranking_col].max() + 1, inplace=True)


titles = [
    'Rank','University','Country','Overall Score',
    'Ranking on Academic Reputation','Academic Reputation',
    'Ranking on Citations per Faculty','Citations per Faculty',
    'Ranking on Faculty Student Ratio','Faculty Student Ratio',
    'Ranking on Employer Reputation','Employer Reputation',
    'Ranking on Employment Outcomes','Employment Outcomes',
    'Ranking on International Student Ratio','International Student Ratio',
    'Ranking on International Research Network','International Research Network',
    'Ranking on International Faculty Ratio','International Faculty Ratio',
    'Ranking on Sustainability Score','Sustainability Score'
]

#Reorder df
df = df[titles]

# Save the updated DataFrame to a new CSV file
df.to_csv('updated_file_2.csv', index=False)

print("DataFrame updated with ranking columns and saved to 'updated_file.csv'")