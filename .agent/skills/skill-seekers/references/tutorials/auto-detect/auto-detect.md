# How To: Auto Detect

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test auto detect

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
assert has_expanded_repr(df)
```

### Step 2: Assign fac = 1.05

```python
fac = 1.05
```

**Verification:**
```python
assert has_horizontally_truncated_repr(df)
```

### Step 3: Assign cols = range(...)

```python
cols = range(int(term_width * fac))
```

**Verification:**
```python
assert has_expanded_repr(df)
```

### Step 4: Assign index = range(...)

```python
index = range(10)
```

**Verification:**
```python
assert has_vertically_truncated_repr(df)
```

### Step 5: Assign df = DataFrame(...)

```python
df = DataFrame(index=index, columns=cols)
```

**Verification:**
```python
assert has_horizontally_truncated_repr(df)
```

### Step 6: Assign index = range(...)

```python
index = range(int(term_height * fac))
```

### Step 7: Assign df = DataFrame(...)

```python
df = DataFrame(index=index, columns=cols)
```

**Verification:**
```python
assert has_expanded_repr(df)
```


## Complete Example

```python
# Workflow
term_width, term_height = get_terminal_size()
fac = 1.05
cols = range(int(term_width * fac))
index = range(10)
df = DataFrame(index=index, columns=cols)
with option_context('mode.sim_interactive', True):
    with option_context('display.max_rows', None):
        with option_context('display.max_columns', None):
            assert has_expanded_repr(df)
    with option_context('display.max_rows', 0):
        with option_context('display.max_columns', 0):
            assert has_horizontally_truncated_repr(df)
    index = range(int(term_height * fac))
    df = DataFrame(index=index, columns=cols)
    with option_context('display.max_rows', 0):
        with option_context('display.max_columns', None):
            assert has_expanded_repr(df)
            assert has_vertically_truncated_repr(df)
    with option_context('display.max_rows', None):
        with option_context('display.max_columns', 0):
            assert has_horizontally_truncated_repr(df)
```

## Next Steps


---

*Source: test_format.py:446 | Complexity: Intermediate | Last updated: 2026-06-02*