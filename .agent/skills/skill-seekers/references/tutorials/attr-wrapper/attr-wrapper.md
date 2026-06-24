# How To: Attr Wrapper

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test attr wrapper

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `decimal`
- `decimal`
- `re`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`
- `pandas.core.common`

**Setup Required:**
```python
# Fixtures: ts
```

## Step-by-Step Guide

### Step 1: Assign grouped = ts.groupby(...)

```python
grouped = ts.groupby(lambda x: x.weekday())
```

### Step 2: Assign result = grouped.std(...)

```python
result = grouped.std()
```

### Step 3: Assign expected = grouped.agg(...)

```python
expected = grouped.agg(lambda x: np.std(x, ddof=1))
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign result = grouped.describe(...)

```python
result = grouped.describe()
```

### Step 6: Assign expected = value

```python
expected = {name: gp.describe() for name, gp in grouped}
```

### Step 7: Assign expected = value

```python
expected = DataFrame(expected).T
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 9: Assign result = value

```python
result = grouped.dtype
```

### Step 10: Assign expected = grouped.agg(...)

```python
expected = grouped.agg(lambda x: x.dtype)
```

### Step 11: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 12: Assign msg = "'SeriesGroupBy' object has no attribute 'foo'"

```python
msg = "'SeriesGroupBy' object has no attribute 'foo'"
```

### Step 13: Call getattr()

```python
getattr(grouped, 'foo')
```


## Complete Example

```python
# Setup
# Fixtures: ts

# Workflow
grouped = ts.groupby(lambda x: x.weekday())
result = grouped.std()
expected = grouped.agg(lambda x: np.std(x, ddof=1))
tm.assert_series_equal(result, expected)
result = grouped.describe()
expected = {name: gp.describe() for name, gp in grouped}
expected = DataFrame(expected).T
tm.assert_frame_equal(result, expected)
result = grouped.dtype
expected = grouped.agg(lambda x: x.dtype)
tm.assert_series_equal(result, expected)
msg = "'SeriesGroupBy' object has no attribute 'foo'"
with pytest.raises(AttributeError, match=msg):
    getattr(grouped, 'foo')
```

## Next Steps


---

*Source: test_groupby.py:443 | Complexity: Advanced | Last updated: 2026-06-02*