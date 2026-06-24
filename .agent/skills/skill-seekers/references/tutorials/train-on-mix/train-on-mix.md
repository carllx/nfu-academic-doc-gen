# How To: Train On Mix

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test train on mix

## Prerequisites

**Required Modules:**
- `unittest`
- `pytest`
- `nltk`
- `nltk.lm`
- `nltk.util`


## Step-by-Step Guide

### Step 1: Assign mixed_sent = value

```python
mixed_sent = [('a', 'b'), ('c', 'd'), ('e', 'f', 'g'), ('h',)]
```

### Step 2: Assign counter = NgramCounter(...)

```python
counter = NgramCounter([mixed_sent])
```

### Step 3: Assign unigrams = value

```python
unigrams = ['h']
```

### Step 4: Assign bigram_contexts = value

```python
bigram_contexts = [('a',), ('c',)]
```

### Step 5: Assign trigram_contexts = value

```python
trigram_contexts = [('e', 'f')]
```

### Step 6: Call self.case.assertCountEqual()

```python
self.case.assertCountEqual(unigrams, counter[1].keys())
```

### Step 7: Call self.case.assertCountEqual()

```python
self.case.assertCountEqual(bigram_contexts, counter[2].keys())
```

### Step 8: Call self.case.assertCountEqual()

```python
self.case.assertCountEqual(trigram_contexts, counter[3].keys())
```


## Complete Example

```python
# Workflow
mixed_sent = [('a', 'b'), ('c', 'd'), ('e', 'f', 'g'), ('h',)]
counter = NgramCounter([mixed_sent])
unigrams = ['h']
bigram_contexts = [('a',), ('c',)]
trigram_contexts = [('e', 'f')]
self.case.assertCountEqual(unigrams, counter[1].keys())
self.case.assertCountEqual(bigram_contexts, counter[2].keys())
self.case.assertCountEqual(trigram_contexts, counter[3].keys())
```

## Next Steps


---

*Source: test_counter.py:107 | Complexity: Advanced | Last updated: 2026-06-02*