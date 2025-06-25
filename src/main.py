import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('../Data/Online_Retail.csv')
# Drop missing values
df = df.dropna(subset=['InvoiceNo', 'StockCode', 'Description', 'Quantity', 'InvoiceDate',
                       'UnitPrice', 'CustomerID', 'Country'])
# Convert invoiceDate to date-time formate
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], dayfirst=False)

# Creating Product-level feature set
product_df = df.groupby('StockCode').agg({
    'Description': 'first',
    'Quantity': 'sum',
    'UnitPrice': 'mean',
    'InvoiceNo': pd.Series.nunique
}).rename(columns={
    'InvoiceNo': 'TransactionCount',
    'Quantity': 'TotalQuantitySold',
    'UnitPrice': 'AvgUnitPrice'
})
# Adding the total revenue column for EDA
product_df['TotalRevenue'] = product_df['TotalQuantitySold'] * product_df['AvgUnitPrice']
# Reset index so StockCode becomes a regular column instead of an index
product_df = product_df.reset_index()

# Feature selection
X = product_df.iloc[:, [2, 3, 4]]

# Feature scaling
sc = StandardScaler()
X = sc.fit_transform(X)
