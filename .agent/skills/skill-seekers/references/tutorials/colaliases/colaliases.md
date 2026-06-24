# How To: Colaliases

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test colaliases

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

### Step 1: Assign frame = frame.copy(...)

```python
frame = frame.copy()
```

### Step 2: Assign unknown = value

```python
frame.iloc[:5, frame.columns.get_loc('A')] = np.nan
```

### Step 3: Call frame.to_excel()

```python
frame.to_excel(path, sheet_name='test1')
```

### Step 4: Call frame.to_excel()

```python
frame.to_excel(path, sheet_name='test1', columns=['A', 'B'])
```

### Step 5: Call frame.to_excel()

```python
frame.to_excel(path, sheet_name='test1', header=False)
```

### Step 6: Call frame.to_excel()

```python
frame.to_excel(path, sheet_name='test1', index=False)
```

### Step 7: Assign col_aliases = Index(...)

```python
col_aliases = Index(['AA', 'X', 'Y', 'Z'])
```

### Step 8: Call frame.to_excel()

```python
frame.to_excel(path, sheet_name='test1', header=col_aliases)
```

### Step 9: Assign xp = frame.copy(...)

```python
xp = frame.copy()
```

### Step 10: Assign xp.columns = col_aliases

```python
xp.columns = col_aliases
```

### Step 11: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(xp, rs)
```

### Step 12: Assign rs = pd.read_excel(...)

```python
rs = pd.read_excel(reader, sheet_name='test1', index_col=0)
```


## Complete Example

```python
# Setup
# Fixtures: frame, path

# Workflow
frame = frame.copy()
frame.iloc[:5, frame.columns.get_loc('A')] = np.nan
frame.to_excel(path, sheet_name='test1')
frame.to_excel(path, sheet_name='test1', columns=['A', 'B'])
frame.to_excel(path, sheet_name='test1', header=False)
frame.to_excel(path, sheet_name='test1', index=False)
col_aliases = Index(['AA', 'X', 'Y', 'Z'])
frame.to_excel(path, sheet_name='test1', header=col_aliases)
with ExcelFile(path) as reader:
    rs = pd.read_excel(reader, sheet_name='test1', index_col=0)
xp = frame.copy()
xp.columns = col_aliases
tm.assert_frame_equal(xp, rs)
```

## Next Steps


---

*Source: test_writers.py:593 | Complexity: Advanced | Last updated: 2026-06-02*