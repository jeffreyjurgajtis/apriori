Apriori
=======

A Python implementation of the [Apriori](https://en.wikipedia.org/wiki/Apriori_algorithm) algorithm — an algorithm used to identify patterns in datasets.

### Usage

Your dataset can be provided via a text file. Items should be seperated by a semicolon. See `categories.txt` for an example.

```python
apriori = Apriori(min_support=771, input_filename='categories.txt')
apriori.run()
apriori.write_itemsets_to_file('patterns.txt')

# See k frequent itemsets. For each k, keys are patterns and values are absolute support:
apriori.frequent_itemset

# {
#   1 => { 'Pattern 1' => 243, ... },
#   k => { 'Pattern 1;Pattern 2' => 132, ... },
#   ...
# }
```
