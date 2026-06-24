# How To: Reading Multiple Specific Sheets

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test reading multiple specific sheets

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `datetime`
- `functools`
- `io`
- `os`
- `pathlib`
- `platform`
- `re`
- `urllib.error`
- `zipfile`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `s3fs`
- `py.path`
- `pyarrow`
- `pandas.arrays`
- `xlrd`
- `xlrd`
- `python_calamine`
- `python_calamine`

**Setup Required:**
```python
# Fixtures: read_ext
```

## Step-by-Step Guide

### Step 1: Assign basename = 'test_multisheet'

```python
basename = 'test_multisheet'
```

**Verification:**
```python
assert len(expected_keys) == len(dfs.keys())
```

### Step 2: Assign expected_keys = value

```python
expected_keys = [2, 'Charlie', 'Charlie']
```

### Step 3: Assign dfs = pd.read_excel(...)

```python
dfs = pd.read_excel(basename + read_ext, sheet_name=expected_keys)
```

### Step 4: Assign expected_keys = list(...)

```python
expected_keys = list(set(expected_keys))
```

### Step 5: Call tm.assert_contains_all()

```python
tm.assert_contains_all(expected_keys, dfs.keys())
```

**Verification:**
```python
assert len(expected_keys) == len(dfs.keys())
```


## Complete Example

```python
# Setup
# Fixtures: read_ext

# Workflow
basename = 'test_multisheet'
expected_keys = [2, 'Charlie', 'Charlie']
dfs = pd.read_excel(basename + read_ext, sheet_name=expected_keys)
expected_keys = list(set(expected_keys))
tm.assert_contains_all(expected_keys, dfs.keys())
assert len(expected_keys) == len(dfs.keys())
```

## Next Steps


---

*Source: test_readers.py:749 | Complexity: Intermediate | Last updated: 2026-06-02*