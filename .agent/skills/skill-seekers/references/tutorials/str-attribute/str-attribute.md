# How To: Str Attribute

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test str attribute

## Prerequisites

**Required Modules:**
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign methods = value

```python
methods = ['strip', 'rstrip', 'lstrip']
```

### Step 2: Assign ser = Series(...)

```python
ser = Series([' jack', 'jill ', ' jesse ', 'frank'])
```

### Step 3: Assign ser = Series(...)

```python
ser = Series(range(5))
```

### Step 4: Assign expected = Series(...)

```python
expected = Series([getattr(str, method)(x) for x in ser.values])
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(getattr(Series.str, method)(ser.str), expected)
```

### Step 6: Call ser.str.repeat()

```python
ser.str.repeat(2)
```


## Complete Example

```python
# Workflow
methods = ['strip', 'rstrip', 'lstrip']
ser = Series([' jack', 'jill ', ' jesse ', 'frank'])
for method in methods:
    expected = Series([getattr(str, method)(x) for x in ser.values])
    tm.assert_series_equal(getattr(Series.str, method)(ser.str), expected)
ser = Series(range(5))
with pytest.raises(AttributeError, match='only use .str accessor'):
    ser.str.repeat(2)
```

## Next Steps


---

*Source: test_str_accessor.py:8 | Complexity: Intermediate | Last updated: 2026-06-02*