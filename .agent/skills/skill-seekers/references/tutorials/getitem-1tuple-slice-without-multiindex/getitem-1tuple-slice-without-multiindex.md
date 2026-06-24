# How To: Getitem 1Tuple Slice Without Multiindex

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test getitem 1tuple slice without multiindex

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.indexing`
- `pandas.tseries.offsets`


## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series(range(5))
```

### Step 2: Assign key = value

```python
key = (slice(3),)
```

### Step 3: Assign result = value

```python
result = ser[key]
```

### Step 4: Assign expected = value

```python
expected = ser[key[0]]
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
ser = Series(range(5))
key = (slice(3),)
result = ser[key]
expected = ser[key[0]]
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_getitem.py:621 | Complexity: Intermediate | Last updated: 2026-06-02*