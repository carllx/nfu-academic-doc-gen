# How To: Read Empty With Blank Row

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test read empty with blank row

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
path = datapath('io', 'data', 'excel', f'empty_with_blank_row{ext}')
```

### Step 2: Assign expected = DataFrame(...)

```python
expected = DataFrame()
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
path = datapath('io', 'data', 'excel', f'empty_with_blank_row{ext}')
if read_only is None:
    result = pd.read_excel(path)
else:
    with contextlib.closing(openpyxl.load_workbook(path, read_only=read_only)) as wb:
        result = pd.read_excel(wb, engine='openpyxl')
expected = DataFrame()
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_openpyxl.py:390 | Complexity: Intermediate | Last updated: 2026-06-02*