# How To: Read With Bad Dimension

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test read with bad dimension

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
# Fixtures: datapath, ext, header, expected_data, filename, read_only
```

## Step-by-Step Guide

### Step 1: Assign path = datapath(...)

```python
path = datapath('io', 'data', 'excel', f'{filename}{ext}')
```

### Step 2: Assign expected = DataFrame(...)

```python
expected = DataFrame(expected_data)
```

### Step 3: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 4: Assign result = pd.read_excel(...)

```python
result = pd.read_excel(path, header=header)
```

### Step 5: Assign result = pd.read_excel(...)

```python
result = pd.read_excel(wb, engine='openpyxl', header=header)
```


## Complete Example

```python
# Setup
# Fixtures: datapath, ext, header, expected_data, filename, read_only

# Workflow
path = datapath('io', 'data', 'excel', f'{filename}{ext}')
if read_only is None:
    result = pd.read_excel(path, header=header)
else:
    with contextlib.closing(openpyxl.load_workbook(path, read_only=read_only)) as wb:
        result = pd.read_excel(wb, engine='openpyxl', header=header)
expected = DataFrame(expected_data)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_openpyxl.py:329 | Complexity: Intermediate | Last updated: 2026-06-02*