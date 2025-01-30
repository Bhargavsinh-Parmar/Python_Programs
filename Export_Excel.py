import pandas as pd

# Data for the projected cash flow statement
excel_file_data = {
    "Year": ["Year 1", "Year 2", "Year 3", "Year 4", "Year 5"],
    "Net Income (INR)": [300000, 600000, 900000, 1441500, 2019450],
    "Add: Depreciation (INR)": [500000, 500000, 500000, 500000, 500000],
    "Net Cash from Operating Activities (INR)": [800000, 1100000, 1400000, 1941500, 2519450],
    "Capital Expenditures (INR)": [-1000000, -1000000, -1000000, -1000000, -1000000],
    "Net Cash from Investing Activities (INR)": [-1000000, -1000000, -1000000, -1000000, -1000000],
    "Net Cash from Financing Activities (INR)": [0, 0, 0, 0, 0],
    "Net Increase/(Decrease) in Cash (INR)": [-200000, 100000, 400000, 941500, 1519450],
    "Opening Cash Balance (INR)": [0, -200000, -100000, 300000, 1241500],
    "Closing Cash Balance (INR)": [-200000, -100000, 300000, 1241500, 2760950]
}

# Create DataFrame
excel_file_df = pd.DataFrame(excel_file_data)

# Save to Excel
excel_file_file_path = "E:\Projected_Cash_Flow_Statement.xlsx"
excel_file_df.to_excel(excel_file_file_path, index=False)

excel_file_file_path
