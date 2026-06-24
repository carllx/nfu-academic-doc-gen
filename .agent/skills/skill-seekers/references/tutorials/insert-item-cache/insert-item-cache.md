# How To: Insert Item Cache

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test insert item cache

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: using_array_manager, using_copy_on_write
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((4, 3)))
```

**Verification:**
```python
assert df.iloc[0, 0] == df[0][0]
```

### Step 2: Assign ser = value

```python
ser = df[0]
```

**Verification:**
```python
assert df.iloc[0, 0] != 99
```

### Step 3: Assign expected_warning = None

```python
expected_warning = None
```

**Verification:**
```python
assert df.iloc[0, 0] == df[0][0]
```

### Step 4: Assign expected_warning = PerformanceWarning

```python
expected_warning = PerformanceWarning
```

**Verification:**
```python
assert df.iloc[0, 0] == 99
```

### Step 5: Assign unknown = 99

```python
ser.iloc[0] = 99
```

**Verification:**
```python
assert df.iloc[0, 0] == df[0][0]
```

### Step 6: Assign unknown = 99

```python
ser.values[0] = 99
```

**Verification:**
```python
assert df.iloc[0, 0] == df[0][0]
```

### Step 7: Assign unknown = value

```python
df[n + 3] = df[1] * n
```


## Complete Example

```python
# Setup
# Fixtures: using_array_manager, using_copy_on_write

# Workflow
df = DataFrame(np.random.default_rng(2).standard_normal((4, 3)))
ser = df[0]
if using_array_manager:
    expected_warning = None
else:
    expected_warning = PerformanceWarning
with tm.assert_produces_warning(expected_warning):
    for n in range(100):
        df[n + 3] = df[1] * n
if using_copy_on_write:
    ser.iloc[0] = 99
    assert df.iloc[0, 0] == df[0][0]
    assert df.iloc[0, 0] != 99
else:
    ser.values[0] = 99
    assert df.iloc[0, 0] == df[0][0]
    assert df.iloc[0, 0] == 99
```

## Next Steps


---

*Source: test_insert.py:74 | Complexity: Intermediate | Last updated: 2026-06-02*