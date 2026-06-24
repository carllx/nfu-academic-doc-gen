# How To: Set Uniform Distortion Probabilities Of Non Domain Values

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test set uniform distortion probabilities of non domain values

## Prerequisites

**Required Modules:**
- `unittest`
- `collections`
- `nltk.translate`
- `nltk.translate.ibm_model`


## Step-by-Step Guide

### Step 1: Assign src_classes = value

```python
src_classes = {'schinken': 0, 'eier': 0, 'spam': 1}
```

### Step 2: Assign trg_classes = value

```python
trg_classes = {'ham': 0, 'eggs': 1, 'spam': 2}
```

### Step 3: Assign corpus = value

```python
corpus = [AlignedSent(['ham', 'eggs'], ['schinken', 'schinken', 'eier']), AlignedSent(['spam', 'spam', 'spam', 'spam'], ['spam', 'spam'])]
```

### Step 4: Assign model4 = IBMModel4(...)

```python
model4 = IBMModel4(corpus, 0, src_classes, trg_classes)
```

### Step 5: Call model4.set_uniform_probabilities()

```python
model4.set_uniform_probabilities(corpus)
```

### Step 6: Call self.assertEqual()

```python
self.assertEqual(model4.head_distortion_table[4][0][0], IBMModel.MIN_PROB)
```

### Step 7: Call self.assertEqual()

```python
self.assertEqual(model4.head_distortion_table[100][1][2], IBMModel.MIN_PROB)
```

### Step 8: Call self.assertEqual()

```python
self.assertEqual(model4.non_head_distortion_table[4][0], IBMModel.MIN_PROB)
```

### Step 9: Call self.assertEqual()

```python
self.assertEqual(model4.non_head_distortion_table[100][2], IBMModel.MIN_PROB)
```


## Complete Example

```python
# Workflow
src_classes = {'schinken': 0, 'eier': 0, 'spam': 1}
trg_classes = {'ham': 0, 'eggs': 1, 'spam': 2}
corpus = [AlignedSent(['ham', 'eggs'], ['schinken', 'schinken', 'eier']), AlignedSent(['spam', 'spam', 'spam', 'spam'], ['spam', 'spam'])]
model4 = IBMModel4(corpus, 0, src_classes, trg_classes)
model4.set_uniform_probabilities(corpus)
self.assertEqual(model4.head_distortion_table[4][0][0], IBMModel.MIN_PROB)
self.assertEqual(model4.head_distortion_table[100][1][2], IBMModel.MIN_PROB)
self.assertEqual(model4.non_head_distortion_table[4][0], IBMModel.MIN_PROB)
self.assertEqual(model4.non_head_distortion_table[100][2], IBMModel.MIN_PROB)
```

## Next Steps


---

*Source: test_ibm4.py:37 | Complexity: Advanced | Last updated: 2026-06-02*