# How To: Ts Frame

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test ts frame

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `functools`
- `io`
- `os`
- `re`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.compat._constants`
- `pandas.compat._optional`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.io.excel`
- `pandas.io.excel._util`

**Setup Required:**
```python
# Fixtures: path
```

## Step-by-Step Guide

### Step 1: Assign unit = get_exp_unit(...)

```python
unit = get_exp_unit(path)
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((5, 4)), columns=Index(list('ABCD')), index=date_range('2000-01-01', periods=5, freq='B'))
```

### Step 3: Assign index = pd.DatetimeIndex(...)

```python
index = pd.DatetimeIndex(np.asarray(df.index), freq=None)
```

### Step 4: Assign df.index = index

```python
df.index = index
```

### Step 5: Assign expected = value

```python
expected = df[:]
```

### Step 6: Assign expected.index = expected.index.as_unit(...)

```python
expected.index = expected.index.as_unit(unit)
```

### Step 7: Call df.to_excel()

```python
df.to_excel(path, sheet_name='test1')
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(expected, recons)
```

### Step 9: Assign recons = pd.read_excel(...)

```python
recons = pd.read_excel(reader, sheet_name='test1', index_col=0)
```


## Complete Example

```python
# Setup
# Fixtures: path

# Workflow
unit = get_exp_unit(path)
df = DataFrame(np.random.default_rng(2).standard_normal((5, 4)), columns=Index(list('ABCD')), index=date_range('2000-01-01', periods=5, freq='B'))
index = pd.DatetimeIndex(np.asarray(df.index), freq=None)
df.index = index
expected = df[:]
expected.index = expected.index.as_unit(unit)
df.to_excel(path, sheet_name='test1')
with ExcelFile(path) as reader:
    recons = pd.read_excel(reader, sheet_name='test1', index_col=0)
tm.assert_frame_equal(expected, recons)
```

## Next Steps


---

*Source: test_writers.py:478 | Complexity: Advanced | Last updated: 2026-06-02*