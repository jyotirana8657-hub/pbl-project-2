import matplotlib.pyplot as plt

# Lists to store data
products = []
sales = []
costs = []
profits = []

# User Input
n = int(input("Enter number of products: "))

for i in range(n):
    print(f"\nEnter details for Product {i+1}")
    
    name = input("Product Name: ")
    sale = float(input("Enter Sale Amount: "))
    cost = float(input("Enter Cost Amount: "))
    
    profit = sale - cost
    
    products.append(name)
    sales.append(sale)
    costs.append(cost)
    profits.append(profit)

# Calculations
total_sales = sum(sales)
average_sales = total_sales / n
total_profit = sum(profits)

# Display Result
print("\n----- SALES ANALYSIS REPORT -----")
print("Total Sales:", total_sales)
print("Average Sales:", average_sales)

if total_profit > 0:
    print("Overall Profit:", total_profit)
elif total_profit < 0:
    print("Overall Loss:", total_profit)
else:
    print("No Profit No Loss")

# Create Bar Chart
plt.bar(products, sales)
plt.xlabel("Products")
plt.ylabel("Sales Amount")
plt.title("Product Sales Analysis")

# Save chart image
plt.savefig("sales_chart.png")
plt.close()

# Create HTML Report
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Sales Data Analysis Report</title>
    <style>
        body {{
            font-family: Arial;
            background-color: #f4f4f4;
            padding: 20px;
        }}

        h1 {{
            color: darkblue;
        }}

        table {{
            width: 80%;
            border-collapse: collapse;
            background-color: white;
        }}

        th, td {{
            border: 1px solid black;
            padding: 10px;
            text-align: center;
        }}

        th {{
            background-color: lightblue;
        }}

        img {{
            width: 600px;
            margin-top: 20px;
        }}
    </style>
</head>

<body>

<h1>Sales Data Analysis Report</h1>

<h2>Summary</h2>

<p><b>Total Sales:</b> {total_sales}</p>
<p><b>Average Sales:</b> {average_sales}</p>
<p><b>Total Profit/Loss:</b> {total_profit}</p>

<h2>Product Details</h2>

<table>
<tr>
    <th>Product</th>
    <th>Sales</th>
    <th>Cost</th>
    <th>Profit/Loss</th>
</tr>
"""

# Add rows in HTML table
for i in range(n):
    html_content += f"""
<tr>
    <td>{products[i]}</td>
    <td>{sales[i]}</td>
    <td>{costs[i]}</td>
    <td>{profits[i]}</td>
</tr>
"""

# Finish HTML
html_content += """
</table>

<h2>Sales Chart</h2>
<img src="sales_chart.png" alt="Sales Chart">

</body>
</html>
"""

# Save HTML file
with open("sales_report.html", "w") as file:
    file.write(html_content)

print("\nHTML Report Generated Successfully!")
print("Open 'sales_report.html' in your browser.")