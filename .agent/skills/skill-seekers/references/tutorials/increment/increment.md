# How To: Increment

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test increment

## Prerequisites

**Required Modules:**
- `unittest`
- `pytest`
- `nltk`


## Step-by-Step Guide

### Step 1: Assign text = 'cow cat mouse cat tiger'

```python
text = 'cow cat mouse cat tiger'
```

### Step 2: Assign cfd = ConditionalFreqDist(...)

```python
cfd = ConditionalFreqDist()
```

### Step 3: Call self.assertEqual()

```python
self.assertEqual(cfd.conditions(), [3, 5])
```

### Step 4: Call self.assertCountEqual()

```python
self.assertCountEqual(cfd.conditions(), [3, 5, 2])
```

### Step 5: Call self.assertEqual()

```python
self.assertEqual(cfd[2]['hi'], 1)
```

### Step 6: Assign condition = len(...)

```python
condition = len(word)
```


## Complete Example

```python
# Workflow
text = 'cow cat mouse cat tiger'
cfd = ConditionalFreqDist()
for word in tokenize.word_tokenize(text):
    condition = len(word)
    cfd[condition][word] += 1
self.assertEqual(cfd.conditions(), [3, 5])
cfd[2]['hi'] += 1
self.assertCountEqual(cfd.conditions(), [3, 5, 2])
self.assertEqual(cfd[2]['hi'], 1)
```

## Next Steps


---

*Source: test_cfd_mutation.py:22 | Complexity: Intermediate | Last updated: 2026-06-02*