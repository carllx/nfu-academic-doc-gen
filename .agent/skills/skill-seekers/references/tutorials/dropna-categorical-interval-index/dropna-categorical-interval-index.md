# How To: Dropna Categorical Interval Index

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dropna categorical interval index

## Prerequisites

**Required Modules:**
- `datetime`
- `dateutil`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign ii = pd.IntervalIndex.from_breaks(...)

```python
ii = pd.IntervalIndex.from_breaks([0, 2.78, 3.14, 6.28])
```

### Step 2: Assign ci = pd.CategoricalIndex(...)

```python
ci = pd.CategoricalIndex(ii)
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame({'A': list('abc')}, index=ci)
```

### Step 4: Assign expected = df

```python
expected = df
```

### Step 5: Assign result = df.dropna(...)

```python
result = df.dropna()
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
ii = pd.IntervalIndex.from_breaks([0, 2.78, 3.14, 6.28])
ci = pd.CategoricalIndex(ii)
df = DataFrame({'A': list('abc')}, index=ci)
expected = df
result = df.dropna()
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_dropna.py:201 | Complexity: Intermediate | Last updated: 2026-06-02*