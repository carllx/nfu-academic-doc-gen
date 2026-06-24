# How To: Read With Empty Trailing Rows

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test read with empty trailing rows

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `contextlib`
- `pathlib`
- `re`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.io.excel`
- `pandas.io.excel._openpyxl`
- `openpyxl`
- `pandas.io.formats.excel`

**Setup Required:**
```python
# Fixtures: datapath, ext, read_only
```

## Step-by-Step Guide

### Step 1: Assign path = datapath(...)

```python
path = datapath('io', 'data', 'excel', f'empty_trailing_rows{ext}')
```

### Step 2: Assign expected = DataFrame(...)

```python
expected = DataFrame({'Title': [np.nan, 'A', 1, 2, 3], 'Unnamed: 1': [np.nan, 'B', 4, 5, 6], 'Unnamed: 2': [np.nan, 'C', 7, 8, 9]})
```

### Step 3: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 4: Assign result = pd.read_excel(...)

```python
result = pd.read_excel(path)
```

### Step 5: Assign result = pd.read_excel(...)

```python
result = pd.read_excel(wb, engine='openpyxl')
```


## Complete Example

```python
# Setup
# Fixtures: datapath, ext, read_only

# Workflow
path = datapath('io', 'data', 'excel', f'empty_trailing_rows{ext}')
if read_only is None:
    result = pd.read_excel(path)
else:
    with contextlib.closing(openpyxl.load_workbook(path, read_only=read_only)) as wb:
        result = pd.read_excel(wb, engine='openpyxl')
expected = DataFrame({'Title': [np.nan, 'A', 1, 2, 3], 'Unnamed: 1': [np.nan, 'B', 4, 5, 6], 'Unnamed: 2': [np.nan, 'C', 7, 8, 9]})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_openpyxl.py:368 | Complexity: Intermediate | Last updated: 2026-06-02*