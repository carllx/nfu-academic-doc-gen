# How To: Write Cells Merge Styled

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test write cells merge styled

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
# Fixtures: ext
```

## Step-by-Step Guide

### Step 1: Assign sheet_name = 'merge_styled'

```python
sheet_name = 'merge_styled'
```

**Verification:**
```python
assert xcell_b1.font == openpyxl_sty_merged
```

### Step 2: Assign sty_b1 = value

```python
sty_b1 = {'font': {'color': '00FF0000'}}
```

**Verification:**
```python
assert xcell_a2.font == openpyxl_sty_merged
```

### Step 3: Assign sty_a2 = value

```python
sty_a2 = {'font': {'color': '0000FF00'}}
```

### Step 4: Assign initial_cells = value

```python
initial_cells = [ExcelCell(col=1, row=0, val=42, style=sty_b1), ExcelCell(col=0, row=1, val=99, style=sty_a2)]
```

### Step 5: Assign sty_merged = value

```python
sty_merged = {'font': {'color': '000000FF', 'bold': True}}
```

### Step 6: Assign sty_kwargs = _OpenpyxlWriter._convert_to_style_kwargs(...)

```python
sty_kwargs = _OpenpyxlWriter._convert_to_style_kwargs(sty_merged)
```

### Step 7: Assign openpyxl_sty_merged = value

```python
openpyxl_sty_merged = sty_kwargs['font']
```

### Step 8: Assign merge_cells = value

```python
merge_cells = [ExcelCell(col=0, row=0, val='pandas', mergestart=1, mergeend=1, style=sty_merged)]
```

### Step 9: Assign xcell_b1 = value

```python
xcell_b1 = wks['B1']
```

### Step 10: Assign xcell_a2 = value

```python
xcell_a2 = wks['A2']
```

**Verification:**
```python
assert xcell_b1.font == openpyxl_sty_merged
```

### Step 11: Call writer._write_cells()

```python
writer._write_cells(initial_cells, sheet_name=sheet_name)
```

### Step 12: Call writer._write_cells()

```python
writer._write_cells(merge_cells, sheet_name=sheet_name)
```

### Step 13: Assign wks = value

```python
wks = writer.sheets[sheet_name]
```


## Complete Example

```python
# Setup
# Fixtures: ext

# Workflow
from pandas.io.formats.excel import ExcelCell
sheet_name = 'merge_styled'
sty_b1 = {'font': {'color': '00FF0000'}}
sty_a2 = {'font': {'color': '0000FF00'}}
initial_cells = [ExcelCell(col=1, row=0, val=42, style=sty_b1), ExcelCell(col=0, row=1, val=99, style=sty_a2)]
sty_merged = {'font': {'color': '000000FF', 'bold': True}}
sty_kwargs = _OpenpyxlWriter._convert_to_style_kwargs(sty_merged)
openpyxl_sty_merged = sty_kwargs['font']
merge_cells = [ExcelCell(col=0, row=0, val='pandas', mergestart=1, mergeend=1, style=sty_merged)]
with tm.ensure_clean(ext) as path:
    with _OpenpyxlWriter(path) as writer:
        writer._write_cells(initial_cells, sheet_name=sheet_name)
        writer._write_cells(merge_cells, sheet_name=sheet_name)
        wks = writer.sheets[sheet_name]
    xcell_b1 = wks['B1']
    xcell_a2 = wks['A2']
    assert xcell_b1.font == openpyxl_sty_merged
    assert xcell_a2.font == openpyxl_sty_merged
```

## Next Steps


---

*Source: test_openpyxl.py:64 | Complexity: Advanced | Last updated: 2026-06-02*