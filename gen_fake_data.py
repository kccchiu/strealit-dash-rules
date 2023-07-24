import os
import pandas as pd
from datetime import datetime, timedelta
import random

# Function to generate fake data
def generate_fake_data():
    data = []
    start_date = datetime(2023, 6, 1)
    end_date = datetime(2023, 8, 31)

    while start_date <= end_date:
        roc_auc = round(random.uniform(0.5, 1.0), 4)
        pr_auc = round(random.uniform(0.5, 1.0), 4)
        data.append((roc_auc, pr_auc, start_date.strftime("%Y-%m-%d")))
        start_date += timedelta(days=1)

    return pd.DataFrame(data, columns=['roc_auc', 'pr_auc', 'train_date'])

# Function to save data to CSV file
def save_data_to_csv(data, category, rule):
    directory = f"{category}"
    if not os.path.exists(directory):
        os.makedirs(directory)

    file_path = f"{directory}/cat{category}_rule{rule}.csv"
    data.to_csv(file_path, index=False)

if __name__ == "__main__":
    categories = ["A", "B", "C"]
    rules = {
        "A": [1, 2, 3, 45],
        "B": [24, 45,52],
        "C": [123,12,42]
    }

    for category in categories:
        for rule in rules[category]:
            fake_data = generate_fake_data()
            save_data_to_csv(fake_data, category, rule)

            print(f"Fake data for Category {category}, Rule {rule} has been generated and saved.")
