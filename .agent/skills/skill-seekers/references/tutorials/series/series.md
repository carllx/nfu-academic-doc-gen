# How To: Series

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test series

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas.compat`
- `pandas`
- `pandas`
- `pandas.tests.io.pytables.common`
- `pandas.util`

**Setup Required:**
```python
# Fixtures: setup_path
```

## Step-by-Step Guide

### Step 1: Assign s = Series(...)

```python
s = Series(range(10), dtype='float64', index=[f'i_{i}' for i in range(10)])
```

### Step 2: Call _check_roundtrip()

```python
_check_roundtrip(s, tm.assert_series_equal, path=setup_path)
```

### Step 3: Assign ts = Series(...)

```python
ts = Series(np.arange(10, dtype=np.float64), index=date_range('2020-01-01', periods=10))
```

### Step 4: Call _check_roundtrip()

```python
_check_roundtrip(ts, tm.assert_series_equal, path=setup_path)
```

### Step 5: Assign ts2 = Series(...)

```python
ts2 = Series(ts.index, Index(ts.index))
```

### Step 6: Call _check_roundtrip()

```python
_check_roundtrip(ts2, tm.assert_series_equal, path=setup_path)
```

### Step 7: Assign ts3 = Series(...)

```python
ts3 = Series(ts.values, Index(np.asarray(ts.index)))
```

### Step 8: Call _check_roundtrip()

```python
_check_roundtrip(ts3, tm.assert_series_equal, path=setup_path, check_index_type=False)
```


## Complete Example

```python
# Setup
# Fixtures: setup_path

# Workflow
s = Series(range(10), dtype='float64', index=[f'i_{i}' for i in range(10)])
_check_roundtrip(s, tm.assert_series_equal, path=setup_path)
ts = Series(np.arange(10, dtype=np.float64), index=date_range('2020-01-01', periods=10))
_check_roundtrip(ts, tm.assert_series_equal, path=setup_path)
ts2 = Series(ts.index, Index(ts.index))
_check_roundtrip(ts2, tm.assert_series_equal, path=setup_path)
ts3 = Series(ts.values, Index(np.asarray(ts.index)))
_check_roundtrip(ts3, tm.assert_series_equal, path=setup_path, check_index_type=False)
```

## Next Steps


---

*Source: test_round_trip.py:263 | Complexity: Advanced | Last updated: 2026-06-02*