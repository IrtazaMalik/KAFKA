from collections import defaultdict
from itertools import combinations

# Initialize parameters
min_support = 0.1  # Minimum support threshold
bucket_size = 10  # Number of buckets in hash table
hash_table = [0] * bucket_size
window_size = 1000  # Fixed-size window
window_data = []

# Function to hash items and update hash table
def hash_item(item):
    return hash(item) % bucket_size

# Function to find frequent itemsets using PCY algorithm
def find_frequent_itemsets(data):
    item_counts = defaultdict(int)
    for transaction in data:
        for item in transaction:
            item_counts[item] += 1

    # Count item pairs in buckets
    bucket_counts = defaultdict(int)
    for transaction in data:
        items = sorted(transaction)
        for i, item1 in enumerate(items):
            hash1 = hash_item(item1)
            for item2 in items[i + 1:]:
                hash2 = hash_item(item2)
                if hash_table[hash1] > 0 and hash_table[hash2] > 0:
                    bucket_index = hash1 ^ hash2
                    bucket_counts[bucket_index] += 1

    # Filter frequent itemsets based on support
    frequent_itemsets = []
    for item, count in item_counts.items():
        support = count / len(data)
        if support >= min_support:
            frequent_itemsets.append({item})
    
    return frequent_itemsets

# Sliding window approach
for i, transaction in enumerate(transactions_stream):
    window_data.append(transaction)
    if len(window_data) >= window_size:
        # Update hash table
        for transaction in window_data:
            for item in transaction:
                hash_table[hash_item(item)] += 1

        # Find frequent itemsets using PCY algorithm
        frequent_itemsets = find_frequent_itemsets(window_data)
        print(f"Window {i+1}: Frequent Itemsets - {frequent_itemsets}")

        # Update window data by removing oldest transactions
        window_data = window_data[window_size // 2:]

# Process remaining data in the last window
if window_data:
    for transaction in window_data:
        for item in transaction:
            hash_table[hash_item(item)] += 1
    frequent_itemsets = find_frequent_itemsets(window_data)
    print(f"Final Window: Frequent Itemsets - {frequent_itemsets}")
