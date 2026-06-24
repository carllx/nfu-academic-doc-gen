# How To: Methods Iloc Getitem Item Cache Fillna

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test methods iloc getitem item cache fillna

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
# Fixtures: using_copy_on_write, warn_copy_on_write
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

### Step 4: Call ser.fillna()

```python
ser.fillna(1, inplace=True)
```

### Step 5: Assign df = df_orig.copy(...)

```python
df = df_orig.copy()
```

### Step 6: Assign ser = value

```python
ser = df.copy()['a']
```

### Step 7: Call ser.fillna()

```python
ser.fillna(1, inplace=True)
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

### Step 11: Call ser.fillna()

```python
ser.fillna(1, inplace=True)
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

### Step 15: Call ser.fillna()

```python
ser.fillna(1, inplace=True)
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

### Step 20: Call unknown.fillna()

```python
df['a'].fillna(1, inplace=True)
```

### Step 21: Call unknown.fillna()

```python
df['a'].fillna(1, inplace=True)
```

### Step 22: Call unknown.fillna()

```python
df['a'].fillna(1, inplace=True)
```

### Step 23: Call unknown.fillna()

```python
df['a'].fillna(1, inplace=True)
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write, warn_copy_on_write

# Workflow
df_orig = DataFrame({'a': [1, 2, 3], 'b': 1})
df = df_orig.copy()
ser = df.iloc[:, 0]
ser.fillna(1, inplace=True)
df = df_orig.copy()
ser = df.copy()['a']
ser.fillna(1, inplace=True)
df = df_orig.copy()
df['a']
ser = df.iloc[:, 0]
ser.fillna(1, inplace=True)
df = df_orig.copy()
df['a']
ser = df['a']
ser.fillna(1, inplace=True)
df = df_orig.copy()
df['a']
if using_copy_on_write:
    with tm.raises_chained_assignment_error():
        df['a'].fillna(1, inplace=True)
else:
    with tm.assert_cow_warning(match='A value'):
        df['a'].fillna(1, inplace=True)
df = df_orig.copy()
ser = df['a']
if using_copy_on_write:
    with tm.raises_chained_assignment_error():
        df['a'].fillna(1, inplace=True)
else:
    with tm.assert_cow_warning(warn_copy_on_write, match='A value'):
        df['a'].fillna(1, inplace=True)
```

## Next Steps


---

*Source: test_chained_assignment_deprecation.py:98 | Complexity: Advanced | Last updated: 2026-06-02*