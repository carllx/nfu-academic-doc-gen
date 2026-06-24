# How To: Append To Another

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test append to another

## Prerequisites

**Required Modules:**
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign fst = Index(...)

```python
fst = Index(['a', 'b'])
```

### Step 2: Assign snd = CategoricalIndex(...)

```python
snd = CategoricalIndex(['d', 'e'])
```

### Step 3: Assign result = fst.append(...)

```python
result = fst.append(snd)
```

### Step 4: Assign expected = Index(...)

```python
expected = Index(['a', 'b', 'd', 'e'])
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Workflow
fst = Index(['a', 'b'])
snd = CategoricalIndex(['d', 'e'])
result = fst.append(snd)
expected = Index(['a', 'b', 'd', 'e'])
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_append.py:56 | Complexity: Intermediate | Last updated: 2026-06-02*