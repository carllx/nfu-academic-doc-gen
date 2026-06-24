# How To: Identical

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test identical

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

### Step 1: Assign i1 = Index(...)

```python
i1 = Index(['a', 'b', 'c'])
```

**Verification:**
```python
assert i1.identical(i2)
```

### Step 2: Assign i2 = Index(...)

```python
i2 = Index(['a', 'b', 'c'])
```

**Verification:**
```python
assert i1.equals(i2)
```

### Step 3: Assign i1 = i1.rename(...)

```python
i1 = i1.rename('foo')
```

**Verification:**
```python
assert not i1.identical(i2)
```

### Step 4: Assign i2 = i2.rename(...)

```python
i2 = i2.rename('foo')
```

**Verification:**
```python
assert i1.identical(i2)
```

### Step 5: Assign i3 = Index(...)

```python
i3 = Index([('a', 'a'), ('a', 'b'), ('b', 'a')])
```

**Verification:**
```python
assert not i3.identical(i4)
```

### Step 6: Assign i4 = Index(...)

```python
i4 = Index([('a', 'a'), ('a', 'b'), ('b', 'a')], tupleize_cols=False)
```

**Verification:**
```python
assert not i3.identical(i4)
```


## Complete Example

```python
# Workflow
i1 = Index(['a', 'b', 'c'])
i2 = Index(['a', 'b', 'c'])
assert i1.identical(i2)
i1 = i1.rename('foo')
assert i1.equals(i2)
assert not i1.identical(i2)
i2 = i2.rename('foo')
assert i1.identical(i2)
i3 = Index([('a', 'a'), ('a', 'b'), ('b', 'a')])
i4 = Index([('a', 'a'), ('a', 'b'), ('b', 'a')], tupleize_cols=False)
assert not i3.identical(i4)
```

## Next Steps


---

*Source: test_base.py:392 | Complexity: Intermediate | Last updated: 2026-06-02*