# Automobile Sales Recession Analysis

A comprehensive data analysis project examining the impact of economic recessions on automobile sales across different vehicle categories from 1980-2023.

## Project Overview

This project analyzes historical automobile sales data to understand how economic recessions affect consumer purchasing behavior in the automotive industry. The analysis includes interactive visualizations, statistical insights, and a web-based dashboard for exploring trends.

### Key Questions Addressed
- How do automobile sales differ between recession and non-recession periods?
- Which vehicle segments demonstrate resilience during economic downturns?
- How do advertising spend and pricing strategies influence sales under different economic conditions?
- What macroeconomic indicators (GDP, unemployment, consumer confidence) most strongly relate to sales performance?

## Key Findings

### Recession Impact
- **Sales drop by ~50%** during recession periods compared to normal times
- **Family and Super Mini cars** show the most resilience during downturns
- **Executive and Sports cars** experience the largest percentage decline (>50% drop)

### Strategic Insights
- Companies allocate only **17.3% of advertising budget** during recessions
- **70% of recession ad spend** focuses on affordable vehicle segments (Family & Super Mini)
- **Negative correlation** between vehicle price and sales volume during recessions
- **Unemployment rate** inversely correlates with sales across all vehicle types

## Technologies Used

- **Python 3.x**
- **Data Analysis**: Pandas, NumPy
- **Visualization**: Matplotlib, Seaborn, Plotly
- **Interactive Dashboard**: Dash
- **Data Processing**: CSV data manipulation

## Project Structure

```
Automobile-Sales-Recession-Analysis/
│
├── data/
│   └── automobile_sales.csv          # Historical sales data (1980-2023)
│
├── notebooks/
│   └── recession_analysis.ipynb       # Jupyter notebook with analysis
│
├── dashboard/
│   └── app.py                         # Interactive Dash dashboard
│
└── README.md                          # This file
```

## Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/alinazir105/Automobile-Sales-Recession-Analysis.git
   cd Automobile-Sales-Recession-Analysis
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Analysis

#### Jupyter Notebook
```bash
jupyter notebook notebooks/recession_analysis.ipynb
```

#### Interactive Dashboard
```bash
cd dashboard
python app.py
```
Then open your browser to `http://127.0.0.1:8050`

## Dashboard Features

The interactive dashboard provides:

- **Yearly Statistics View**
  - Overall sales trends (1980-2023)
  - Monthly sales breakdown by selected year
  - Vehicle type performance analysis
  - Advertising expenditure distribution

- **Recession Period Statistics View**
  - Sales trends during recession periods
  - Vehicle type resilience analysis
  - Advertising strategy during downturns
  - Unemployment impact on sales

## Dataset Description

The dataset contains historical automobile sales data enriched with macroeconomic indicators:

- **Date**: Month-end date of observation
- **Recession**: Binary indicator (1 = recession, 0 = normal)
- **Automobile_Sales**: Number of vehicles sold
- **GDP**: Per capita GDP value (USD)
- **Unemployment_Rate**: Monthly unemployment rate
- **Consumer_Confidence**: Consumer confidence index
- **Seasonality_Weight**: Seasonal effect on sales
- **Price**: Average vehicle price
- **Advertising_Expenditure**: Company advertising spend
- **Vehicle_Type**: Type of vehicle (SuperMiniCar, SmallFamilyCar, MediumFamilyCar, ExecutiveCar, Sports)
- **Competition**: Market competition measure

## Analysis Highlights

### 11 Comprehensive Visualizations
1. Yearly trend in average automobile sales (1980-2023)
2. Sales vs. advertising expenditure (non-recession)
3. Average sales comparison (recession vs. non-recession)
4. Vehicle-wise sales analysis
5. GDP trends during different economic periods
6. Seasonality impact on sales
7. Consumer confidence vs. sales (recession)
8. Vehicle price vs. sales relationship
9. Advertising expenditure proportions
10. Vehicle type advertising allocation
11. Unemployment rate impact on sales

## 🎓 Skills Demonstrated

- **Data Analysis**: Exploratory data analysis, statistical analysis
- **Data Visualization**: Static and interactive visualizations
- **Web Development**: Interactive dashboard creation
- **Business Intelligence**: Translating data into actionable insights
- **Python Programming**: Data manipulation, visualization, web apps

## Future Improvements

- [ ] Add predictive modeling (time series forecasting)
- [ ] Implement machine learning models for sales prediction
- [ ] Add correlation analysis and statistical tests
- [ ] Deploy dashboard to cloud platform
- [ ] Add data export functionality
- [ ] Include more advanced visualizations (heatmaps, correlation matrices)
- [ ] Add user authentication for dashboard
- [ ] Implement real-time data updates

## Author

**Ali Nazir**
- GitHub: [@alinazir105](https://github.com/alinazir105)


## Acknowledgments

- Dataset provided for educational purposes
- Economic recession data based on historical records

---

**Note**: This project is for educational and portfolio purposes. The insights provided are based on the dataset analysis and should be validated with additional data sources for real-world applications.

