# How To: Fillna Array

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test fillna array

## Prerequisites

**Required Modules:**
- `collections`
- `numpy`
- `pytest`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign cat = Categorical(...)

```python
cat = Categorical(['A', 'B', 'C', None, None])
```

**Verification:**
```python
assert isna(cat[-1])
```

### Step 2: Assign other = cat.fillna(...)

```python
other = cat.fillna('C')
```

**Verification:**
```python
assert isna(cat[-1])
```

### Step 3: Assign result = cat.fillna(...)

```python
result = cat.fillna(other)
```

### Step 4: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(result, other)
```

**Verification:**
```python
assert isna(cat[-1])
```

### Step 5: Assign other = np.array(...)

```python
other = np.array(['A', 'B', 'C', 'B', 'A'])
```

### Step 6: Assign result = cat.fillna(...)

```python
result = cat.fillna(other)
```

### Step 7: Assign expected = Categorical(...)

```python
expected = Categorical(['A', 'B', 'C', 'B', 'A'], dtype=cat.dtype)
```

### Step 8: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(result, expected)
```

**Verification:**
```python
assert isna(cat[-1])
```


## Complete Example

```python
# Workflow
cat = Categorical(['A', 'B', 'C', None, None])
other = cat.fillna('C')
result = cat.fillna(other)
tm.assert_categorical_equal(result, other)
assert isna(cat[-1])
other = np.array(['A', 'B', 'C', 'B', 'A'])
result = cat.fillna(other)
expected = Categorical(['A', 'B', 'C', 'B', 'A'], dtype=cat.dtype)
tm.assert_categorical_equal(result, expected)
assert isna(cat[-1])
```

## Next Steps


---

*Source: test_missing.py:114 | Complexity: Advanced | Last updated: 2026-06-02*