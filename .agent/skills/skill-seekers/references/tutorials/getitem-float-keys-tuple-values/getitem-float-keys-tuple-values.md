# How To: Getitem Float Keys Tuple Values

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test getitem float keys tuple values

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
ser = Series([(1, 1), (2, 2), (3, 3)], index=[0.0, 0.1, 0.2], name='foo')
```

**Verification:**
```python
assert result == (1, 1)
```

### Step 2: Assign result = value

```python
result = ser[0.0]
```

**Verification:**
```python
assert result == (1, 1)
```

### Step 3: Assign expected = Series(...)

```python
expected = Series([(1, 1), (2, 2)], index=[0.0, 0.0], name='foo')
```

### Step 4: Assign ser = Series(...)

```python
ser = Series([(1, 1), (2, 2), (3, 3)], index=[0.0, 0.0, 0.2], name='foo')
```

### Step 5: Assign result = value

```python
result = ser[0.0]
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
ser = Series([(1, 1), (2, 2), (3, 3)], index=[0.0, 0.1, 0.2], name='foo')
result = ser[0.0]
assert result == (1, 1)
expected = Series([(1, 1), (2, 2)], index=[0.0, 0.0], name='foo')
ser = Series([(1, 1), (2, 2), (3, 3)], index=[0.0, 0.0, 0.2], name='foo')
result = ser[0.0]
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_getitem.py:45 | Complexity: Intermediate | Last updated: 2026-06-02*