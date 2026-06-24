# How To: Info Repr

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test info repr

## Prerequisites

**Required Modules:**
- `datetime`
- `io`
- `pathlib`
- `re`
- `shutil`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas`
- `pandas`
- `pandas.io.formats`
- `pandas.io.formats.format`


## Step-by-Step Guide

### Step 1: Assign unknown = get_terminal_size(...)

```python
term_width, term_height = get_terminal_size()
```

**Verification:**
```python
assert has_vertically_truncated_repr(df)
```

### Step 2: Assign max_rows = 60

```python
max_rows = 60
```

**Verification:**
```python
assert has_info_repr(df)
```

### Step 3: Assign max_cols = value

```python
max_cols = 20 + (max(term_width, 80) - 80) // 4
```

**Verification:**
```python
assert has_horizontally_truncated_repr(df)
```

### Step 4: Assign unknown = value

```python
h, w = (max_rows + 1, max_cols - 1)
```

**Verification:**
```python
assert has_info_repr(df)
```

### Step 5: Assign df = DataFrame(...)

```python
df = DataFrame({k: np.arange(1, 1 + h) for k in np.arange(w)})
```

**Verification:**
```python
assert has_vertically_truncated_repr(df)
```

### Step 6: Assign unknown = value

```python
h, w = (max_rows - 1, max_cols + 1)
```

### Step 7: Assign df = DataFrame(...)

```python
df = DataFrame({k: np.arange(1, 1 + h) for k in np.arange(w)})
```

**Verification:**
```python
assert has_horizontally_truncated_repr(df)
```


## Complete Example

```python
# Workflow
term_width, term_height = get_terminal_size()
max_rows = 60
max_cols = 20 + (max(term_width, 80) - 80) // 4
h, w = (max_rows + 1, max_cols - 1)
df = DataFrame({k: np.arange(1, 1 + h) for k in np.arange(w)})
assert has_vertically_truncated_repr(df)
with option_context('display.large_repr', 'info'):
    assert has_info_repr(df)
h, w = (max_rows - 1, max_cols + 1)
df = DataFrame({k: np.arange(1, 1 + h) for k in np.arange(w)})
assert has_horizontally_truncated_repr(df)
with option_context('display.large_repr', 'info', 'display.max_columns', max_cols):
    assert has_info_repr(df)
```

## Next Steps


---

*Source: test_format.py:1207 | Complexity: Intermediate | Last updated: 2026-06-02*