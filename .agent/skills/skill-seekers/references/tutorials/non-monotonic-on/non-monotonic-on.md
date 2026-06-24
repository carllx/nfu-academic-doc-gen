# How To: Non Monotonic On

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test non monotonic on

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`
- `pandas.tseries`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'A': date_range('20130101', periods=5, freq='s'), 'B': range(5)})
```

**Verification:**
```python
assert not df.index.is_monotonic_increasing
```

### Step 2: Assign df = df.set_index(...)

```python
df = df.set_index('A')
```

### Step 3: Assign non_monotonic_index = df.index.to_list(...)

```python
non_monotonic_index = df.index.to_list()
```

### Step 4: Assign unknown = value

```python
non_monotonic_index[0] = non_monotonic_index[3]
```

### Step 5: Assign df.index = non_monotonic_index

```python
df.index = non_monotonic_index
```

**Verification:**
```python
assert not df.index.is_monotonic_increasing
```

### Step 6: Assign msg = 'index values must be monotonic'

```python
msg = 'index values must be monotonic'
```

### Step 7: Assign df = df.reset_index(...)

```python
df = df.reset_index()
```

### Step 8: Assign msg = 'invalid on specified as A, must be a column \\(of DataFrame\\), an Index or None'

```python
msg = 'invalid on specified as A, must be a column \\(of DataFrame\\), an Index or None'
```

### Step 9: Call df.rolling.sum()

```python
df.rolling('2s').sum()
```

### Step 10: Call df.rolling.sum()

```python
df.rolling('2s', on='A').sum()
```


## Complete Example

```python
# Workflow
df = DataFrame({'A': date_range('20130101', periods=5, freq='s'), 'B': range(5)})
df = df.set_index('A')
non_monotonic_index = df.index.to_list()
non_monotonic_index[0] = non_monotonic_index[3]
df.index = non_monotonic_index
assert not df.index.is_monotonic_increasing
msg = 'index values must be monotonic'
with pytest.raises(ValueError, match=msg):
    df.rolling('2s').sum()
df = df.reset_index()
msg = 'invalid on specified as A, must be a column \\(of DataFrame\\), an Index or None'
with pytest.raises(ValueError, match=msg):
    df.rolling('2s', on='A').sum()
```

## Next Steps


---

*Source: test_timeseries_window.py:127 | Complexity: Advanced | Last updated: 2026-06-02*