# How To: Arrow String Multiplication Scalar Repeat

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test arrow string multiplication scalar repeat

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

### Step 2: Assign result = value

```python
result = binary * 2
```

### Step 3: Assign expected = pd.Series(...)

```python
expected = pd.Series(['abcabc', 'defgdefg'], dtype=ArrowDtype(pa.string()))
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign reflected_result = value

```python
reflected_result = 2 * binary
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(reflected_result, expected)
```


## Complete Example

```python
# Workflow
binary = pd.Series(['abc', 'defg'], dtype=ArrowDtype(pa.string()))
result = binary * 2
expected = pd.Series(['abcabc', 'defgdefg'], dtype=ArrowDtype(pa.string()))
tm.assert_series_equal(result, expected)
reflected_result = 2 * binary
tm.assert_series_equal(reflected_result, expected)
```

## Next Steps


---

*Source: test_arrow.py:1317 | Complexity: Intermediate | Last updated: 2026-06-02*