# How To: Setitem Invalid Indexer Raises

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test setitem invalid indexer raises

## Prerequisites

**Required Modules:**
- `pickle`
- `re`
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays.string_`
- `pandas.core.arrays.string_arrow`


## Step-by-Step Guide

### Step 1: Assign pa = pytest.importorskip(...)

```python
pa = pytest.importorskip('pyarrow')
```

### Step 2: Assign arr = ArrowStringArray(...)

```python
arr = ArrowStringArray(pa.array(list('abcde')))
```

### Step 3: Assign unknown = 'foo'

```python
arr[5] = 'foo'
```

### Step 4: Assign unknown = 'foo'

```python
arr[-6] = 'foo'
```

### Step 5: Assign unknown = 'foo'

```python
arr[[0, 5]] = 'foo'
```

### Step 6: Assign unknown = 'foo'

```python
arr[[0, -6]] = 'foo'
```

### Step 7: Assign unknown = 'foo'

```python
arr[[True, True, False]] = 'foo'
```

### Step 8: Assign unknown = value

```python
arr[[0, 1]] = ['foo', 'bar', 'baz']
```


## Complete Example

```python
# Workflow
pa = pytest.importorskip('pyarrow')
arr = ArrowStringArray(pa.array(list('abcde')))
with pytest.raises(IndexError, match=None):
    arr[5] = 'foo'
with pytest.raises(IndexError, match=None):
    arr[-6] = 'foo'
with pytest.raises(IndexError, match=None):
    arr[[0, 5]] = 'foo'
with pytest.raises(IndexError, match=None):
    arr[[0, -6]] = 'foo'
with pytest.raises(IndexError, match=None):
    arr[[True, True, False]] = 'foo'
with pytest.raises(ValueError, match=None):
    arr[[0, 1]] = ['foo', 'bar', 'baz']
```

## Next Steps


---

*Source: test_string_arrow.py:234 | Complexity: Advanced | Last updated: 2026-06-02*