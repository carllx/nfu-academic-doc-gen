# How To: Isin Large Series Mixed Dtypes And Nan

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: mock, workflow, integration

## Overview

Workflow: test isin large series mixed dtypes and nan

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`
- `pandas.core.arrays`

**Setup Required:**
```python
# Fixtures: monkeypatch
```

## Step-by-Step Guide

### Step 1: Assign min_isin_comp = 5

```python
min_isin_comp = 5
```

### Step 2: Assign ser = Series(...)

```python
ser = Series([1, 2, np.nan] * min_isin_comp)
```

### Step 3: Assign expected = Series(...)

```python
expected = Series([False] * 3 * min_isin_comp)
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Call m.setattr()

```python
m.setattr(algorithms, '_MINIMUM_COMP_ARR_LEN', min_isin_comp)
```

### Step 6: Assign result = ser.isin(...)

```python
result = ser.isin({'foo', 'bar'})
```


## Complete Example

```python
# Setup
# Fixtures: monkeypatch

# Workflow
min_isin_comp = 5
ser = Series([1, 2, np.nan] * min_isin_comp)
with monkeypatch.context() as m:
    m.setattr(algorithms, '_MINIMUM_COMP_ARR_LEN', min_isin_comp)
    result = ser.isin({'foo', 'bar'})
expected = Series([False] * 3 * min_isin_comp)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_isin.py:201 | Complexity: Intermediate | Last updated: 2026-06-02*