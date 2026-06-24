# How To: Infer With Date And Datetime

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test infer with date and datetime

## Prerequisites

**Required Modules:**
- `collections`
- `collections.abc`
- `datetime`
- `dateutil.tz`
- `numpy`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas.compat`
- `pandas.compat.numpy`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`
- `pandas.core.internals.blocks`
- `numpy.dtypes`


## Step-by-Step Guide

### Step 1: Assign ts = Timestamp(...)

```python
ts = Timestamp(2016, 1, 1)
```

### Step 2: Assign vals = value

```python
vals = [ts.to_pydatetime(), ts.date()]
```

### Step 3: Assign ser = Series(...)

```python
ser = Series(vals)
```

### Step 4: Assign expected = Series(...)

```python
expected = Series(vals, dtype=object)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ser, expected)
```

### Step 6: Assign idx = Index(...)

```python
idx = Index(vals)
```

### Step 7: Assign expected = Index(...)

```python
expected = Index(vals, dtype=object)
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx, expected)
```


## Complete Example

```python
# Workflow
ts = Timestamp(2016, 1, 1)
vals = [ts.to_pydatetime(), ts.date()]
ser = Series(vals)
expected = Series(vals, dtype=object)
tm.assert_series_equal(ser, expected)
idx = Index(vals)
expected = Index(vals, dtype=object)
tm.assert_index_equal(idx, expected)
```

## Next Steps


---

*Source: test_constructors.py:70 | Complexity: Advanced | Last updated: 2026-06-02*