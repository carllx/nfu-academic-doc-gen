# How To: Fillna Dict Inplace Nonunique Columns

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test fillna dict inplace nonunique columns

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`
- `pandas.tests.frame.common`

**Setup Required:**
```python
# Fixtures: using_copy_on_write, warn_copy_on_write
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'A': [np.nan] * 3, 'B': [NaT, Timestamp(1), NaT], 'C': [np.nan, 'foo', 2]})
```

**Verification:**
```python
assert tm.shares_memory(df.iloc[:, 0], orig.iloc[:, 0])
```

### Step 2: Assign df.columns = value

```python
df.columns = ['A', 'A', 'A']
```

**Verification:**
```python
assert not tm.shares_memory(df.iloc[:, 1], orig.iloc[:, 1])
```

### Step 3: Assign orig = value

```python
orig = df[:]
```

**Verification:**
```python
assert tm.shares_memory(df.iloc[:, 2], orig.iloc[:, 2])
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'A': [2.0] * 3, 'B': [2, Timestamp(1), 2], 'C': [2, 'foo', 2]})
```

### Step 5: Assign expected.columns = value

```python
expected.columns = ['A', 'A', 'A']
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, expected)
```

**Verification:**
```python
assert not tm.shares_memory(df.iloc[:, 1], orig.iloc[:, 1])
```

### Step 7: Call df.fillna()

```python
df.fillna({'A': 2}, inplace=True)
```

**Verification:**
```python
assert tm.shares_memory(df.iloc[:, 0], orig.iloc[:, 0])
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write, warn_copy_on_write

# Workflow
df = DataFrame({'A': [np.nan] * 3, 'B': [NaT, Timestamp(1), NaT], 'C': [np.nan, 'foo', 2]})
df.columns = ['A', 'A', 'A']
orig = df[:]
with tm.assert_cow_warning(warn_copy_on_write):
    df.fillna({'A': 2}, inplace=True)
expected = DataFrame({'A': [2.0] * 3, 'B': [2, Timestamp(1), 2], 'C': [2, 'foo', 2]})
expected.columns = ['A', 'A', 'A']
tm.assert_frame_equal(df, expected)
if not using_copy_on_write:
    assert tm.shares_memory(df.iloc[:, 0], orig.iloc[:, 0])
assert not tm.shares_memory(df.iloc[:, 1], orig.iloc[:, 1])
if not using_copy_on_write:
    assert tm.shares_memory(df.iloc[:, 2], orig.iloc[:, 2])
```

## Next Steps


---

*Source: test_fillna.py:24 | Complexity: Intermediate | Last updated: 2026-06-02*