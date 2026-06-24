# How To: Basic Getitem Setitem Corner

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test basic getitem setitem corner

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.errors`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: datetime_series
```

## Step-by-Step Guide

### Step 1: Assign msg = 'key of type tuple not found and not a MultiIndex'

```python
msg = 'key of type tuple not found and not a MultiIndex'
```

### Step 2: Assign msg = 'Indexing with a single-item list'

```python
msg = 'Indexing with a single-item list'
```

### Step 3: Assign result = value

```python
result = datetime_series[slice(None, 5),]
```

### Step 4: Assign expected = value

```python
expected = datetime_series[:5]
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 6: Assign msg = "unhashable type(: 'slice')?"

```python
msg = "unhashable type(: 'slice')?"
```

### Step 7: datetime_series[:, 2]

```python
datetime_series[:, 2]
```

### Step 8: Assign unknown = 2

```python
datetime_series[:, 2] = 2
```

### Step 9: datetime_series[[slice(None, 5)]]

```python
datetime_series[[slice(None, 5)]]
```

### Step 10: datetime_series[[5, [None, None]]]

```python
datetime_series[[5, [None, None]]]
```

### Step 11: Assign unknown = 2

```python
datetime_series[[5, [None, None]]] = 2
```


## Complete Example

```python
# Setup
# Fixtures: datetime_series

# Workflow
msg = 'key of type tuple not found and not a MultiIndex'
with pytest.raises(KeyError, match=msg):
    datetime_series[:, 2]
with pytest.raises(KeyError, match=msg):
    datetime_series[:, 2] = 2
msg = 'Indexing with a single-item list'
with pytest.raises(ValueError, match=msg):
    datetime_series[[slice(None, 5)]]
result = datetime_series[slice(None, 5),]
expected = datetime_series[:5]
tm.assert_series_equal(result, expected)
msg = "unhashable type(: 'slice')?"
with pytest.raises(TypeError, match=msg):
    datetime_series[[5, [None, None]]]
with pytest.raises(TypeError, match=msg):
    datetime_series[[5, [None, None]]] = 2
```

## Next Steps


---

*Source: test_indexing.py:218 | Complexity: Advanced | Last updated: 2026-06-02*