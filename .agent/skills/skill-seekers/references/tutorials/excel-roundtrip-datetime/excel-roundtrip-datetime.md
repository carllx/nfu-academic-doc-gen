# How To: Excel Roundtrip Datetime

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test excel roundtrip datetime

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
# Fixtures: merge_cells, path
```

## Step-by-Step Guide

### Step 1: Assign unit = get_exp_unit(...)

```python
unit = get_exp_unit(path)
```

### Step 2: Assign tsframe = DataFrame(...)

```python
tsframe = DataFrame(np.random.default_rng(2).standard_normal((5, 4)), columns=Index(list('ABCD')), index=date_range('2000-01-01', periods=5, freq='B'))
```

### Step 3: Assign index = pd.DatetimeIndex(...)

```python
index = pd.DatetimeIndex(np.asarray(tsframe.index), freq=None)
```

### Step 4: Assign tsframe.index = index

```python
tsframe.index = index
```

### Step 5: Assign tsf = tsframe.copy(...)

```python
tsf = tsframe.copy()
```

### Step 6: Assign tsf.index = value

```python
tsf.index = [x.date() for x in tsframe.index]
```

### Step 7: Call tsf.to_excel()

```python
tsf.to_excel(path, sheet_name='test1', merge_cells=merge_cells)
```

### Step 8: Assign expected = value

```python
expected = tsframe[:]
```

### Step 9: Assign expected.index = expected.index.as_unit(...)

```python
expected.index = expected.index.as_unit(unit)
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(expected, recons)
```

### Step 11: Assign recons = pd.read_excel(...)

```python
recons = pd.read_excel(reader, sheet_name='test1', index_col=0)
```


## Complete Example

```python
# Setup
# Fixtures: merge_cells, path

# Workflow
unit = get_exp_unit(path)
tsframe = DataFrame(np.random.default_rng(2).standard_normal((5, 4)), columns=Index(list('ABCD')), index=date_range('2000-01-01', periods=5, freq='B'))
index = pd.DatetimeIndex(np.asarray(tsframe.index), freq=None)
tsframe.index = index
tsf = tsframe.copy()
tsf.index = [x.date() for x in tsframe.index]
tsf.to_excel(path, sheet_name='test1', merge_cells=merge_cells)
with ExcelFile(path) as reader:
    recons = pd.read_excel(reader, sheet_name='test1', index_col=0)
expected = tsframe[:]
expected.index = expected.index.as_unit(unit)
tm.assert_frame_equal(expected, recons)
```

## Next Steps


---

*Source: test_writers.py:684 | Complexity: Advanced | Last updated: 2026-06-02*