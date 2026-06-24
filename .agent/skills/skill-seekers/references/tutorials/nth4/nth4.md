# How To: Nth4

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test nth4

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame([[1, np.nan], [1, 4], [5, 6]], columns=['A', 'B'])
```

### Step 2: Assign gb = df.groupby(...)

```python
gb = df.groupby('A')
```

### Step 3: Assign result = gb.B.nth(...)

```python
result = gb.B.nth(0, dropna='all')
```

### Step 4: Assign expected = value

```python
expected = df.B.iloc[[1, 2]]
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame([[1, np.nan], [1, 4], [5, 6]], columns=['A', 'B'])
gb = df.groupby('A')
result = gb.B.nth(0, dropna='all')
expected = df.B.iloc[[1, 2]]
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_nth.py:274 | Complexity: Intermediate | Last updated: 2026-06-02*