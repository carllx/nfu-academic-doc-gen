# How To: Inplace Arithmetic Series Update

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test inplace arithmetic series update

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `collections`
- `datetime`
- `enum`
- `functools`
- `operator`
- `re`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.computation`
- `pandas.tests.frame.common`

**Setup Required:**
```python
# Fixtures: using_copy_on_write, warn_copy_on_write
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'A': [1, 2, 3]})
```

**Verification:**
```python
assert series._values is not vals
```

### Step 2: Assign df_orig = df.copy(...)

```python
df_orig = df.copy()
```

**Verification:**
```python
assert series._values is vals
```

### Step 3: Assign series = value

```python
series = df['A']
```

### Step 4: Assign vals = value

```python
vals = series._values
```

**Verification:**
```python
assert series._values is not vals
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, df_orig)
```

**Verification:**
```python
assert series._values is vals
```

### Step 6: Assign expected = DataFrame(...)

```python
expected = DataFrame({'A': [2, 3, 4]})
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, expected)
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write, warn_copy_on_write

# Workflow
df = DataFrame({'A': [1, 2, 3]})
df_orig = df.copy()
series = df['A']
vals = series._values
with tm.assert_cow_warning(warn_copy_on_write):
    series += 1
if using_copy_on_write:
    assert series._values is not vals
    tm.assert_frame_equal(df, df_orig)
else:
    assert series._values is vals
    expected = DataFrame({'A': [2, 3, 4]})
    tm.assert_frame_equal(df, expected)
```

## Next Steps


---

*Source: test_arithmetic.py:2024 | Complexity: Intermediate | Last updated: 2026-06-02*