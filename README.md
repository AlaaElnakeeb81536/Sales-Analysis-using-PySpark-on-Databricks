# Sales Analysis using PySpark on Databricks

## Project Overview
This project leverages PySpark on Databricks to analyze sales data, uncovering valuable insights into customer behavior, product performance, and sales trends. The analysis helps identify high-value customers, popular products, seasonal patterns, and geographical sales distribution.

![Sales Dashboard](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/4026566508639073/3934584737389230/604712118645609/latest.html)

## Datasets
The analysis utilizes two primary datasets:

1. **Sales Transaction Dataset**:
   - Customer ID
   - Product ID
   - Order Date
   - Location (Country)
   - Source of Order (Restaurant, Online, Delivery)
   - Other transaction details

2. **Product Information Dataset**:
   - Product ID
   - Product Name
   - Product Category
   - Price
   - Other product attributes

## Key Analyses Performed

### Customer Insights
- **Total Amount Spent by Customer**: Identifies high-value customers
- **Visit Frequency**: Analyzes customer loyalty patterns

### Sales Trends
- **Monthly Sales Patterns**: Reveals seasonal trends
- **Yearly Sales Growth**: Tracks annual performance
- **Quarterly Sales Breakdown**: Identifies business cycles

### Product Analysis
- **Product Popularity**: Measures purchase frequency
- **Category Performance**: Compares sales across food categories

### Geographical Analysis
- **Country-wise Sales**: Identifies top-performing markets
- **Regional Preferences**: Reveals location-based trends

### Order Channel Analysis
- **Sales by Order Source**: Compares performance across channels (Restaurant, Online, Delivery)

## Technical Implementation
- **PySpark**: For large-scale data processing
- **Databricks**: Cloud-based platform for collaborative analytics
- **SQL & DataFrame API**: For flexible data manipulation
- **Visualization**: Built-in Databricks visualization tools

## Dashboard
The project includes an interactive dashboard that visualizes all key metrics:
- Customer value segmentation
- Sales trend charts
- Product performance heatmaps
- Geographical sales distribution
- Channel comparison metrics

[View Interactive Dashboard](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/4026566508639073/3934584737389230/604712118645609/latest.html)

## How to Run
1. Import the notebook into your Databricks workspace
2. Upload the sales and product datasets
3. Update the file paths in the first cell
4. Run all cells sequentially

## Requirements
- Databricks workspace
- PySpark 3.0+
- Python 3.7+
- Sample sales data in CSV format

## Insights Applied
The analysis helps:
- Optimize marketing spend
- Improve inventory planning
- Enhance customer segmentation
- Identify growth opportunities
- Evaluate channel effectiveness
