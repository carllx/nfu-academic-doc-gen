# How To: Categorical Repr Int With Nan

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test categorical repr int with nan

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._config`
- `pandas`


## Step-by-Step Guide

### Step 1: Assign c = Categorical(...)

```python
c = Categorical([1, 2, np.nan])
```

**Verification:**
```python
assert repr(c) == c_exp
```

### Step 2: Assign c_exp = '[1, 2, NaN]\nCategories (2, int64): [1, 2]'

```python
c_exp = '[1, 2, NaN]\nCategories (2, int64): [1, 2]'
```

**Verification:**
```python
assert repr(s) == s_exp
```

### Step 3: Assign s = Series.astype(...)

```python
s = Series([1, 2, np.nan], dtype='object').astype('category')
```

### Step 4: Assign s_exp = '0      1\n1      2\n2    NaN\ndtype: category\nCategories (2, int64): [1, 2]'

```python
s_exp = '0      1\n1      2\n2    NaN\ndtype: category\nCategories (2, int64): [1, 2]'
```

**Verification:**
```python
assert repr(s) == s_exp
```


## Complete Example

```python
# Workflow
c = Categorical([1, 2, np.nan])
c_exp = '[1, 2, NaN]\nCategories (2, int64): [1, 2]'
assert repr(c) == c_exp
s = Series([1, 2, np.nan], dtype='object').astype('category')
s_exp = '0      1\n1      2\n2    NaN\ndtype: category\nCategories (2, int64): [1, 2]'
assert repr(s) == s_exp
```

## Next Steps


---

*Source: test_repr.py:255 | Complexity: Intermediate | Last updated: 2026-06-02*