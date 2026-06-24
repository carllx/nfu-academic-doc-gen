# How To: Zero Rows

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test zero rows

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `contextlib`
- `datetime`
- `io`
- `os`
- `pathlib`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`
- `pandas.io.sas.sas7bdat`
- `py.path`

**Setup Required:**
```python
# Fixtures: datapath, encoding
```

## Step-by-Step Guide

### Step 1: Assign fname = datapath(...)

```python
fname = datapath('io', 'sas', 'data', 'zero_rows.sas7bdat')
```

### Step 2: Assign result = pd.read_sas(...)

```python
result = pd.read_sas(fname, encoding=encoding)
```

### Step 3: Assign str_value = value

```python
str_value = b'a' if encoding is None else 'a'
```

### Step 4: Assign expected = value

```python
expected = pd.DataFrame([{'char_field': str_value, 'num_field': 1.0}]).iloc[:0]
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: datapath, encoding

# Workflow
fname = datapath('io', 'sas', 'data', 'zero_rows.sas7bdat')
result = pd.read_sas(fname, encoding=encoding)
str_value = b'a' if encoding is None else 'a'
expected = pd.DataFrame([{'char_field': str_value, 'num_field': 1.0}]).iloc[:0]
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_sas7bdat.py:252 | Complexity: Intermediate | Last updated: 2026-06-02*