# Product Segmentation and Market Basket Analysis

While exploring customer segmentation with the UCI Online Retail dataset, I came across a research paper that applied RFM analysis to cluster customers. That sparked a question:

> 💡 "If we can segment customers to improve targeting, why not segment the **products** themselves to improve profit?"

This project flips the lens — instead of analyzing who is buying, we’re analyzing **what is being bought**.

---

## 🎯 Objective

- Segment products based on their sales behavior (price, quantity, volume)
- Discover co-purchased product combinations using association rule mining *(to be done)*

These insights can help businesses — especially those serving wholesale buyers — improve bundling, cross-selling, and inventory planning.

---

## 📄 Dataset Info

This project uses the Online Retail dataset from the UCI Machine Learning Repository.  
It contains transactions made by a UK-based online retailer over a one-year period, capturing detailed information about each item sold, when it was sold, and to which country.

- **Source**: [UCI Online Retail Data](https://archive.ics.uci.edu/ml/datasets/Online+Retail)  
- **Rows**: >500,000 transactions  
- **Period**: December 2010 – December 2011

| Column       | Description                              |
|--------------|------------------------------------------|
| InvoiceNo    | Transaction ID                           |
| StockCode    | Product/item ID                          |
| Description  | Product name                             |
| Quantity     | Number of items purchased                |
| InvoiceDate  | Date and time of transaction             |
| UnitPrice    | Price per item (in GBP)                  |
| CustomerID   | Unique customer identifier               |
| Country      | Country where the transaction occurred   |

---

## ⚙️ Approach (So Far)

We’ve completed the **Product Segmentation** phase of the project using clustering techniques.

### ✅ Steps Completed:

1. **Data Cleaning**  
   Removed null values, filtered invalid transactions.

2. **Feature Engineering**  
   Created product-level metrics:
   - `TotalQuantitySold`
   - `AvgUnitPrice`
   - `TransactionCount` (number of unique invoices per product)
   - `TotalRevenue` (used for EDA only)

3. **Feature Scaling**  
   Standardized the variables for clustering.

4. **Product Segmentation**  
   Applied **KMeans clustering** on the selected features to segment products into distinct behavioral groups.

5. **Exploratory Comparison**  
   Also ran **Hierarchical Clustering** as a supporting method. The clusters produced were consistent, validating the segmentation.

Next, we’ll derive insights from each segment and move on to **association rule mining** using the Apriori algorithm.

---

🔄 *README will be updated as the project progresses.*
