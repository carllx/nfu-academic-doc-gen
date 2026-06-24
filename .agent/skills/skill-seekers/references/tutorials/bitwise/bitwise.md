# How To: Bitwise

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test bitwise

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `datetime`
- `decimal`
- `io`
- `operator`
- `pickle`
- `re`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas._libs.tslibs`
- `pandas.compat`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas._testing`
- `pandas.api.extensions`
- `pandas.api.types`
- `pandas.tests.extension`
- `pandas.core.arrays.arrow.array`
- `pandas.core.arrays.arrow.extension_types`

**Setup Required:**
```python
# Fixtures: pa_type
```

## Step-by-Step Guide

### Step 1: Assign dtype = ArrowDtype(...)

```python
dtype = ArrowDtype(pa_type)
```

### Step 2: Assign left = pd.Series(...)

```python
left = pd.Series([1, None, 3, 4], dtype=dtype)
```

### Step 3: Assign right = pd.Series(...)

```python
right = pd.Series([None, 3, 5, 4], dtype=dtype)
```

### Step 4: Assign result = value

```python
result = left | right
```

### Step 5: Assign expected = pd.Series(...)

```python
expected = pd.Series([None, None, 3 | 5, 4 | 4], dtype=dtype)
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 7: Assign result = value

```python
result = left & right
```

### Step 8: Assign expected = pd.Series(...)

```python
expected = pd.Series([None, None, 3 & 5, 4 & 4], dtype=dtype)
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 10: Assign result = value

```python
result = left ^ right
```

### Step 11: Assign expected = pd.Series(...)

```python
expected = pd.Series([None, None, 3 ^ 5, 4 ^ 4], dtype=dtype)
```

### Step 12: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 13: Assign result = value

```python
result = ~left
```

### Step 14: Assign expected = value

```python
expected = ~left.fillna(0).to_numpy()
```

### Step 15: Assign expected = pd.Series.mask(...)

```python
expected = pd.Series(expected, dtype=dtype).mask(left.isnull())
```

### Step 16: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: pa_type

# Workflow
dtype = ArrowDtype(pa_type)
left = pd.Series([1, None, 3, 4], dtype=dtype)
right = pd.Series([None, 3, 5, 4], dtype=dtype)
result = left | right
expected = pd.Series([None, None, 3 | 5, 4 | 4], dtype=dtype)
tm.assert_series_equal(result, expected)
result = left & right
expected = pd.Series([None, None, 3 & 5, 4 & 4], dtype=dtype)
tm.assert_series_equal(result, expected)
result = left ^ right
expected = pd.Series([None, None, 3 ^ 5, 4 ^ 4], dtype=dtype)
tm.assert_series_equal(result, expected)
result = ~left
expected = ~left.fillna(0).to_numpy()
expected = pd.Series(expected, dtype=dtype).mask(left.isnull())
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_arrow.py:1256 | Complexity: Advanced | Last updated: 2026-06-02*