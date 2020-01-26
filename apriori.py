import os
import numpy

class Apriori(object):
    def __init__(self, min_support, input_filename):
        dirname = os.path.dirname(os.path.abspath(__file__))
        self.path_to_data = os.path.join(dirname, input_filename)
        self.min_support = min_support
        self.transactions = self.build_transactions()
        self.frequent_itemset = dict()

    """
    Build transaction list from input file
    """
    def build_transactions(self):
        transactions = list()

        with open(self.path_to_data, 'r') as category_file:
            for line in category_file.readlines():
                categories = [category.rstrip() for category in line.split(';')]
                transactions.append(categories)

        return transactions

    """
    Build initial k1 frequent itemset
    """
    def generate_k1_itemset(self):
        itemset = dict()

        for transaction in self.transactions:
            for category in transaction:
                itemset.setdefault(category, 0)
                itemset[category] += 1

        return itemset

    """
    Generate K itemset
    """
    def generate_itemset(self, current_itemset, k):
        categories = set()
        new_itemset = dict()

        for key in current_itemset.keys():
            row = frozenset([category.strip() for category in key.split(';')])
            categories.add(row)

        patterns = set([x.union(y) for x in categories for y in categories \
                if len(x.union(y)) == k])

        for pattern in patterns:
            pattern = list(pattern)
            key = ';'.join(pattern)
            new_itemset.setdefault(key, 0)
            print(key)

            for transaction in self.transactions:
                is_match = all(category in transaction for category in pattern)
                if is_match:
                    new_itemset[key] += 1

        return new_itemset

    """
    Remove all items that do not meet minsup
    """
    def prune_itemset(self, current_itemset):
        frequent_itemset = dict()

        for pattern, support in current_itemset.items():
            if support > self.min_support:
                frequent_itemset[pattern] = support

        return frequent_itemset

    """
    Run the apriori algorithm
    """
    def run(self):
        k = 1
        current_itemset = self.generate_k1_itemset()
        current_itemset = self.prune_itemset(current_itemset)
        self.frequent_itemset[k] = current_itemset

        while len(self.frequent_itemset[k]) > 0:
            k += 1
            current_itemset = self.generate_itemset(current_itemset, k)
            current_itemset = self.prune_itemset(current_itemset)
            self.frequent_itemset[k] = current_itemset
            print(current_itemset)

    """
    Write patterns to file
    """
    def write_itemsets_to_file(self, filename):
        with open(filename, 'w') as result_file:
            for itemset in self.frequent_itemset.values():
                for pattern, support in itemset.items():
                    result_file.write(f'{support}:{pattern}\n')


def main():
    apriori = Apriori(min_support=771, input_filename='categories.txt')
    apriori.run()
    apriori.write_itemsets_to_file('patterns.txt')

if __name__ == '__main__':
    main()
