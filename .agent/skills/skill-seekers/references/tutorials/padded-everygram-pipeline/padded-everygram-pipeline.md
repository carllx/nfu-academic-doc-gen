# How To: Padded Everygram Pipeline

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test padded everygram pipeline

## Prerequisites

**Required Modules:**
- `unittest`
- `nltk.lm.preprocessing`


## Step-by-Step Guide

### Step 1: Assign expected_train = value

```python
expected_train = [[('<s>',), ('<s>', 'a'), ('a',), ('a', 'b'), ('b',), ('b', 'c'), ('c',), ('c', '</s>'), ('</s>',)]]
```

### Step 2: Assign expected_vocab = value

```python
expected_vocab = ['<s>', 'a', 'b', 'c', '</s>']
```

### Step 3: Assign unknown = padded_everygram_pipeline(...)

```python
train_data, vocab_data = padded_everygram_pipeline(2, [['a', 'b', 'c']])
```

### Step 4: Call self.assertEqual()

```python
self.assertEqual([list(sent) for sent in train_data], expected_train)
```

### Step 5: Call self.assertEqual()

```python
self.assertEqual(list(vocab_data), expected_vocab)
```


## Complete Example

```python
# Workflow
expected_train = [[('<s>',), ('<s>', 'a'), ('a',), ('a', 'b'), ('b',), ('b', 'c'), ('c',), ('c', '</s>'), ('</s>',)]]
expected_vocab = ['<s>', 'a', 'b', 'c', '</s>']
train_data, vocab_data = padded_everygram_pipeline(2, [['a', 'b', 'c']])
self.assertEqual([list(sent) for sent in train_data], expected_train)
self.assertEqual(list(vocab_data), expected_vocab)
```

## Next Steps


---

*Source: test_preprocessing.py:13 | Complexity: Intermediate | Last updated: 2026-06-02*