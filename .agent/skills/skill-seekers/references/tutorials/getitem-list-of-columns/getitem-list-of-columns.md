# How To: Getitem List Of Columns

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test getitem list of columns

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.groupby.grouper`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'], 'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'], 'C': np.random.default_rng(2).standard_normal(8), 'D': np.random.default_rng(2).standard_normal(8), 'E': np.random.default_rng(2).standard_normal(8)})
```

### Step 2: Assign result = unknown.mean(...)

```python
result = df.groupby('A')[['C', 'D']].mean()
```

### Step 3: Assign result2 = unknown.mean(...)

```python
result2 = df.groupby('A')[df.columns[2:4]].mean()
```

### Step 4: Assign expected = unknown.groupby.mean(...)

```python
expected = df.loc[:, ['A', 'C', 'D']].groupby('A').mean()
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result2, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'], 'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'], 'C': np.random.default_rng(2).standard_normal(8), 'D': np.random.default_rng(2).standard_normal(8), 'E': np.random.default_rng(2).standard_normal(8)})
result = df.groupby('A')[['C', 'D']].mean()
result2 = df.groupby('A')[df.columns[2:4]].mean()
expected = df.loc[:, ['A', 'C', 'D']].groupby('A').mean()
tm.assert_frame_equal(result, expected)
tm.assert_frame_equal(result2, expected)
```

## Next Steps


---

*Source: test_grouping.py:70 | Complexity: Intermediate | Last updated: 2026-06-02*