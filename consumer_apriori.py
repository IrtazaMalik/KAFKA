from collections import defaultdict
from itertools import combinations

# Initialize parameters
min_support = 0.1  # Minimum support threshold
window_size = 1000  # Fixed-size window
window_data = []

# Function to find frequent itemsets using Apriori algorithm
def find_frequent_itemsets(data):
    item_counts = defaultdict(int)
    for transaction in data:
        for item in transaction:
            item_counts[item] += 1

    frequent_itemsets = []
    for item, count in item_counts.items():
        support = count / len(data)
        if support >= min_support:
            frequent_itemsets.append({item})
    
    return frequent_itemsets

# Function to generate candidate itemsets
def generate_candidates(prev_itemsets, k):
    candidates = set()
    for itemset1 in prev_itemsets:
        for itemset2 in prev_itemsets:
            union_set = itemset1.union(itemset2)
            if len(union_set) == k:
                candidates.add(frozenset(union_set))
    return candidates

# Sliding window approach
for i, transaction in enumerate(transactions_stream):
    window_data.append(transaction)
    if len(window_data) >= window_size:
        frequent_itemsets = find_frequent_itemsets(window_data)
        print(f"Window {i+1}: Frequent Itemsets - {frequent_itemsets}")

        # Generate candidate itemsets for next iteration
        k = len(frequent_itemsets[0]) + 1
        candidates = generate_candidates(frequent_itemsets, k)

        # Update window data by removing oldest transactions
        window_data = window_data[window_size // 2:]

# Process remaining data in the last window
if window_data:
    frequent_itemsets = find_frequent_itemsets(window_data)
    print(f"Final Window: Frequent Itemsets - {frequent_itemsets}")
