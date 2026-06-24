# How To: Append Overlay Startrow Startcol

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test append overlay startrow startcol

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
# Fixtures: ext, startrow, startcol, greeting, goodbye
```

## Step-by-Step Guide

### Step 1: Assign df1 = DataFrame(...)

```python
df1 = DataFrame({'greeting': ['hello', 'world'], 'goodbye': ['goodbye', 'people']})
```

### Step 2: Assign df2 = DataFrame(...)

```python
df2 = DataFrame(['poop'])
```

### Step 3: Call df1.to_excel()

```python
df1.to_excel(f, engine='openpyxl', sheet_name='poo', index=False)
```

### Step 4: Assign result = pd.read_excel(...)

```python
result = pd.read_excel(f, sheet_name='poo', engine='openpyxl')
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame({'greeting': greeting, 'goodbye': goodbye})
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Call df2.to_excel()

```python
df2.to_excel(writer, index=False, header=False, startrow=startrow + 1, startcol=startcol, sheet_name='poo')
```


## Complete Example

```python
# Setup
# Fixtures: ext, startrow, startcol, greeting, goodbye

# Workflow
df1 = DataFrame({'greeting': ['hello', 'world'], 'goodbye': ['goodbye', 'people']})
df2 = DataFrame(['poop'])
with tm.ensure_clean(ext) as f:
    df1.to_excel(f, engine='openpyxl', sheet_name='poo', index=False)
    with ExcelWriter(f, engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
        df2.to_excel(writer, index=False, header=False, startrow=startrow + 1, startcol=startcol, sheet_name='poo')
    result = pd.read_excel(f, sheet_name='poo', engine='openpyxl')
    expected = DataFrame({'greeting': greeting, 'goodbye': goodbye})
    tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_openpyxl.py:231 | Complexity: Intermediate | Last updated: 2026-06-02*