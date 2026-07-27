import pandas as pd
import sqlite3

# 1. Load the synthetic CSV you generated earlier
df = pd.read_csv("omnichannel_demand_inventory_data.csv")

# 2. Create a temporary in-memory SQLite database
conn = sqlite3.connect(":memory:")

# 3. Push the Pandas DataFrame into a SQL table named 'sales'
df.to_sql("sales", conn, index=False, if_exists="replace")

print("Data successfully loaded into SQLite!")