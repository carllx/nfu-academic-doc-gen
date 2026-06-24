# How To: Set Index Multiindex

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test set index multiindex

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign d = value

```python
d = {'t1': [2, 2.5, 3], 't2': [4, 5, 6]}
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(d)
```

### Step 3: Assign tuples = value

```python
tuples = [(0, 1), (0, 2), (1, 2)]
```

### Step 4: Assign unknown = tuples

```python
df['tuples'] = tuples
```

### Step 5: Assign index = MultiIndex.from_tuples(...)

```python
index = MultiIndex.from_tuples(df['tuples'])
```

### Step 6: Call df.set_index()

```python
df.set_index(index)
```


## Complete Example

```python
# Workflow
d = {'t1': [2, 2.5, 3], 't2': [4, 5, 6]}
df = DataFrame(d)
tuples = [(0, 1), (0, 2), (1, 2)]
df['tuples'] = tuples
index = MultiIndex.from_tuples(df['tuples'])
df.set_index(index)
```

## Next Steps


---

*Source: test_set_index.py:57 | Complexity: Intermediate | Last updated: 2026-06-02*