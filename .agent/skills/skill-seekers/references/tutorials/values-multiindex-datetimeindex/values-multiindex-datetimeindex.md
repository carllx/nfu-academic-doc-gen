# How To: Values Multiindex Datetimeindex

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test values multiindex datetimeindex

## Prerequisites

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas.core.dtypes.cast`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign ints = np.arange(...)

```python
ints = np.arange(10 ** 18, 10 ** 18 + 5)
```

### Step 2: Assign naive = pd.DatetimeIndex(...)

```python
naive = pd.DatetimeIndex(ints)
```

### Step 3: Assign aware = pd.DatetimeIndex(...)

```python
aware = pd.DatetimeIndex(ints, tz='US/Central')
```

### Step 4: Assign idx = MultiIndex.from_arrays(...)

```python
idx = MultiIndex.from_arrays([naive, aware])
```

### Step 5: Assign result = value

```python
result = idx.values
```

### Step 6: Assign outer = pd.DatetimeIndex(...)

```python
outer = pd.DatetimeIndex([x[0] for x in result])
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(outer, naive)
```

### Step 8: Assign inner = pd.DatetimeIndex(...)

```python
inner = pd.DatetimeIndex([x[1] for x in result])
```

### Step 9: Call tm.assert_index_equal()

```python
tm.assert_index_equal(inner, aware)
```

### Step 10: Assign result = value

```python
result = idx[:2].values
```

### Step 11: Assign outer = pd.DatetimeIndex(...)

```python
outer = pd.DatetimeIndex([x[0] for x in result])
```

### Step 12: Call tm.assert_index_equal()

```python
tm.assert_index_equal(outer, naive[:2])
```

### Step 13: Assign inner = pd.DatetimeIndex(...)

```python
inner = pd.DatetimeIndex([x[1] for x in result])
```

### Step 14: Call tm.assert_index_equal()

```python
tm.assert_index_equal(inner, aware[:2])
```


## Complete Example

```python
# Workflow
ints = np.arange(10 ** 18, 10 ** 18 + 5)
naive = pd.DatetimeIndex(ints)
aware = pd.DatetimeIndex(ints, tz='US/Central')
idx = MultiIndex.from_arrays([naive, aware])
result = idx.values
outer = pd.DatetimeIndex([x[0] for x in result])
tm.assert_index_equal(outer, naive)
inner = pd.DatetimeIndex([x[1] for x in result])
tm.assert_index_equal(inner, aware)
result = idx[:2].values
outer = pd.DatetimeIndex([x[0] for x in result])
tm.assert_index_equal(outer, naive[:2])
inner = pd.DatetimeIndex([x[1] for x in result])
tm.assert_index_equal(inner, aware[:2])
```

## Next Steps


---

*Source: test_integrity.py:54 | Complexity: Advanced | Last updated: 2026-06-02*