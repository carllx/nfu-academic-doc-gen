# How To: Int Types

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test int types

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
# Fixtures: np_type, path
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).integers(-10, 10, size=(10, 2)), dtype=np_type)
```

### Step 2: Call df.to_excel()

```python
df.to_excel(path, sheet_name='test1')
```

### Step 3: Assign int_frame = df.astype(...)

```python
int_frame = df.astype(np.int64)
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(int_frame, recons)
```

### Step 5: Assign recons2 = pd.read_excel(...)

```python
recons2 = pd.read_excel(path, sheet_name='test1', index_col=0)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(int_frame, recons2)
```

### Step 7: Assign recons = pd.read_excel(...)

```python
recons = pd.read_excel(reader, sheet_name='test1', index_col=0)
```


## Complete Example

```python
# Setup
# Fixtures: np_type, path

# Workflow
df = DataFrame(np.random.default_rng(2).integers(-10, 10, size=(10, 2)), dtype=np_type)
df.to_excel(path, sheet_name='test1')
with ExcelFile(path) as reader:
    recons = pd.read_excel(reader, sheet_name='test1', index_col=0)
int_frame = df.astype(np.int64)
tm.assert_frame_equal(int_frame, recons)
recons2 = pd.read_excel(path, sheet_name='test1', index_col=0)
tm.assert_frame_equal(int_frame, recons2)
```

## Next Steps


---

*Source: test_writers.py:507 | Complexity: Intermediate | Last updated: 2026-06-02*