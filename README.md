# Product Segmentation and Market Basket Analysis

While exploring customer segmentation with the UCI Online Retail dataset, I came across a research paper that applied RFM analysis to cluster customers. That sparked a question:

> 💡 "If we can segment customers to improve targeting, why not segment the **products** themselves to improve profit?"

This project flips the lens — instead of analyzing who is buying, we’re analyzing **what is being bought**.

---

## 🎯 Objective

- Segment products based on their sales behavior (price, quantity, volume)
- Discover co-purchased product combinations using association rule mining

These insights can help businesses — especially those serving wholesale buyers — improve bundling, cross-selling, and inventory planning.

---

## 📄 Dataset Info
This project uses the Online Retail dataset from the UCI Machine Learning Repository.  
It contains transactions made by a UK-based online retailer over a one-year period, capturing detailed information about each item sold, when it was sold, and to which country.

- **Source**: [UCI Online Retail Data](https://archive.ics.uci.edu/ml/datasets/Online+Retail)  
- **Rows**: >500,000 transactions  
- **Period**: December 2010 – December 2011

| Column       | Description                          |
|--------------|--------------------------------------|
| InvoiceNo    | Transaction ID                       |
| StockCode    | Product/item ID                      |
| Description  | Product name                         |
| Quantity     | Number of items purchased            |
| InvoiceDate  | Date and time of transaction         |
| UnitPrice    | Price per item (in GBP)              |
| CustomerID   | Unique customer identifier           |
| Country      | Country where the transaction occurred |
