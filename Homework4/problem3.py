import numpy as np
import pandas as pd
from enum import Enum
from collections import Counter

instance = np.arange(1,9)

class Price(Enum):
    low = 1
    average = 2
    high = 3
price = [Price.high, Price.high, Price.low, Price.high, Price.average, Price.high, Price.average, Price.low]

class Quality(Enum):
    ok = 1
    excellent = 2
quality = [Quality.ok, Quality.excellent, Quality.ok, Quality.excellent, Quality.excellent, Quality.ok, Quality.excellent, Quality.excellent]

class Size(Enum):
    small = 1
    median = 2
    large = 3
size = [Size.large, Size.median, Size.median, Size.small, Size.median, Size.small, Size.large, Size.median]

class Purchase(Enum):
    yes = 1
    no = 2
purchase = [Purchase.no, Purchase.yes, Purchase.yes, Purchase.yes, Purchase.no, Purchase.no, Purchase.yes, Purchase.yes]

df = pd.DataFrame({
    "instance": instance,
    "price": [p.name for p in price],
    "quality": [q.name for q in quality],
    "size": [s.name for s in size],
    "purchase": [p.name for p in purchase]
})
#print(df)

"""
for col in df.columns:
    if col == "instance": continue
    if col.value_counts() >= minimum_value_count:
        print(df[col].value_counts())
price

high       4
low        2
average    2

quality

excellent    5
ok           3


size

median    4
large     2
small     2
Name: count, dtype: int64

purchase

yes    5
no     3
Name: count, dtype: int64

"""


#all_counts = df.drop(columns="instance").stack().value_counts()
#filtered = all_counts[all_counts >= minimum_value_count]
#print(filtered)

"""
excellent    5
yes          5
high         4
median       4
ok           3
no           3
"""

#global order is [purchase=yes, quality=excellent, price=high, size=median, quality=ok, purchase=no]




transactions = []
for _, row in df.drop(columns="instance").iterrows():
    transaction = [f"{col}={row[col]}" for col in df.columns if col != "instance"]
    transactions.append(transaction)
#Now every transaction is a transaction
#print(transactions)

#Now I have all of the item counts
minimum_value_count = 3
item_counts = Counter(item for transaction in transactions for item in transaction)

frequent_items = {
    item: count for item, count in item_counts.items()
    if count >= minimum_value_count
}

#print(frequent_items)

global_order = sorted(frequent_items.keys(), key=lambda item: (-frequent_items[item], item))
ranking = {item: i for i, item in enumerate(global_order)}

#print(global_order)
#print(ranking)

sorted_transactions = []
for transaction in transactions:
    #Item in the transacttion stays if it's there
    filtered = [item for item in transaction if item in frequent_items]
    filtered.sort(key=lambda item: ranking[item])
    sorted_transactions.append(filtered)

print("Filtered and sorted transactions:")
for i, t in enumerate(sorted_transactions, start=1):
    print(f"T{i}: {t}")
print()

"""
Filtered and sorted transactions:
T1: ['price=high', 'purchase=no', 'quality=ok']
T2: ['purchase=yes', 'quality=excellent', 'price=high', 'size=median']
T3: ['purchase=yes', 'size=median', 'quality=ok']
T4: ['purchase=yes', 'quality=excellent', 'price=high']
T5: ['quality=excellent', 'size=median', 'purchase=no']
T6: ['price=high', 'purchase=no', 'quality=ok']
T7: ['purchase=yes', 'quality=excellent']
T8: ['purchase=yes', 'quality=excellent', 'size=median']
"""

# Step 6: FP-tree classes and functions
class FPNode:
    #Each node is going to have an item(the transaction category), count of when it's seen, a possible parent or child node
    def __init__(self, item, count=1, parent=None):
        self.item = item
        self.count = count
        self.parent = parent
        self.children = {}

    def display(self, level=0):
        indent = "  " * level
        print(f"{indent}{self.item}: {self.count}")
        for child in self.children.values():
            child.display(level + 1)


def insert_transaction(transaction, root):
    current = root
    for item in transaction:
        if item in current.children:
            current.children[item].count += 1
        else:
            current.children[item] = FPNode(item=item, count=1, parent=current)
        current = current.children[item]


# Build the tree
root = FPNode("ROOT", count=0)

for transaction in sorted_transactions:
    if transaction:
        insert_transaction(transaction, root)

print("FP-tree:")
root.display()