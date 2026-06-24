# How To: Order Matters

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test order matters

## Prerequisites

**Required Modules:**
- `re`
- `weakref`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.tslibs.dtypes`
- `pandas.core.dtypes.base`
- `pandas.core.dtypes.common`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays.sparse`


## Step-by-Step Guide

### Step 1: Assign categories = value

```python
categories = ['a', 'b']
```

**Verification:**
```python
assert c1 is not c2
```

### Step 2: Assign c1 = CategoricalDtype(...)

```python
c1 = CategoricalDtype(categories, ordered=True)
```

**Verification:**
```python
assert c1 is not c3
```

### Step 3: Assign c2 = CategoricalDtype(...)

```python
c2 = CategoricalDtype(categories, ordered=False)
```

### Step 4: Assign c3 = CategoricalDtype(...)

```python
c3 = CategoricalDtype(categories, ordered=None)
```

**Verification:**
```python
assert c1 is not c2
```


## Complete Example

```python
# Workflow
categories = ['a', 'b']
c1 = CategoricalDtype(categories, ordered=True)
c2 = CategoricalDtype(categories, ordered=False)
c3 = CategoricalDtype(categories, ordered=None)
assert c1 is not c2
assert c1 is not c3
```

## Next Steps


---

*Source: test_dtypes.py:896 | Complexity: Intermediate | Last updated: 2026-06-02*