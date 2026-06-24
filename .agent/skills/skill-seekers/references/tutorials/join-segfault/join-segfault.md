# How To: Join Segfault

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test join segfault

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.reshape.concat`


## Step-by-Step Guide

### Step 1: Assign df1 = DataFrame(...)

```python
df1 = DataFrame({'a': [1, 1], 'b': [1, 2], 'x': [1, 2]})
```

### Step 2: Assign df2 = DataFrame(...)

```python
df2 = DataFrame({'a': [2, 2], 'b': [1, 2], 'y': [1, 2]})
```

### Step 3: Assign df1 = df1.set_index(...)

```python
df1 = df1.set_index(['a', 'b'])
```

### Step 4: Assign df2 = df2.set_index(...)

```python
df2 = df2.set_index(['a', 'b'])
```

### Step 5: Call df1.join()

```python
df1.join(df2, how=how)
```


## Complete Example

```python
# Workflow
df1 = DataFrame({'a': [1, 1], 'b': [1, 2], 'x': [1, 2]})
df2 = DataFrame({'a': [2, 2], 'b': [1, 2], 'y': [1, 2]})
df1 = df1.set_index(['a', 'b'])
df2 = df2.set_index(['a', 'b'])
for how in ['left', 'right', 'outer']:
    df1.join(df2, how=how)
```

## Next Steps


---

*Source: test_join.py:433 | Complexity: Intermediate | Last updated: 2026-06-02*