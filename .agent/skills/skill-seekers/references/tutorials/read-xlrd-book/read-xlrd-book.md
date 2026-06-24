# How To: Read Xlrd Book

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test read xlrd book

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `io`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas`
- `pandas._testing`
- `pandas.io.excel`
- `pandas.io.excel._base`
- `xlrd.biffh`

**Setup Required:**
```python
# Fixtures: read_ext_xlrd, datapath
```

## Step-by-Step Guide

### Step 1: Assign engine = 'xlrd'

```python
engine = 'xlrd'
```

### Step 2: Assign sheet_name = 'Sheet1'

```python
sheet_name = 'Sheet1'
```

### Step 3: Assign pth = datapath(...)

```python
pth = datapath('io', 'data', 'excel', 'test1.xls')
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 5: Assign expected = pd.read_excel(...)

```python
expected = pd.read_excel(book, sheet_name=sheet_name, engine=engine, index_col=0)
```

### Step 6: Assign result = pd.read_excel(...)

```python
result = pd.read_excel(xl, sheet_name=sheet_name, index_col=0)
```


## Complete Example

```python
# Setup
# Fixtures: read_ext_xlrd, datapath

# Workflow
engine = 'xlrd'
sheet_name = 'Sheet1'
pth = datapath('io', 'data', 'excel', 'test1.xls')
with xlrd.open_workbook(pth) as book:
    with ExcelFile(book, engine=engine) as xl:
        result = pd.read_excel(xl, sheet_name=sheet_name, index_col=0)
    expected = pd.read_excel(book, sheet_name=sheet_name, engine=engine, index_col=0)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_xlrd.py:30 | Complexity: Intermediate | Last updated: 2026-06-02*