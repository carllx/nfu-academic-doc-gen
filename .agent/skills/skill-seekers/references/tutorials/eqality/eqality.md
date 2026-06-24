# How To: Eqality

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test eqality

## Prerequisites

**Required Modules:**
- `unittest`
- `collections`
- `timeit`
- `nltk.lm`
- `nltk.corpus.europarl_raw`


## Step-by-Step Guide

### Step 1: Assign v1 = Vocabulary(...)

```python
v1 = Vocabulary(['a', 'b', 'c'], unk_cutoff=1)
```

### Step 2: Assign v2 = Vocabulary(...)

```python
v2 = Vocabulary(['a', 'b', 'c'], unk_cutoff=1)
```

### Step 3: Assign v3 = Vocabulary(...)

```python
v3 = Vocabulary(['a', 'b', 'c'], unk_cutoff=1, unk_label='blah')
```

### Step 4: Assign v4 = Vocabulary(...)

```python
v4 = Vocabulary(['a', 'b'], unk_cutoff=1)
```

### Step 5: Call self.assertEqual()

```python
self.assertEqual(v1, v2)
```

### Step 6: Call self.assertNotEqual()

```python
self.assertNotEqual(v1, v3)
```

### Step 7: Call self.assertNotEqual()

```python
self.assertNotEqual(v1, v4)
```


## Complete Example

```python
# Workflow
v1 = Vocabulary(['a', 'b', 'c'], unk_cutoff=1)
v2 = Vocabulary(['a', 'b', 'c'], unk_cutoff=1)
v3 = Vocabulary(['a', 'b', 'c'], unk_cutoff=1, unk_label='blah')
v4 = Vocabulary(['a', 'b'], unk_cutoff=1)
self.assertEqual(v1, v2)
self.assertNotEqual(v1, v3)
self.assertNotEqual(v1, v4)
```

## Next Steps


---

*Source: test_vocabulary.py:115 | Complexity: Intermediate | Last updated: 2026-06-02*