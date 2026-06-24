# How To: Getitem List Duplicates

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test getitem list duplicates

## Prerequisites

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((4, 4)), columns=list('AABC'))
```

**Verification:**
```python
assert result.columns.name == 'foo'
```

### Step 2: Assign df.columns.name = 'foo'

```python
df.columns.name = 'foo'
```

### Step 3: Assign result = value

```python
result = df[['B', 'C']]
```

**Verification:**
```python
assert result.columns.name == 'foo'
```

### Step 4: Assign expected = value

```python
expected = df.iloc[:, 2:]
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame(np.random.default_rng(2).standard_normal((4, 4)), columns=list('AABC'))
df.columns.name = 'foo'
result = df[['B', 'C']]
assert result.columns.name == 'foo'
expected = df.iloc[:, 2:]
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_getitem.py:91 | Complexity: Intermediate | Last updated: 2026-06-02*