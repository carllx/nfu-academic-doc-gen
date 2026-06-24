# How To: Getitem Single Column

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test getitem single column

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
result = df.groupby('A')['C'].mean()
```

### Step 3: Assign as_frame = unknown.groupby.mean(...)

```python
as_frame = df.loc[:, ['A', 'C']].groupby('A').mean()
```

### Step 4: Assign as_series = value

```python
as_series = as_frame.iloc[:, 0]
```

### Step 5: Assign expected = as_series

```python
expected = as_series
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'], 'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'], 'C': np.random.default_rng(2).standard_normal(8), 'D': np.random.default_rng(2).standard_normal(8), 'E': np.random.default_rng(2).standard_normal(8)})
result = df.groupby('A')['C'].mean()
as_frame = df.loc[:, ['A', 'C']].groupby('A').mean()
as_series = as_frame.iloc[:, 0]
expected = as_series
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_grouping.py:116 | Complexity: Intermediate | Last updated: 2026-06-02*