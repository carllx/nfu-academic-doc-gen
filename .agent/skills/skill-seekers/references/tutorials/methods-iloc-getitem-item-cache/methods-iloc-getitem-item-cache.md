# How To: Methods Iloc Getitem Item Cache

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test methods iloc getitem item cache

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.errors`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: func, args, using_copy_on_write, warn_copy_on_write
```

## Step-by-Step Guide

### Step 1: Assign df_orig = DataFrame(...)

```python
df_orig = DataFrame({'a': [1, 2, 3], 'b': 1})
```

### Step 2: Assign df = df_orig.copy(...)

```python
df = df_orig.copy()
```

### Step 3: Assign ser = value

```python
ser = df.iloc[:, 0]
```

### Step 4: Call getattr()

```python
getattr(ser, func)(*args, inplace=True)
```

### Step 5: Assign df = df_orig.copy(...)

```python
df = df_orig.copy()
```

### Step 6: Assign ser = value

```python
ser = df.copy()['a']
```

### Step 7: Call getattr()

```python
getattr(ser, func)(*args, inplace=True)
```

### Step 8: Assign df = df_orig.copy(...)

```python
df = df_orig.copy()
```

### Step 9: df['a']

```python
df['a']
```

### Step 10: Assign ser = value

```python
ser = df.iloc[:, 0]
```

### Step 11: Call getattr()

```python
getattr(ser, func)(*args, inplace=True)
```

### Step 12: Assign df = df_orig.copy(...)

```python
df = df_orig.copy()
```

### Step 13: df['a']

```python
df['a']
```

### Step 14: Assign ser = value

```python
ser = df['a']
```

### Step 15: Call getattr()

```python
getattr(ser, func)(*args, inplace=True)
```

### Step 16: Assign df = df_orig.copy(...)

```python
df = df_orig.copy()
```

### Step 17: df['a']

```python
df['a']
```

### Step 18: Assign df = df_orig.copy(...)

```python
df = df_orig.copy()
```

### Step 19: Assign ser = value

```python
ser = df['a']
```

### Step 20: Call getattr()

```python
getattr(df['a'], func)(*args, inplace=True)
```

### Step 21: Call getattr()

```python
getattr(df['a'], func)(*args, inplace=True)
```

### Step 22: Call getattr()

```python
getattr(df['a'], func)(*args, inplace=True)
```

### Step 23: Call getattr()

```python
getattr(df['a'], func)(*args, inplace=True)
```


## Complete Example

```python
# Setup
# Fixtures: func, args, using_copy_on_write, warn_copy_on_write

# Workflow
df_orig = DataFrame({'a': [1, 2, 3], 'b': 1})
df = df_orig.copy()
ser = df.iloc[:, 0]
getattr(ser, func)(*args, inplace=True)
df = df_orig.copy()
ser = df.copy()['a']
getattr(ser, func)(*args, inplace=True)
df = df_orig.copy()
df['a']
ser = df.iloc[:, 0]
getattr(ser, func)(*args, inplace=True)
df = df_orig.copy()
df['a']
ser = df['a']
getattr(ser, func)(*args, inplace=True)
df = df_orig.copy()
df['a']
if using_copy_on_write:
    with tm.raises_chained_assignment_error(not PY311):
        getattr(df['a'], func)(*args, inplace=True)
else:
    with tm.assert_cow_warning(not PY311, match='A value'):
        getattr(df['a'], func)(*args, inplace=True)
df = df_orig.copy()
ser = df['a']
if using_copy_on_write:
    with tm.raises_chained_assignment_error(not PY311):
        getattr(df['a'], func)(*args, inplace=True)
else:
    with tm.assert_cow_warning(warn_copy_on_write and (not PY311), match='A value'):
        getattr(df['a'], func)(*args, inplace=True)
```

## Next Steps


---

*Source: test_chained_assignment_deprecation.py:49 | Complexity: Advanced | Last updated: 2026-06-02*