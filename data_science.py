import csv
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from collections import Counter

# Read the CSV file
ev = pd.read_csv("ElectricCarData.csv")
print(ev.head(8))

# Filter data for Tesla cars
ev_tesla = ev[ev['Brand'].str.strip() == 'Tesla']
print(ev_tesla.reset_index())

# Print dataframe info
print(ev.info())

# Check for missing values
print(" ---------------------------------")
print(ev.isna().sum())

# Describe the dataset
print(ev.describe())

# Plot Acceleration vs Price
plot_Accel = ev["PriceEuro"]
plot_price = ev["Accel"]
plt.plot(plot_price, plot_Accel, linestyle=" ", marker="*")
plt.show()

# Ensure FastCharge and TopSpeed are numeric, handling non-numeric values
ev["FastCharge"] = pd.to_numeric(ev["FastCharge"], errors='coerce')
ev["TopSpeed"] = pd.to_numeric(ev["TopSpeed"], errors='coerce')

# Calculate 'Top' as battery life in hours and sort values
ev["Top"] = ev["FastCharge"] / ev["TopSpeed"]
ev_sorted = ev.sort_values(["Top"], ascending=False)

# Plot Efficiency vs Top
plot_eff = ev["Efficiency"]
plot_Top = ev["Top"]
plt.plot(plot_eff, plot_Top, linestyle=" ", marker=".")
plt.show()

# Unique Body Styles
print(ev["BodyStyle"].unique())

# Counter for BodyStyle, Brand, and PowerTrain
style_counter = Counter()
model_counter = Counter()
wheel_counter = Counter()

with open("ElectricCarData.csv") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        style_counter.update(row["BodyStyle"].split(" "))
        model_counter.update(row["Brand"].split(" "))
        wheel_counter.update(row["PowerTrain"].split("Drive"))

print(style_counter)
print(model_counter)
print(wheel_counter)
print(style_counter.most_common(5))

# Plot most common body styles
stylee = []
frequency = []
for item in style_counter.most_common(15):
    stylee.append(item[0])
    frequency.append(item[1])

plt.style.use("dark_background")
plt.barh(stylee, frequency, color="b")
plt.title("Most popular body style")
plt.ylabel("body style")
plt.xlabel("frequency")
plt.show()

stylee.reverse()
frequency.reverse()
plt.barh(stylee, frequency, color="c")
plt.show()

# Most common car brands
model_counter[""] = 0  # Handle empty brand names
print(model_counter)
print(model_counter.most_common(10))

model = []
frequencyy = []
for item in model_counter.most_common(15):
    model.append(item[0])
    frequencyy.append(item[1])

plt.style.use('Solarize_Light2')
plt.barh(model, frequencyy, color="k")
plt.title("Most popular Brand")
plt.ylabel("model")
plt.xlabel("frequency")
plt.show()

# Most common powertrain types
wheel = []
frequenccy = []
for item in wheel_counter.most_common(15):
    wheel.append(item[0])
    frequenccy.append(item[1])

del frequenccy[0]
del wheel[0]

print(wheel)
print(frequenccy)

plt.plot(wheel, frequenccy, color="k", linestyle="--", marker=" ", linewidth=2, label="Powertrain Types")
plt.title('Powertrain Type Frequency')
plt.xlabel('Powertrain Type')
plt.ylabel('Frequency')
plt.legend()
plt.grid(True)
plt.show()






