# How To: Rolling Corr Diff Length

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test rolling corr diff length

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas`
- `pandas._testing`
- `pandas.core.algorithms`


## Step-by-Step Guide

### Step 1: Assign s1 = Series(...)

```python
s1 = Series([1, 2, 3], index=[0, 1, 2])
```

### Step 2: Assign s2 = Series(...)

```python
s2 = Series([1, 3], index=[0, 2])
```

### Step 3: Assign result = s1.rolling.corr(...)

```python
result = s1.rolling(window=3, min_periods=2).corr(s2)
```

### Step 4: Assign expected = Series(...)

```python
expected = Series([None, None, 1.0])
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 6: Assign s2a = Series(...)

```python
s2a = Series([1, None, 3], index=[0, 1, 2])
```

### Step 7: Assign result = s1.rolling.corr(...)

```python
result = s1.rolling(window=3, min_periods=2).corr(s2a)
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
s1 = Series([1, 2, 3], index=[0, 1, 2])
s2 = Series([1, 3], index=[0, 2])
result = s1.rolling(window=3, min_periods=2).corr(s2)
expected = Series([None, None, 1.0])
tm.assert_series_equal(result, expected)
s2a = Series([1, None, 3], index=[0, 1, 2])
result = s1.rolling(window=3, min_periods=2).corr(s2a)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_pairwise.py:158 | Complexity: Advanced | Last updated: 2026-06-02*