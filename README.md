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

## 🧠 Project Flow

We began by cleaning and preparing the data, removing records with missing values and converting date-related fields to the appropriate format. Instead of focusing on customer segmentation like the original paper, we aggregated data at the product level to understand each product’s performance over the year.

Next, we engineered key features: the total quantity sold, average unit price, and the number of transactions in which each product appeared. These features were chosen to reflect volume, value, and popularity.

After standardizing the features, we applied KMeans clustering to group products with similar sales patterns. Based on the elbow method, three distinct product clusters emerged.

Each cluster was then analyzed to understand its characteristics and business significance. We replaced numeric labels with interpretable names to communicate insights clearly.

---

## 🔍 Product Segments and Recommendations

| Segment Name                | Description                                                                 | Recommendation                                                                 |
|----------------------------|-----------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| Low Volume - Low Price     | Products that sell infrequently and generate low revenue                    | Bundle with popular items or phase out if no longer relevant                    |
| High Volume - Low Price    | Fast-moving, frequently purchased products that are essential to the catalog| Ensure consistent stock, consider discounts for bulk purchases                  |
| Moderate Volume - High Price| Premium items that sell moderately but contribute significantly to revenue  | Highlight in marketing campaigns and upsell to high-value customers            |

These segments help the business prioritize inventory, promotions, and marketing based on product behavior rather than just raw sales numbers.

---

## 📦 Output

The final product-level dataset with assigned cluster labels has been exported as:
[📄 clustered_product_data.csv](./Data/clustered_product_data.csv)

This serves as a foundation for the next phase of the project — Market Basket Analysis — which will uncover associations between products and improve cross-selling strategies.
