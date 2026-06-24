# How To: Where Other

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test where other

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas.compat.numpy`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tseries.frequencies`


## Step-by-Step Guide

### Step 1: Assign i = date_range(...)

```python
i = date_range('20130101', periods=3, tz='US/Eastern')
```

### Step 2: Assign i2 = i.copy(...)

```python
i2 = i.copy()
```

### Step 3: Assign i2 = Index(...)

```python
i2 = Index([pd.NaT, pd.NaT] + i[2:].tolist())
```

### Step 4: Assign result = i.where(...)

```python
result = i.where(notna(i2), i2)
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, i2)
```

### Step 6: Assign i2 = i.copy(...)

```python
i2 = i.copy()
```

### Step 7: Assign i2 = Index(...)

```python
i2 = Index([pd.NaT, pd.NaT] + i[2:].tolist())
```

### Step 8: Assign result = i.where(...)

```python
result = i.where(notna(i2), i2._values)
```

### Step 9: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, i2)
```

### Step 10: Assign result = i.where(...)

```python
result = i.where(notna(i), other=arr)
```

### Step 11: Assign expected = i

```python
expected = i
```

### Step 12: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Workflow
i = date_range('20130101', periods=3, tz='US/Eastern')
for arr in [np.nan, pd.NaT]:
    result = i.where(notna(i), other=arr)
    expected = i
    tm.assert_index_equal(result, expected)
i2 = i.copy()
i2 = Index([pd.NaT, pd.NaT] + i[2:].tolist())
result = i.where(notna(i2), i2)
tm.assert_index_equal(result, i2)
i2 = i.copy()
i2 = Index([pd.NaT, pd.NaT] + i[2:].tolist())
result = i.where(notna(i2), i2._values)
tm.assert_index_equal(result, i2)
```

## Next Steps


---

*Source: test_indexing.py:128 | Complexity: Advanced | Last updated: 2026-06-02*