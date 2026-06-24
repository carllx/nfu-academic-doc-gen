# How To: Assign Index Sequences

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test assign index sequences

## Prerequisites

**Required Modules:**
- `datetime`
- `io`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame.set_index(...)

```python
df = DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}).set_index(['a', 'b'])
```

### Step 2: Assign index = list(...)

```python
index = list(df.index)
```

### Step 3: Assign unknown = value

```python
index[0] = ('faz', 'boo')
```

### Step 4: Assign df.index = index

```python
df.index = index
```

### Step 5: Call repr()

```python
repr(df)
```

### Step 6: Assign unknown = value

```python
index[0] = ['faz', 'boo']
```

### Step 7: Assign df.index = index

```python
df.index = index
```

### Step 8: Call repr()

```python
repr(df)
```


## Complete Example

```python
# Workflow
df = DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}).set_index(['a', 'b'])
index = list(df.index)
index[0] = ('faz', 'boo')
df.index = index
repr(df)
index[0] = ['faz', 'boo']
df.index = index
repr(df)
```

## Next Steps


---

*Source: test_repr.py:63 | Complexity: Advanced | Last updated: 2026-06-02*