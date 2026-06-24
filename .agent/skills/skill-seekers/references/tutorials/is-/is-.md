# How To: Is 

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test is 

## Prerequisites

**Required Modules:**
- `collections`
- `datetime`
- `functools`
- `math`
- `operator`
- `re`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.indexes.api`
- `pyarrow`
- `IPython.core.completer`


## Step-by-Step Guide

### Step 1: Assign ind = Index(...)

```python
ind = Index(range(10))
```

**Verification:**
```python
assert ind.is_(ind)
```

### Step 2: Assign ind2 = ind.view(...)

```python
ind2 = ind.view()
```

**Verification:**
```python
assert ind.is_(ind.view().view().view().view())
```

### Step 3: Assign ind2.name = 'bob'

```python
ind2.name = 'bob'
```

**Verification:**
```python
assert not ind.is_(Index(range(10)))
```

### Step 4: Assign arr = np.array(...)

```python
arr = np.array(range(1, 11))
```

**Verification:**
```python
assert not ind.is_(ind.copy())
```

### Step 5: Assign ind1 = Index(...)

```python
ind1 = Index(arr, copy=False)
```

**Verification:**
```python
assert not ind.is_(ind.copy(deep=False))
```

### Step 6: Assign ind2 = Index(...)

```python
ind2 = Index(arr, copy=False)
```

**Verification:**
```python
assert not ind.is_(ind[:])
```


## Complete Example

```python
# Workflow
ind = Index(range(10))
assert ind.is_(ind)
assert ind.is_(ind.view().view().view().view())
assert not ind.is_(Index(range(10)))
assert not ind.is_(ind.copy())
assert not ind.is_(ind.copy(deep=False))
assert not ind.is_(ind[:])
assert not ind.is_(np.array(range(10)))
assert ind.is_(ind.view())
ind2 = ind.view()
ind2.name = 'bob'
assert ind.is_(ind2)
assert ind2.is_(ind)
assert not ind.is_(Index(ind.values))
arr = np.array(range(1, 11))
ind1 = Index(arr, copy=False)
ind2 = Index(arr, copy=False)
assert not ind1.is_(ind2)
```

## Next Steps


---

*Source: test_base.py:410 | Complexity: Intermediate | Last updated: 2026-06-02*