# How To: Set Uniform Vacancy Probabilities Of Max Displacements

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test set uniform vacancy probabilities of max displacements

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

### Step 4: Assign model5 = IBMModel5(...)

```python
model5 = IBMModel5(corpus, 0, src_classes, trg_classes)
```

### Step 5: Call model5.set_uniform_probabilities()

```python
model5.set_uniform_probabilities(corpus)
```

### Step 6: Assign expected_prob = value

```python
expected_prob = 1.0 / (2 * 4)
```

### Step 7: Call self.assertEqual()

```python
self.assertEqual(model5.head_vacancy_table[4][4][0], expected_prob)
```

### Step 8: Call self.assertEqual()

```python
self.assertEqual(model5.head_vacancy_table[-3][1][2], expected_prob)
```

### Step 9: Call self.assertEqual()

```python
self.assertEqual(model5.non_head_vacancy_table[4][4][0], expected_prob)
```

### Step 10: Call self.assertEqual()

```python
self.assertEqual(model5.non_head_vacancy_table[-3][1][2], expected_prob)
```


## Complete Example

```python
# Workflow
src_classes = {'schinken': 0, 'eier': 0, 'spam': 1}
trg_classes = {'ham': 0, 'eggs': 1, 'spam': 2}
corpus = [AlignedSent(['ham', 'eggs'], ['schinken', 'schinken', 'eier']), AlignedSent(['spam', 'spam', 'spam', 'spam'], ['spam', 'spam'])]
model5 = IBMModel5(corpus, 0, src_classes, trg_classes)
model5.set_uniform_probabilities(corpus)
expected_prob = 1.0 / (2 * 4)
self.assertEqual(model5.head_vacancy_table[4][4][0], expected_prob)
self.assertEqual(model5.head_vacancy_table[-3][1][2], expected_prob)
self.assertEqual(model5.non_head_vacancy_table[4][4][0], expected_prob)
self.assertEqual(model5.non_head_vacancy_table[-3][1][2], expected_prob)
```

## Next Steps


---

*Source: test_ibm5.py:13 | Complexity: Advanced | Last updated: 2026-06-02*