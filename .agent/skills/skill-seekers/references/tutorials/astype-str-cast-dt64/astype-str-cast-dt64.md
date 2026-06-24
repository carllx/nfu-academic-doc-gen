# How To: Astype Str Cast Dt64

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test astype str cast dt64

## Prerequisites

**Required Modules:**
- `datetime`
- `importlib`
- `string`
- `sys`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign ts = Series(...)

```python
ts = Series([Timestamp('2010-01-04 00:00:00')])
```

### Step 2: Assign res = ts.astype(...)

```python
res = ts.astype(str)
```

### Step 3: Assign expected = Series(...)

```python
expected = Series(['2010-01-04'], dtype='str')
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, expected)
```

### Step 5: Assign ts = Series(...)

```python
ts = Series([Timestamp('2010-01-04 00:00:00', tz='US/Eastern')])
```

### Step 6: Assign res = ts.astype(...)

```python
res = ts.astype(str)
```

### Step 7: Assign expected = Series(...)

```python
expected = Series(['2010-01-04 00:00:00-05:00'], dtype='str')
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, expected)
```


## Complete Example

```python
# Workflow
ts = Series([Timestamp('2010-01-04 00:00:00')])
res = ts.astype(str)
expected = Series(['2010-01-04'], dtype='str')
tm.assert_series_equal(res, expected)
ts = Series([Timestamp('2010-01-04 00:00:00', tz='US/Eastern')])
res = ts.astype(str)
expected = Series(['2010-01-04 00:00:00-05:00'], dtype='str')
tm.assert_series_equal(res, expected)
```

## Next Steps


---

*Source: test_astype.py:287 | Complexity: Advanced | Last updated: 2026-06-02*