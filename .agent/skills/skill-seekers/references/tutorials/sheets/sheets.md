# How To: Sheets

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test sheets

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
# Fixtures: frame, path
```

## Step-by-Step Guide

### Step 1: Assign unit = get_exp_unit(...)

```python
unit = get_exp_unit(path)
```

**Verification:**
```python
assert 2 == len(reader.sheet_names)
```

### Step 2: Assign tsframe = DataFrame(...)

```python
tsframe = DataFrame(np.random.default_rng(2).standard_normal((5, 4)), columns=Index(list('ABCD')), index=date_range('2000-01-01', periods=5, freq='B'))
```

**Verification:**
```python
assert 'test1' == reader.sheet_names[0]
```

### Step 3: Assign index = pd.DatetimeIndex(...)

```python
index = pd.DatetimeIndex(np.asarray(tsframe.index), freq=None)
```

**Verification:**
```python
assert 'test2' == reader.sheet_names[1]
```

### Step 4: Assign tsframe.index = index

```python
tsframe.index = index
```

### Step 5: Assign expected = value

```python
expected = tsframe[:]
```

### Step 6: Assign expected.index = expected.index.as_unit(...)

```python
expected.index = expected.index.as_unit(unit)
```

### Step 7: Assign frame = frame.copy(...)

```python
frame = frame.copy()
```

### Step 8: Assign unknown = value

```python
frame.iloc[:5, frame.columns.get_loc('A')] = np.nan
```

### Step 9: Call frame.to_excel()

```python
frame.to_excel(path, sheet_name='test1')
```

### Step 10: Call frame.to_excel()

```python
frame.to_excel(path, sheet_name='test1', columns=['A', 'B'])
```

### Step 11: Call frame.to_excel()

```python
frame.to_excel(path, sheet_name='test1', header=False)
```

### Step 12: Call frame.to_excel()

```python
frame.to_excel(path, sheet_name='test1', index=False)
```

### Step 13: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(expected, recons)
```

**Verification:**
```python
assert 2 == len(reader.sheet_names)
```

### Step 14: Call frame.to_excel()

```python
frame.to_excel(writer, sheet_name='test1')
```

### Step 15: Call tsframe.to_excel()

```python
tsframe.to_excel(writer, sheet_name='test2')
```

### Step 16: Assign recons = pd.read_excel(...)

```python
recons = pd.read_excel(reader, sheet_name='test1', index_col=0)
```

### Step 17: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(frame, recons)
```

### Step 18: Assign recons = pd.read_excel(...)

```python
recons = pd.read_excel(reader, sheet_name='test2', index_col=0)
```


## Complete Example

```python
# Setup
# Fixtures: frame, path

# Workflow
unit = get_exp_unit(path)
tsframe = DataFrame(np.random.default_rng(2).standard_normal((5, 4)), columns=Index(list('ABCD')), index=date_range('2000-01-01', periods=5, freq='B'))
index = pd.DatetimeIndex(np.asarray(tsframe.index), freq=None)
tsframe.index = index
expected = tsframe[:]
expected.index = expected.index.as_unit(unit)
frame = frame.copy()
frame.iloc[:5, frame.columns.get_loc('A')] = np.nan
frame.to_excel(path, sheet_name='test1')
frame.to_excel(path, sheet_name='test1', columns=['A', 'B'])
frame.to_excel(path, sheet_name='test1', header=False)
frame.to_excel(path, sheet_name='test1', index=False)
with ExcelWriter(path) as writer:
    frame.to_excel(writer, sheet_name='test1')
    tsframe.to_excel(writer, sheet_name='test2')
with ExcelFile(path) as reader:
    recons = pd.read_excel(reader, sheet_name='test1', index_col=0)
    tm.assert_frame_equal(frame, recons)
    recons = pd.read_excel(reader, sheet_name='test2', index_col=0)
tm.assert_frame_equal(expected, recons)
assert 2 == len(reader.sheet_names)
assert 'test1' == reader.sheet_names[0]
assert 'test2' == reader.sheet_names[1]
```

## Next Steps


---

*Source: test_writers.py:558 | Complexity: Advanced | Last updated: 2026-06-02*