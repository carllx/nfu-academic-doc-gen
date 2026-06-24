# How To: Inf Handling

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test inf handling

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.api.types`
- `pandas.core.reshape.tile`


## Step-by-Step Guide

### Step 1: Assign data = np.arange(...)

```python
data = np.arange(6)
```

**Verification:**
```python
assert result[5] == Interval(4, np.inf)
```

### Step 2: Assign data_ser = Series(...)

```python
data_ser = Series(data, dtype='int64')
```

**Verification:**
```python
assert result[0] == Interval(-np.inf, 2)
```

### Step 3: Assign bins = value

```python
bins = [-np.inf, 2, 4, np.inf]
```

**Verification:**
```python
assert result_ser[5] == Interval(4, np.inf)
```

### Step 4: Assign result = cut(...)

```python
result = cut(data, bins)
```

**Verification:**
```python
assert result_ser[0] == Interval(-np.inf, 2)
```

### Step 5: Assign result_ser = cut(...)

```python
result_ser = cut(data_ser, bins)
```

### Step 6: Assign ex_uniques = IntervalIndex.from_breaks(...)

```python
ex_uniques = IntervalIndex.from_breaks(bins)
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result.categories, ex_uniques)
```

**Verification:**
```python
assert result[5] == Interval(4, np.inf)
```


## Complete Example

```python
# Workflow
data = np.arange(6)
data_ser = Series(data, dtype='int64')
bins = [-np.inf, 2, 4, np.inf]
result = cut(data, bins)
result_ser = cut(data_ser, bins)
ex_uniques = IntervalIndex.from_breaks(bins)
tm.assert_index_equal(result.categories, ex_uniques)
assert result[5] == Interval(4, np.inf)
assert result[0] == Interval(-np.inf, 2)
assert result_ser[5] == Interval(4, np.inf)
assert result_ser[0] == Interval(-np.inf, 2)
```

## Next Steps


---

*Source: test_cut.py:268 | Complexity: Intermediate | Last updated: 2026-06-02*