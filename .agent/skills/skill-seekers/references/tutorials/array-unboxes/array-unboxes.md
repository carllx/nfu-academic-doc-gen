# How To: Array Unboxes

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test array unboxes

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `decimal`
- `re`
- `numpy`
- `pytest`
- `pytz`
- `pandas._config`
- `pandas`
- `pandas._testing`
- `pandas.api.extensions`
- `pandas.arrays`
- `pandas.core.arrays`
- `pandas.tests.extension.decimal`

**Setup Required:**
```python
# Fixtures: index_or_series
```

## Step-by-Step Guide

### Step 1: Assign box = index_or_series

```python
box = index_or_series
```

### Step 2: Assign data = box(...)

```python
data = box([decimal.Decimal('1'), decimal.Decimal('2')])
```

### Step 3: Assign dtype = DecimalDtype2(...)

```python
dtype = DecimalDtype2()
```

### Step 4: Assign result = pd.array(...)

```python
result = pd.array(data, dtype='decimal2')
```

### Step 5: Assign expected = DecimalArray2._from_sequence(...)

```python
expected = DecimalArray2._from_sequence(data.values, dtype=dtype)
```

### Step 6: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```

### Step 7: Call DecimalArray2._from_sequence()

```python
DecimalArray2._from_sequence(data, dtype=dtype)
```


## Complete Example

```python
# Setup
# Fixtures: index_or_series

# Workflow
box = index_or_series
data = box([decimal.Decimal('1'), decimal.Decimal('2')])
dtype = DecimalDtype2()
with pytest.raises(TypeError, match='scalars should not be of type pd.Series or pd.Index'):
    DecimalArray2._from_sequence(data, dtype=dtype)
result = pd.array(data, dtype='decimal2')
expected = DecimalArray2._from_sequence(data.values, dtype=dtype)
tm.assert_equal(result, expected)
```

## Next Steps


---

*Source: test_array.py:498 | Complexity: Intermediate | Last updated: 2026-06-02*