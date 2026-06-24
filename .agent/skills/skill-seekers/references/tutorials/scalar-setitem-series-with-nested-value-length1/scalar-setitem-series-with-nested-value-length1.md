# How To: Scalar Setitem Series With Nested Value Length1

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test scalar setitem series with nested value length1

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `array`
- `datetime`
- `re`
- `weakref`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.indexing.common`
- `pandas.tests.indexing.test_floats`

**Setup Required:**
```python
# Fixtures: value, indexer_sli
```

## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series([1.0, 2.0, 3.0])
```

**Verification:**
```python
assert (ser.loc[0] == value).all()
```

### Step 2: Assign ser = Series(...)

```python
ser = Series([1, 'a', 'b'], dtype=object)
```

**Verification:**
```python
assert ser.loc[0] == value
```

### Step 3: Assign unknown = value

```python
indexer_sli(ser)[0] = value
```

### Step 4: Assign unknown = value

```python
indexer_sli(ser)[0] = value
```

### Step 5: Assign expected = Series(...)

```python
expected = Series([0.0, 2.0, 3.0])
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ser, expected)
```

**Verification:**
```python
assert (ser.loc[0] == value).all()
```

### Step 7: Assign unknown = value

```python
indexer_sli(ser)[0] = value
```


## Complete Example

```python
# Setup
# Fixtures: value, indexer_sli

# Workflow
ser = Series([1.0, 2.0, 3.0])
if isinstance(value, np.ndarray):
    indexer_sli(ser)[0] = value
    expected = Series([0.0, 2.0, 3.0])
    tm.assert_series_equal(ser, expected)
else:
    with pytest.raises(ValueError, match='setting an array element with a sequence'):
        indexer_sli(ser)[0] = value
ser = Series([1, 'a', 'b'], dtype=object)
indexer_sli(ser)[0] = value
if isinstance(value, np.ndarray):
    assert (ser.loc[0] == value).all()
else:
    assert ser.loc[0] == value
```

## Next Steps


---

*Source: test_indexing.py:1120 | Complexity: Intermediate | Last updated: 2026-06-02*