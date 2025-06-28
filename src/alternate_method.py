import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering

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

# Hierarchical clustering

# Finding the optimal no of clusters using dendrogram
dendrogram = sch.dendrogram(sch.linkage(X, method='ward'))
plt.show()

# By examining the dendrogram, optimal number of clusters is 3
hc = AgglomerativeClustering(n_clusters=3, linkage='ward')
y_hc = hc.fit_predict(X)

# Inserting the cluster label to the product data frame
product_df['Cluster(Hierarchical)'] = y_hc


# Grouping by the hierarchical clusters
hm_cluster_summary = product_df.groupby('Cluster(Hierarchical)')[
    ['TotalQuantitySold', 'AvgUnitPrice', 'TransactionCount']].mean()
print("Hierarchical Cluster Summary:")
print(hm_cluster_summary)
