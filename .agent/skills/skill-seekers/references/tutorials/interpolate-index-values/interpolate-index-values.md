# How To: Interpolate Index Values

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test interpolate index values

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign s = Series(...)

```python
s = Series(np.nan, index=np.sort(np.random.default_rng(2).random(30)))
```

### Step 2: Assign unknown = np.random.default_rng.standard_normal(...)

```python
s.loc[::3] = np.random.default_rng(2).standard_normal(10)
```

### Step 3: Assign vals = s.index.values.astype(...)

```python
vals = s.index.values.astype(float)
```

### Step 4: Assign result = s.interpolate(...)

```python
result = s.interpolate(method='index')
```

### Step 5: Assign expected = s.copy(...)

```python
expected = s.copy()
```

### Step 6: Assign bad = isna(...)

```python
bad = isna(expected.values)
```

### Step 7: Assign good = value

```python
good = ~bad
```

### Step 8: Assign expected = Series(...)

```python
expected = Series(np.interp(vals[bad], vals[good], s.values[good]), index=s.index[bad])
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result[bad], expected)
```

### Step 10: Assign other_result = s.interpolate(...)

```python
other_result = s.interpolate(method='values')
```

### Step 11: Call tm.assert_series_equal()

```python
tm.assert_series_equal(other_result, result)
```

### Step 12: Call tm.assert_series_equal()

```python
tm.assert_series_equal(other_result[bad], expected)
```


## Complete Example

```python
# Workflow
s = Series(np.nan, index=np.sort(np.random.default_rng(2).random(30)))
s.loc[::3] = np.random.default_rng(2).standard_normal(10)
vals = s.index.values.astype(float)
result = s.interpolate(method='index')
expected = s.copy()
bad = isna(expected.values)
good = ~bad
expected = Series(np.interp(vals[bad], vals[good], s.values[good]), index=s.index[bad])
tm.assert_series_equal(result[bad], expected)
other_result = s.interpolate(method='values')
tm.assert_series_equal(other_result, result)
tm.assert_series_equal(other_result[bad], expected)
```

## Next Steps


---

*Source: test_interpolate.py:219 | Complexity: Advanced | Last updated: 2026-06-02*