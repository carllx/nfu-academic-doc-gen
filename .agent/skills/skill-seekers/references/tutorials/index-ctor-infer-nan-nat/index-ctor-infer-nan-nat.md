# How To: Index Ctor Infer Nan Nat

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test index ctor infer nan nat

## Prerequisites

- [ ] Setup code must be executed first

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

**Setup Required:**
```python
# Fixtures: klass, dtype, na_val
```

## Step-by-Step Guide

### Step 1: Assign na_list = value

```python
na_list = [na_val, na_val]
```

**Verification:**
```python
assert expected.dtype == dtype
```

### Step 2: Assign expected = klass(...)

```python
expected = klass(na_list)
```

**Verification:**
```python
assert expected.dtype == dtype
```

### Step 3: Assign result = Index(...)

```python
result = Index(na_list)
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 5: Assign result = Index(...)

```python
result = Index(np.array(na_list))
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: klass, dtype, na_val

# Workflow
na_list = [na_val, na_val]
expected = klass(na_list)
assert expected.dtype == dtype
result = Index(na_list)
tm.assert_index_equal(result, expected)
result = Index(np.array(na_list))
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_base.py:192 | Complexity: Intermediate | Last updated: 2026-06-02*