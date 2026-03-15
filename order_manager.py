import datetime

# Database of orders (list of dictionaries)
orders = [
    {"client": "Libeň Car Service", "job": "Web Landing Page", "price": 4500},
    {"client": "Lion Bakery", "job": "Facebook Management", "price": 2000},
    {"client": "Marek the Plumber", "job": "Database Cleanup", "price": 3000},
    {"client": "YouTube Channel", "job": "Video Uploads", "price": 7000},
    {"client": "Fashion E-shop", "job": "SEO Optimization", "price": 3500 }
]

def create_report(order_list):
    today = datetime.date.today()
    file_name = f"income_report_{today}.txt"
    
    total_income = 0
    goal = 20000
    
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(f"--- FINANCIAL REPORT - DATE: {today} ---\n\n")
        
        for o in order_list:
            # Formatting: 20 characters for name and job to keep columns straight
            line = f"Client: {o['client']:20} | Job: {o['job']:20} | Price: {o['price']} CZK\n"
            f.write(line)
            total_income += o['price']
            
        f.write(f"\n" + "-"*60 + "\n")
        f.write(f"TOTAL POTENTIAL EARNINGS: {total_income} CZK\n")
        f.write(f"REMAINING TO GOAL ({goal} CZK): {goal - total_income} CZK\n")

    return file_name, total_income

# Running the program
file, amount = create_report(orders)
print(f"Success! Report generated in file: {file}")
print(f"Current project value: {amount} CZK.")
