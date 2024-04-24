from collections import defaultdict
from itertools import combinations

# Initialize parameters
min_support = 0.1  # Minimum support threshold
window_size = 1000  # Fixed-size window
window_data = []
frequent_itemsets = []

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

# Function to prune infrequent itemsets
def prune_itemsets(candidate_itemsets, frequent_itemsets):
    pruned_candidates = []
    for candidate in candidate_itemsets:
        subsets = combinations(candidate, len(candidate) - 1)
        if all(frozenset(subset) in frequent_itemsets for subset in subsets):
            pruned_candidates.append(candidate)
    return pruned_candidates

# Process streaming data
for i, transaction in enumerate(transactions_stream):
    window_data.append(transaction)
    
    # Remove oldest transactions if window size exceeded
    if len(window_data) > window_size:
        window_data.pop(0)
    
    # Find frequent itemsets using Apriori algorithm
    frequent_itemsets = find_frequent_itemsets(window_data)
    
    # Generate candidate itemsets for next iteration
    if len(frequent_itemsets) > 1:
        k = len(frequent_itemsets[0]) + 1
        candidate_itemsets = generate_candidates(frequent_itemsets, k)
        pruned_candidates = prune_itemsets(candidate_itemsets, frequent_itemsets)
        frequent_itemsets.extend(pruned_candidates)
    
    # Print frequent itemsets for each window
    print(f"Window {i+1}: Frequent Itemsets - {frequent_itemsets}")

# Print frequent itemsets for the final window
print(f"Final Window: Frequent Itemsets - {frequent_itemsets}")
