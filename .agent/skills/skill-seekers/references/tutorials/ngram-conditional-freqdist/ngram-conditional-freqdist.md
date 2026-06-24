# How To: Ngram Conditional Freqdist

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test ngram conditional freqdist

## Prerequisites

**Required Modules:**
- `unittest`
- `pytest`
- `nltk`
- `nltk.lm`
- `nltk.util`


## Step-by-Step Guide

### Step 1: Assign case = unittest.TestCase(...)

```python
case = unittest.TestCase()
```

### Step 2: Assign expected_trigram_contexts = value

```python
expected_trigram_contexts = [('a', 'b'), ('b', 'c'), ('e', 'g'), ('g', 'd'), ('d', 'b')]
```

### Step 3: Assign expected_bigram_contexts = value

```python
expected_bigram_contexts = [('a',), ('b',), ('d',), ('e',), ('c',), ('g',)]
```

### Step 4: Assign bigrams = value

```python
bigrams = self.trigram_counter[2]
```

### Step 5: Assign trigrams = value

```python
trigrams = self.trigram_counter[3]
```

### Step 6: Call self.case.assertCountEqual()

```python
self.case.assertCountEqual(expected_bigram_contexts, bigrams.conditions())
```

### Step 7: Call self.case.assertCountEqual()

```python
self.case.assertCountEqual(expected_trigram_contexts, trigrams.conditions())
```


## Complete Example

```python
# Workflow
case = unittest.TestCase()
expected_trigram_contexts = [('a', 'b'), ('b', 'c'), ('e', 'g'), ('g', 'd'), ('d', 'b')]
expected_bigram_contexts = [('a',), ('b',), ('d',), ('e',), ('c',), ('g',)]
bigrams = self.trigram_counter[2]
trigrams = self.trigram_counter[3]
self.case.assertCountEqual(expected_bigram_contexts, bigrams.conditions())
self.case.assertCountEqual(expected_trigram_contexts, trigrams.conditions())
```

## Next Steps


---

*Source: test_counter.py:41 | Complexity: Intermediate | Last updated: 2026-06-02*