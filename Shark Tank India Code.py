import pandas as pd

# Load the Excel file into a pandas DataFrame
df = pd.read_excel('C://Users/HP/Documents/Shark Tank India Analysis/Shark_Tank_India.xlsx', sheet_name='Shark Tank India')

# Display the first few rows of the DataFrame
print(df.head())

# Display basic information
print("Dataset Info:")
print(df.info())

# Check for missing values
missing_values_count = df.isnull().sum()

# Get the data types of each column and store them in a variable
data_types = df.dtypes



########################### DATA TYPE CHANGE ################################
# Changing data types for each column
df = df.astype({
    'Season Number': 'int64',
    'Startup Name': 'string',
    'Episode Number': 'int64',
    'Pitch Number': 'int64',
    'Season Start': 'datetime64',
    'Season End': 'datetime64',
    'Original Air Date': 'datetime64',
    'Episode Title': 'string',
    'Anchor': 'string',
    'Industry': 'string',
    'Business Description': 'string',
    'Company Website': 'string',
    'Started in': 'int64',
    'Number of Presenters': 'int64',
    'Male Presenters': 'int64',
    'Female Presenters': 'int64',
    'Transgender Presenters': 'int64',
    'Couple Presenters': 'bool',
    'Pitchers Average Age': 'float64',
    'Pitchers City': 'string',
    'Pitchers State': 'string',
    'Yearly Revenue': 'float64',
    'Monthly Sales': 'float64',
    'Gross Margin': 'float64',
    'Net Margin': 'float64',
    'EBITDA': 'float64',
    'Cash Burn': 'float64',
    'SKUs': 'int64',
    'Has Patents': 'bool',
    'Bootstrapped': 'bool',
    'Original Ask Amount (Lakhs)': 'float64',
    'Original Offered Equity': 'float64',
    'Valuation Requested (Lakhs)': 'float64',
    'Received Offer': 'bool',
    'Accepted Offer': 'bool',
    'Total Deal Amount': 'float64',
    'Total Deal Equity': 'float64',
    'Total Deal Debt': 'float64',
    'Debt Interest': 'float64',
    'Deal Valuation': 'float64',
    'Number of Sharks in Deal': 'int64',
    'Deal Has Conditions': 'bool',
    'Royalty Deal': 'bool',
    'Advisory Shares Equity': 'float64',
    'Namita Investment Amount': 'float64',
    'Namita Investment Equity': 'float64',
    'Namita Debt Amount': 'float64',
    'Vineeta Investment Amount': 'float64',
    'Vineeta Investment Equity': 'float64',
    'Vineeta Debt Amount': 'float64',
    'Anupam Investment Amount': 'float64',
    'Anupam Investment Equity': 'float64',
    'Anupam Debt Amount': 'float64',
    'Aman Investment Amount': 'float64',
    'Aman Investment Equity': 'float64',
    'Aman Debt Amount': 'float64',
    'Peyush Investment Amount': 'float64',
    'Peyush Investment Equity': 'float64',
    'Peyush Debt Amount': 'float64',
    'Amit Investment Amount': 'float64',
    'Amit Investment Equity': 'float64',
    'Amit Debt Amount': 'float64',
    'Ashneer Investment Amount': 'float64',
    'Ashneer Investment Equity': 'float64',
    'Ashneer Debt Amount': 'float64',
    'Guest Investment Amount': 'float64',
    'Guest Investment Equity': 'float64',
    'Guest Debt Amount': 'float64',
    'Invested Guest Name': 'string',
    'All Guest Names': 'string',
    'Namita Present': 'bool',
    'Vineeta Present': 'bool',
    'Anupam Present': 'bool',
    'Aman Present': 'bool',
    'Peyush Present': 'bool',
    'Amit Present': 'bool',
    'Ashneer Present': 'bool',
    'Guest Present': 'bool'
})

# Verify changes
print(df.dtypes)

#####################
# Fill NaN values with 0 and then convert to integers
df[['Namita Present', 'Vineeta Present', 'Anupam Present', 'Aman Present', 
    'Peyush Present', 'Amit Present', 'Ashneer Present', 'Guest Present']] = df[[
    'Namita Present', 'Vineeta Present', 'Anupam Present', 'Aman Present', 
    'Peyush Present', 'Amit Present', 'Ashneer Present', 'Guest Present'
]].fillna(0).astype(int)

# Verify the changes
print(df[['Namita Present', 'Vineeta Present', 'Anupam Present', 'Aman Present', 
          'Peyush Present', 'Amit Present', 'Ashneer Present', 'Guest Present']].head())

#############################
# Fill NaN values with a placeholder and change data types to string
df['Invested Guest Name'] = df['Invested Guest Name'].fillna('Not Present').astype(str)
df['All Guest Names'] = df['All Guest Names'].fillna('None').astype(str)

# Verify the changes
print(df[['Invested Guest Name', 'All Guest Names']].head())

####################################
# Fill NaN values in the Startup Air Date column with a string placeholder
df['Original Air Date'] = df['Original Air Date'].fillna('Not Aired')

# Verify the changes
print(df['Original Air Date'].head())

################################
# Fill NaN values in the Company Website column with a placeholder text
df['Company Website'] = df['Company Website'].fillna('Not Available')

# Verify the changes
print(df['Company Website'].head())

######
# Convert the 'Started in' column to datetime, assuming January 1st as the default
df['Started in'] = pd.to_datetime(df['Started in'], format='%Y', errors='coerce')

####################################
# Fill 2021 where the Startup Name is 'Dorji'
df.loc[df['Startup Name'] == 'Dorji', 'Started in'] = 2021

# Verify the changes
print(df)

##############################
# Fill NaN values with 0 in the specified columns
df[['Male Presenters', 'Female Presenters', 'Transgender Presenters', 'Couple Presenters']] = df[['Male Presenters', 'Female Presenters', 'Transgender Presenters', 'Couple Presenters']].fillna(0)

# Verify the changes
print(df)

###########################
df[['Yearly Revenue', 'Monthly Sales', 'Gross Margin', 'Net Margin', 'EBITDA']] = df[['Yearly Revenue', 'Monthly Sales', 'Gross Margin', 'Net Margin', 'EBITDA']].fillna(0)

########################
df['Cash Burn'] = df['Cash Burn'].fillna("No")

######################
df['SKUs'] = df['SKUs'].fillna('Unknown')

##############
# Fill null values with -1 to indicate no offer was made
df['Accepted Offer'] = df['Accepted Offer'].fillna(-1)

#####################
df['Total Deal Amount'] = df['Total Deal Amount'].fillna(0)
df['Total Deal Equity'] = df['Total Deal Equity'].fillna(0)
df['Total Deal Debt'] = df['Total Deal Debt'].fillna(0)
df['Debt Interest'] = df['Debt Interest'].fillna(0)

# Filling missing values in 'Deal Valuation' and 'Number of Sharks in Deal'
df['Deal Valuation'] = df['Deal Valuation'].fillna("Not Disclosed")
df['Number of Sharks in Deal'] = df['Number of Sharks in Deal'].fillna(0)

# Save the modified dataset to a new CSV file
df.to_csv('C://Users/HP/Shark Tank India Analysis/Shark_Tank_India_Modified12.csv', index=False)

print("Dataset has been saved successfully!")