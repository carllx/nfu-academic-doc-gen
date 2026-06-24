# How To: Value Counts With Nan

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test value counts with nan

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `collections`
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.base.common`

**Setup Required:**
```python
# Fixtures: dropna, index_or_series
```

## Step-by-Step Guide

### Step 1: Assign klass = index_or_series

```python
klass = index_or_series
```

### Step 2: Assign values = value

```python
values = [True, pd.NA, np.nan]
```

### Step 3: Assign obj = klass(...)

```python
obj = klass(values)
```

### Step 4: Assign res = obj.value_counts(...)

```python
res = obj.value_counts(dropna=dropna)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, expected)
```

### Step 6: Assign expected = Series(...)

```python
expected = Series([1], index=Index([True], dtype=obj.dtype), name='count')
```

### Step 7: Assign expected = Series(...)

```python
expected = Series([1, 1, 1], index=[True, pd.NA, np.nan], name='count')
```


## Complete Example

```python
# Setup
# Fixtures: dropna, index_or_series

# Workflow
klass = index_or_series
values = [True, pd.NA, np.nan]
obj = klass(values)
res = obj.value_counts(dropna=dropna)
if dropna is True:
    expected = Series([1], index=Index([True], dtype=obj.dtype), name='count')
else:
    expected = Series([1, 1, 1], index=[True, pd.NA, np.nan], name='count')
tm.assert_series_equal(res, expected)
```

## Next Steps


---

*Source: test_value_counts.py:333 | Complexity: Intermediate | Last updated: 2026-06-02*