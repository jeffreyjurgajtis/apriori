import os
import numpy

class Apriori(object):
    def __init__(self, min_support):
        dirname = os.path.dirname(os.path.abspath(__file__))
        self.path_to_data = os.path.join(dirname, 'categories.txt')
        self.min_support = min_support
        self.itemsets = dict()
        self.frequent_itemsets = dict()

    def build_itemsets(self):
        with open(self.path_to_data, 'r') as category_file:
            for line in category_file.readlines():
                for item in line.split(';'):
                    item = item.rstrip()
                    self.itemsets.setdefault(item, 0)
                    self.itemsets[item] += 1

    def build_frequent_itemsets(self):
        for item, support in self.itemsets.items():
            if support > self.min_support:
                self.frequent_itemsets[item] = support

        output = open('patterns.txt', 'w')
        for item, support in self.frequent_itemsets.items():
            output.write(f'{support}:{item}\n')
        output.close()

def main():
    apriori = Apriori(771)
    apriori.build_itemsets()
    apriori.build_frequent_itemsets()
    # import code; code.interact(local=dict(globals(), **locals()))

if __name__ == '__main__':
    main()
