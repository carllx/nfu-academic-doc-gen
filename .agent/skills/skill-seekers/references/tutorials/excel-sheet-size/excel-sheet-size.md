# How To: Excel Sheet Size

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test excel sheet size

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
# Fixtures: path
```

## Step-by-Step Guide

### Step 1: Assign breaking_row_count = value

```python
breaking_row_count = 2 ** 20 + 1
```

### Step 2: Assign breaking_col_count = value

```python
breaking_col_count = 2 ** 14 + 1
```

### Step 3: Assign row_arr = np.zeros(...)

```python
row_arr = np.zeros(shape=(breaking_row_count, 1))
```

### Step 4: Assign col_arr = np.zeros(...)

```python
col_arr = np.zeros(shape=(1, breaking_col_count))
```

### Step 5: Assign row_df = DataFrame(...)

```python
row_df = DataFrame(row_arr)
```

### Step 6: Assign col_df = DataFrame(...)

```python
col_df = DataFrame(col_arr)
```

### Step 7: Assign msg = 'sheet is too large'

```python
msg = 'sheet is too large'
```

### Step 8: Call row_df.to_excel()

```python
row_df.to_excel(path)
```

### Step 9: Call col_df.to_excel()

```python
col_df.to_excel(path)
```


## Complete Example

```python
# Setup
# Fixtures: path

# Workflow
breaking_row_count = 2 ** 20 + 1
breaking_col_count = 2 ** 14 + 1
row_arr = np.zeros(shape=(breaking_row_count, 1))
col_arr = np.zeros(shape=(1, breaking_col_count))
row_df = DataFrame(row_arr)
col_df = DataFrame(col_arr)
msg = 'sheet is too large'
with pytest.raises(ValueError, match=msg):
    row_df.to_excel(path)
with pytest.raises(ValueError, match=msg):
    col_df.to_excel(path)
```

## Next Steps


---

*Source: test_writers.py:376 | Complexity: Advanced | Last updated: 2026-06-02*