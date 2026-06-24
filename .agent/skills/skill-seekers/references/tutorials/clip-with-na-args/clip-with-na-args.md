# How To: Clip With Na Args

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: Should process np.nan argument as None

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: 'Should process np.nan argument as None'

```python
'Should process np.nan argument as None'
```

### Step 2: Assign s = Series(...)

```python
s = Series([1, 2, 3])
```

### Step 3: Call tm.assert_series_equal()

```python
tm.assert_series_equal(s.clip(np.nan), Series([1, 2, 3]))
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(s.clip(upper=np.nan, lower=np.nan), Series([1, 2, 3]))
```

### Step 5: Assign msg = "Downcasting behavior in Series and DataFrame methods 'where'"

```python
msg = "Downcasting behavior in Series and DataFrame methods 'where'"
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, Series([1, 4, 3]))
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, Series([1, 2, 1]))
```

### Step 8: Assign s = Series(...)

```python
s = Series([1, 2, 3])
```

### Step 9: Assign result = s.clip(...)

```python
result = s.clip(0, [np.nan, np.nan, np.nan])
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(s, result)
```

### Step 11: Assign res = s.clip(...)

```python
res = s.clip(lower=[0, 4, np.nan])
```

### Step 12: Assign res = s.clip(...)

```python
res = s.clip(upper=[1, np.nan, 1])
```


## Complete Example

```python
# Workflow
'Should process np.nan argument as None'
s = Series([1, 2, 3])
tm.assert_series_equal(s.clip(np.nan), Series([1, 2, 3]))
tm.assert_series_equal(s.clip(upper=np.nan, lower=np.nan), Series([1, 2, 3]))
msg = "Downcasting behavior in Series and DataFrame methods 'where'"
with tm.assert_produces_warning(FutureWarning, match=msg):
    res = s.clip(lower=[0, 4, np.nan])
tm.assert_series_equal(res, Series([1, 4, 3]))
with tm.assert_produces_warning(FutureWarning, match=msg):
    res = s.clip(upper=[1, np.nan, 1])
tm.assert_series_equal(res, Series([1, 2, 1]))
s = Series([1, 2, 3])
result = s.clip(0, [np.nan, np.nan, np.nan])
tm.assert_series_equal(s, result)
```

## Next Steps


---

*Source: test_clip.py:63 | Complexity: Advanced | Last updated: 2026-06-02*