# How To: Copy Name

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test copy name

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `copy`
- `re`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.compat.numpy`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: index_flat
```

## Step-by-Step Guide

### Step 1: Assign index = index_flat

```python
index = index_flat
```

**Verification:**
```python
assert first is not second
```

### Step 2: Assign first = type(...)

```python
first = type(index)(index, copy=True, name='mario')
```

**Verification:**
```python
assert index.equals(first)
```

### Step 3: Assign second = type(...)

```python
second = type(first)(first, copy=False)
```

**Verification:**
```python
assert first.name == 'mario'
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(first, second)
```

**Verification:**
```python
assert second.name == 'mario'
```

### Step 5: Assign s1 = pd.Series(...)

```python
s1 = pd.Series(2, index=first)
```

**Verification:**
```python
assert s3.index.name == 'mario'
```

### Step 6: Assign s2 = pd.Series(...)

```python
s2 = pd.Series(3, index=second[:-1])
```

### Step 7: Assign s3 = value

```python
s3 = s1 * s2
```

**Verification:**
```python
assert s3.index.name == 'mario'
```


## Complete Example

```python
# Setup
# Fixtures: index_flat

# Workflow
index = index_flat
first = type(index)(index, copy=True, name='mario')
second = type(first)(first, copy=False)
assert first is not second
tm.assert_index_equal(first, second)
assert index.equals(first)
assert first.name == 'mario'
assert second.name == 'mario'
s1 = pd.Series(2, index=first)
s2 = pd.Series(3, index=second[:-1])
s3 = s1 * s2
assert s3.index.name == 'mario'
```

## Next Steps


---

*Source: test_common.py:151 | Complexity: Intermediate | Last updated: 2026-06-02*