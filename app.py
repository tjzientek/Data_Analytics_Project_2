# Import SQLAlchemy `automap` and other dependencies

import pandas as pd
import sqlite3

engine = create_engine("sqlite:///airport.db")
print("successful connection")

conn = sqlite3.connect("airport.db")

engine = create_engine("sqlite:///airport.db")
print("successful connection")

df1 = pd.read_sql("select * from airports", con=engine)
df1.head()

df2= df1[["Name", "IATA", "ICAO"]]
df2.head(10)

# Filter the data so that only those names with international airports are shown.

international_df2 = df2.loc[df1["Name"].str.contains("International"), :]

international_df2.head()