# How To: Arrow String Multiplication

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test arrow string multiplication

## Prerequisites

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


## Step-by-Step Guide

### Step 1: Assign binary = pd.Series(...)

```python
binary = pd.Series(['abc', 'defg'], dtype=ArrowDtype(pa.string()))
```

### Step 2: Assign repeat = pd.Series(...)

```python
repeat = pd.Series([2, -2], dtype='int64[pyarrow]')
```

### Step 3: Assign result = value

```python
result = binary * repeat
```

### Step 4: Assign expected = pd.Series(...)

```python
expected = pd.Series(['abcabc', ''], dtype=ArrowDtype(pa.string()))
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 6: Assign reflected_result = value

```python
reflected_result = repeat * binary
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, reflected_result)
```


## Complete Example

```python
# Workflow
binary = pd.Series(['abc', 'defg'], dtype=ArrowDtype(pa.string()))
repeat = pd.Series([2, -2], dtype='int64[pyarrow]')
result = binary * repeat
expected = pd.Series(['abcabc', ''], dtype=ArrowDtype(pa.string()))
tm.assert_series_equal(result, expected)
reflected_result = repeat * binary
tm.assert_series_equal(result, reflected_result)
```

## Next Steps


---

*Source: test_arrow.py:1306 | Complexity: Intermediate | Last updated: 2026-06-02*