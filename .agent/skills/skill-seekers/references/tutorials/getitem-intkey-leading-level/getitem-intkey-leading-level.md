# How To: Getitem Intkey Leading Level

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test getitem intkey leading level

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: multiindex_year_month_day_dataframe_random_data, dtype
```

## Step-by-Step Guide

### Step 1: Assign ymd = multiindex_year_month_day_dataframe_random_data

```python
ymd = multiindex_year_month_day_dataframe_random_data
```

**Verification:**
```python
assert isinstance(mi, MultiIndex)
```

### Step 2: Assign levels = value

```python
levels = ymd.index.levels
```

**Verification:**
```python
assert mi.levels[0].dtype == np.dtype(int)
```

### Step 3: Assign ymd.index = ymd.index.set_levels(...)

```python
ymd.index = ymd.index.set_levels([levels[0].astype(dtype)] + levels[1:])
```

**Verification:**
```python
assert mi.levels[0].dtype == np.float64
```

### Step 4: Assign ser = value

```python
ser = ymd['A']
```

**Verification:**
```python
assert 14 not in mi.levels[0]
```

### Step 5: Assign mi = value

```python
mi = ser.index
```

**Verification:**
```python
assert not mi.levels[0]._should_fallback_to_positional
```

### Step 6: ser[14]

```python
ser[14]
```

**Verification:**
```python
assert not mi._should_fallback_to_positional
```


## Complete Example

```python
# Setup
# Fixtures: multiindex_year_month_day_dataframe_random_data, dtype

# Workflow
ymd = multiindex_year_month_day_dataframe_random_data
levels = ymd.index.levels
ymd.index = ymd.index.set_levels([levels[0].astype(dtype)] + levels[1:])
ser = ymd['A']
mi = ser.index
assert isinstance(mi, MultiIndex)
if dtype is int:
    assert mi.levels[0].dtype == np.dtype(int)
else:
    assert mi.levels[0].dtype == np.float64
assert 14 not in mi.levels[0]
assert not mi.levels[0]._should_fallback_to_positional
assert not mi._should_fallback_to_positional
with pytest.raises(KeyError, match='14'):
    ser[14]
```

## Next Steps


---

*Source: test_partial.py:161 | Complexity: Intermediate | Last updated: 2026-06-02*