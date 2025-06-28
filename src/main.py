import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

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
X = product_df.iloc[:, ['TotalQuantitySold', 'AvgUnitPrice', 'TransactionCount']]

# Feature scaling
sc = StandardScaler()
X = sc.fit_transform(X)

# KMeans clustering

# Finding the optimal no of clusters
wcss = []
for i in range(1, 11):
    km = KMeans(n_clusters=i, init='k-means++', random_state=0)
    km.fit(X)
    wcss.append(km.inertia_)
plt.plot(range(1, 11), wcss)
plt.xlabel('No. of clusters')
plt.ylabel('WCSS')
plt.show()

# By elbow method, optimal number of clusters is 3
km = KMeans(n_clusters=3, init='k-means++', random_state=0)
y_kmeans = km.fit_predict(X)

# Inserting the cluster label to the product data frame
product_df['Cluster(KMeans)'] = y_kmeans


# Grouping by the kmeans clusters
km_cluster_summary = product_df.groupby('Cluster(KMeans)')[[
    'TotalQuantitySold', 'AvgUnitPrice', 'TransactionCount']].mean()
print("KMeans Cluster Summary:")
print(km_cluster_summary)
