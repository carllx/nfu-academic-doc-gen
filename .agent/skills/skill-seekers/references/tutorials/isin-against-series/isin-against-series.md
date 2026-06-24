# How To: Isin Against Series

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test isin against series

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
df = DataFrame({'A': [1, 2, 3, 4], 'B': [2, np.nan, 4, 4]}, index=['a', 'b', 'c', 'd'])
```

### Step 2: Assign s = Series(...)

```python
s = Series([1, 3, 11, 4], index=['a', 'b', 'c', 'd'])
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame(False, index=df.index, columns=df.columns)
```

### Step 4: Assign unknown = True

```python
expected.loc['a', 'A'] = True
```

### Step 5: Assign unknown = True

```python
expected.loc['d'] = True
```

### Step 6: Assign result = df.isin(...)

```python
result = df.isin(s)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({'A': [1, 2, 3, 4], 'B': [2, np.nan, 4, 4]}, index=['a', 'b', 'c', 'd'])
s = Series([1, 3, 11, 4], index=['a', 'b', 'c', 'd'])
expected = DataFrame(False, index=df.index, columns=df.columns)
expected.loc['a', 'A'] = True
expected.loc['d'] = True
result = df.isin(s)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_isin.py:130 | Complexity: Intermediate | Last updated: 2026-06-02*