# How To: Divmod

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test divmod

## Prerequisites

**Required Modules:**
- `datetime`
- `decimal`
- `operator`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas._libs.tslibs`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`
- `pandas.core.computation`
- `pandas.core.computation.check`


## Step-by-Step Guide

### Step 1: Assign a = Series(...)

```python
a = Series([1, 1, 1, np.nan], index=['a', 'b', 'c', 'd'])
```

### Step 2: Assign b = Series(...)

```python
b = Series([2, np.nan, 1, np.nan], index=['a', 'b', 'd', 'e'])
```

### Step 3: Assign result = a.divmod(...)

```python
result = a.divmod(b)
```

### Step 4: Assign expected = divmod(...)

```python
expected = divmod(a, b)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result[0], expected[0])
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result[1], expected[1])
```

### Step 7: Assign result = a.rdivmod(...)

```python
result = a.rdivmod(b)
```

### Step 8: Assign expected = divmod(...)

```python
expected = divmod(b, a)
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result[0], expected[0])
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result[1], expected[1])
```


## Complete Example

```python
# Workflow
a = Series([1, 1, 1, np.nan], index=['a', 'b', 'c', 'd'])
b = Series([2, np.nan, 1, np.nan], index=['a', 'b', 'd', 'e'])
result = a.divmod(b)
expected = divmod(a, b)
tm.assert_series_equal(result[0], expected[0])
tm.assert_series_equal(result[1], expected[1])
result = a.rdivmod(b)
expected = divmod(b, a)
tm.assert_series_equal(result[0], expected[0])
tm.assert_series_equal(result[1], expected[1])
```

## Next Steps


---

*Source: test_arithmetic.py:194 | Complexity: Advanced | Last updated: 2026-06-02*