# How To: Isin With I8

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test isin with i8

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign expected = Series(...)

```python
expected = Series([True, True, False, False, False])
```

### Step 2: Assign expected2 = Series(...)

```python
expected2 = Series([False, True, False, False, False])
```

### Step 3: Assign s = Series(...)

```python
s = Series(date_range('jan-01-2013', 'jan-05-2013'))
```

### Step 4: Assign result = s.isin(...)

```python
result = s.isin(s[0:2])
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 6: Assign result = s.isin(...)

```python
result = s.isin(s[0:2].values)
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 8: Assign result = s.isin(...)

```python
result = s.isin([s[1]])
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected2)
```

### Step 10: Assign result = s.isin(...)

```python
result = s.isin([np.datetime64(s[1])])
```

### Step 11: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected2)
```

### Step 12: Assign result = s.isin(...)

```python
result = s.isin(set(s[0:2]))
```

### Step 13: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 14: Assign s = Series(...)

```python
s = Series(pd.to_timedelta(range(5), unit='d'))
```

### Step 15: Assign result = s.isin(...)

```python
result = s.isin(s[0:2])
```

### Step 16: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
expected = Series([True, True, False, False, False])
expected2 = Series([False, True, False, False, False])
s = Series(date_range('jan-01-2013', 'jan-05-2013'))
result = s.isin(s[0:2])
tm.assert_series_equal(result, expected)
result = s.isin(s[0:2].values)
tm.assert_series_equal(result, expected)
result = s.isin([s[1]])
tm.assert_series_equal(result, expected2)
result = s.isin([np.datetime64(s[1])])
tm.assert_series_equal(result, expected2)
result = s.isin(set(s[0:2]))
tm.assert_series_equal(result, expected)
s = Series(pd.to_timedelta(range(5), unit='d'))
result = s.isin(s[0:2])
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_isin.py:70 | Complexity: Advanced | Last updated: 2026-06-02*