# How To: Corr Item Cache

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test corr item cache

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: using_copy_on_write, warn_copy_on_write
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'A': range(10)})
```

**Verification:**
```python
assert len(df._mgr.arrays) == 2
```

### Step 2: Assign unknown = value

```python
df['B'] = range(10)[::-1]
```

**Verification:**
```python
assert df.loc[0, 'A'] == 0
```

### Step 3: Assign ser = value

```python
ser = df['A']
```

**Verification:**
```python
assert df.loc[0, 'A'] == 99
```

### Step 4: Assign _ = df.corr(...)

```python
_ = df.corr(numeric_only=True)
```

**Verification:**
```python
assert df['A'] is ser
```

### Step 5: Assign unknown = 99

```python
ser.iloc[0] = 99
```

**Verification:**
```python
assert df.values[0, 0] == 99
```

### Step 6: Assign unknown = 99

```python
ser.values[0] = 99
```

**Verification:**
```python
assert df.loc[0, 'A'] == 99
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write, warn_copy_on_write

# Workflow
df = DataFrame({'A': range(10)})
df['B'] = range(10)[::-1]
ser = df['A']
assert len(df._mgr.arrays) == 2
_ = df.corr(numeric_only=True)
if using_copy_on_write:
    ser.iloc[0] = 99
    assert df.loc[0, 'A'] == 0
else:
    ser.values[0] = 99
    assert df.loc[0, 'A'] == 99
    if not warn_copy_on_write:
        assert df['A'] is ser
    assert df.values[0, 0] == 99
```

## Next Steps


---

*Source: test_cov_corr.py:210 | Complexity: Intermediate | Last updated: 2026-06-02*