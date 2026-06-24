# How To: Where Tz

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test where tz

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

### Step 2: Assign result = i.where(...)

```python
result = i.where(notna(i))
```

### Step 3: Assign expected = i

```python
expected = i
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 5: Assign i2 = i.copy(...)

```python
i2 = i.copy()
```

### Step 6: Assign i2 = Index(...)

```python
i2 = Index([pd.NaT, pd.NaT] + i[2:].tolist())
```

### Step 7: Assign result = i.where(...)

```python
result = i.where(notna(i2))
```

### Step 8: Assign expected = i2

```python
expected = i2
```

### Step 9: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Workflow
i = date_range('20130101', periods=3, tz='US/Eastern')
result = i.where(notna(i))
expected = i
tm.assert_index_equal(result, expected)
i2 = i.copy()
i2 = Index([pd.NaT, pd.NaT] + i[2:].tolist())
result = i.where(notna(i2))
expected = i2
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_indexing.py:201 | Complexity: Advanced | Last updated: 2026-06-02*