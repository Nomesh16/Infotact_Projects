# EchoChain - Circular Economy & Secondary Market Lifecycle Analytics

## Problem Statement
Manufacturers track products rigorously until the point of sale. Post-sale, the product's lifecycle becomes a data blind spot, making it impossible to measure environmental impact, landfill diversion, or refurbishment potential.

## Solution
EchoChain scrapes secondary market data (like eBay) and joins it with internal manufacturing Bills of Materials (BOM) to reveal a "Circularity Score" for products, helping identify buy-back and refurbishment opportunities.

## Tech Stack
- **Data Processing:** Python, Pandas, PySpark
- **Fuzzy Matching:** fuzzywuzzy
- **Visualization:** Microsoft PowerBI
- **Data Source:** Mock secondary market and manufacturing dataset (20,000 rows)

## Key Features
- Data cleaning and quality validation
- PySpark-based aggregation and analysis
- Fuzzy title matching between scraped listings and internal SKUs
- Executive PowerBI dashboard with:
  - Average Circularity Score by Product Model
  - Refurbishment Cost by Brand
  - Buyback Recommendation breakdown
  - CO2 Reduction by Brand
  - Key KPI cards (Avg Circularity Score, Avg Depreciation, Total Refurbishment Profit)

## Files
- `EchoChain_20000.csv` - Mock dataset
- `EchoChain_Dashboard.pbix` - PowerBI dashboard
- `mock_scraper/` - Python scripts (data cleaning, PySpark, fuzzy matching)
