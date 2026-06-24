# How To: Creating And Reading Multiple Sheets

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test creating and reading multiple sheets

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
# Fixtures: ext
```

## Step-by-Step Guide

### Step 1: Assign sheets = value

```python
sheets = ['AAA', 'BBB', 'CCC']
```

### Step 2: Assign dfs = value

```python
dfs = [tdf(s) for s in sheets]
```

### Step 3: Assign dfs = dict(...)

```python
dfs = dict(zip(sheets, dfs))
```

### Step 4: Assign unknown = value

```python
d, i = ([11, 22, 33], [1, 2, 3])
```

### Step 5: Assign dfs_returned = pd.read_excel(...)

```python
dfs_returned = pd.read_excel(pth, sheet_name=sheets, index_col=0)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(dfs[s], dfs_returned[s])
```

### Step 7: Call df.to_excel()

```python
df.to_excel(ew, sheet_name=sheetname)
```


## Complete Example

```python
# Setup
# Fixtures: ext

# Workflow
def tdf(col_sheet_name):
    d, i = ([11, 22, 33], [1, 2, 3])
    return DataFrame(d, i, columns=[col_sheet_name])
sheets = ['AAA', 'BBB', 'CCC']
dfs = [tdf(s) for s in sheets]
dfs = dict(zip(sheets, dfs))
with tm.ensure_clean(ext) as pth:
    with ExcelWriter(pth) as ew:
        for sheetname, df in dfs.items():
            df.to_excel(ew, sheet_name=sheetname)
    dfs_returned = pd.read_excel(pth, sheet_name=sheets, index_col=0)
    for s in sheets:
        tm.assert_frame_equal(dfs[s], dfs_returned[s])
```

## Next Steps


---

*Source: test_writers.py:156 | Complexity: Intermediate | Last updated: 2026-06-02*