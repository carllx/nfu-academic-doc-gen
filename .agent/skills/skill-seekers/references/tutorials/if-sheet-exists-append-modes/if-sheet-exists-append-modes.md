# How To: If Sheet Exists Append Modes

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test if sheet exists append modes

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
# Fixtures: ext, if_sheet_exists, num_sheets, expected
```

## Step-by-Step Guide

### Step 1: Assign df1 = DataFrame(...)

```python
df1 = DataFrame({'fruit': ['apple', 'banana']})
```

**Verification:**
```python
assert len(wb.sheetnames) == num_sheets
```

### Step 2: Assign df2 = DataFrame(...)

```python
df2 = DataFrame({'fruit': ['pear']})
```

**Verification:**
```python
assert wb.sheetnames[0] == 'foo'
```

### Step 3: Call df1.to_excel()

```python
df1.to_excel(f, engine='openpyxl', sheet_name='foo', index=False)
```

**Verification:**
```python
assert list(result['fruit']) == expected
```

### Step 4: Call df2.to_excel()

```python
df2.to_excel(writer, sheet_name='foo', index=False)
```

**Verification:**
```python
assert len(wb.sheetnames) == num_sheets
```

### Step 5: Assign result = pd.read_excel(...)

```python
result = pd.read_excel(wb, 'foo', engine='openpyxl')
```

**Verification:**
```python
assert list(result['fruit']) == expected
```

### Step 6: Assign result = pd.read_excel(...)

```python
result = pd.read_excel(wb, wb.sheetnames[1], engine='openpyxl')
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, df2)
```


## Complete Example

```python
# Setup
# Fixtures: ext, if_sheet_exists, num_sheets, expected

# Workflow
df1 = DataFrame({'fruit': ['apple', 'banana']})
df2 = DataFrame({'fruit': ['pear']})
with tm.ensure_clean(ext) as f:
    df1.to_excel(f, engine='openpyxl', sheet_name='foo', index=False)
    with ExcelWriter(f, engine='openpyxl', mode='a', if_sheet_exists=if_sheet_exists) as writer:
        df2.to_excel(writer, sheet_name='foo', index=False)
    with contextlib.closing(openpyxl.load_workbook(f)) as wb:
        assert len(wb.sheetnames) == num_sheets
        assert wb.sheetnames[0] == 'foo'
        result = pd.read_excel(wb, 'foo', engine='openpyxl')
        assert list(result['fruit']) == expected
        if len(wb.sheetnames) == 2:
            result = pd.read_excel(wb, wb.sheetnames[1], engine='openpyxl')
            tm.assert_frame_equal(result, df2)
```

## Next Steps


---

*Source: test_openpyxl.py:200 | Complexity: Intermediate | Last updated: 2026-06-02*