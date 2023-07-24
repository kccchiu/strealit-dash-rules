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
        category = random.choice(["ABC", "BSD", "AbcDef"])
        if category == "ABC":
            rule = random.choice(["abc1_OS.csv", "weh.csv", "bcd_abc.csv"])
        elif category == "BSD":
            rule = random.choice(["efgh_1.csv", "asdasd_ab.csv", "bcd_qw.csv"])
        else:  # AbcDef
            rule = random.choice(["apple.csv", "abc2_def.csv", "99_Abc.csv"])

        roc_auc = round(random.uniform(0.5, 1.0), 4)
        pr_auc = round(random.uniform(0.5, 1.0), 4)
        data.append((category, rule, roc_auc, pr_auc, start_date.strftime("%Y-%m-%d")))
        start_date += timedelta(days=1)

    return pd.DataFrame(data, columns=['category', 'rule', 'roc_auc', 'pr_auc', 'train_date'])

# Function to save data to CSV file
def save_data_to_csv(data, category, rule):
    directory = f"data/{category}"
    if not os.path.exists(directory):
        os.makedirs(directory)

    file_path = f"{directory}/{rule}"
    data.to_csv(file_path, index=False)

if __name__ == "__main__":
    fake_data = generate_fake_data()
    for _, row in fake_data.iterrows():
        category, rule, roc_auc, pr_auc, train_date = row
        save_data_to_csv(fake_data[["roc_auc", "pr_auc", "train_date"]], category, rule)
