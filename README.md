# Product Segmentation in Retail Using KMeans Clustering

While exploring customer segmentation with the UCI Online Retail dataset, I came across a research paper that applied RFM analysis to cluster customers. That sparked a question:

> "If we can segment customers to improve targeting, why not segment the **products** themselves to improve profitability?"

This project flips the lens — instead of analyzing who is buying, we analyze **what is being bought**.

---

## Objective

The primary objective of this project is to **segment products based on their sales behavior** using unsupervised learning.  
By grouping products with similar pricing, sales volume, and purchase frequency, the project aims to support better:

- Inventory planning  
- Pricing and promotion strategies  
- Product-level decision-making  

---

## Dataset Info

This project uses the **Online Retail** dataset from the UCI Machine Learning Repository.  
It contains transactional data from a UK-based online retailer over a one-year period.

- **Source**: https://archive.ics.uci.edu/ml/datasets/Online+Retail  
- **Rows**: Over 500,000 transactions  
- **Period**: December 2010 – December 2011  
- **Currency**: GBP  

| Column       | Description                              |
|--------------|------------------------------------------|
| InvoiceNo    | Transaction ID                           |
| StockCode    | Product/item ID                          |
| Description  | Product name                             |
| Quantity     | Number of items purchased                |
| InvoiceDate  | Date and time of transaction             |
| UnitPrice    | Price per item (GBP)                     |
| CustomerID   | Unique customer identifier               |
| Country      | Country where the transaction occurred   |

---

## Project Flow

The analysis begins with data cleaning and preprocessing, including handling missing values and converting date-related fields to appropriate formats.  
Instead of performing customer-level analysis, the data is aggregated at the **product level** to evaluate each product’s overall sales performance.

Key features are then engineered for each product, including:
- Total quantity sold  
- Average unit price  
- Number of transactions  

These features were selected to capture product volume, value, and popularity.

After standardizing the features, **KMeans clustering** is applied to segment products with similar sales behavior.  
The elbow method is used to determine the optimal number of clusters, resulting in three distinct product segments.

Finally, each cluster is analyzed and assigned an interpretable label to clearly communicate its business significance.

---

## Product Segments and Recommendations

| Segment Name                 | Description                                                   | Recommendation                                               |
|------------------------------|---------------------------------------------------------------|--------------------------------------------------------------|
| Low Volume - Low Price       | Products with low demand and low revenue contribution         | Bundle with popular products or evaluate for discontinuation |
| High Volume - Low Price      | Fast-moving, frequently purchased products                    | Ensure consistent stock and optimize bulk pricing strategies |
| Moderate Volume - High Price | Premium products with lower frequency but high per-unit value | Promote through targeted marketing and premium positioning   |

This segmentation highlights the natural imbalance in retail catalogs, where a large number of low-value products coexist with a smaller set of high-impact items. The clusters enable differentiated strategies rather than one-size-fits-all decisions.

---

## Output

The final product-level dataset with cluster labels is available here:

[clustered_product_data.csv](./Data/clustered_product_data.csv)

This dataset can be directly used for downstream analysis such as pricing optimization, catalog restructuring, or recommendation strategy development.

---

## Future Work

Potential extensions of this project include applying **market basket analysis** to identify frequently co-purchased products and exploring how different product segments interact within transactions.
