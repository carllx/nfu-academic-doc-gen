# How To: Add 2D

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test add 2d

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `operator`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas.compat`
- `pandas.compat.pyarrow`
- `pandas.util._test_decorators`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays.string_`
- `pandas.core.arrays.string_arrow`
- `pyarrow`
- `pyarrow.compute`
- `pyarrow`

**Setup Required:**
```python
# Fixtures: dtype, request
```

## Step-by-Step Guide

### Step 1: Assign a = pd.array(...)

```python
a = pd.array(['a', 'b', 'c'], dtype=dtype)
```

### Step 2: Assign b = np.array(...)

```python
b = np.array([['a', 'b', 'c']], dtype=object)
```

### Step 3: Assign s = pd.Series(...)

```python
s = pd.Series(a)
```

### Step 4: Assign reason = "Failed: DID NOT RAISE <class 'ValueError'>"

```python
reason = "Failed: DID NOT RAISE <class 'ValueError'>"
```

### Step 5: Assign mark = pytest.mark.xfail(...)

```python
mark = pytest.mark.xfail(raises=None, reason=reason)
```

### Step 6: Call request.applymarker()

```python
request.applymarker(mark)
```

### Step 7: a + b

```python
a + b
```

### Step 8: s + b

```python
s + b
```


## Complete Example

```python
# Setup
# Fixtures: dtype, request

# Workflow
if dtype.storage == 'pyarrow':
    reason = "Failed: DID NOT RAISE <class 'ValueError'>"
    mark = pytest.mark.xfail(raises=None, reason=reason)
    request.applymarker(mark)
a = pd.array(['a', 'b', 'c'], dtype=dtype)
b = np.array([['a', 'b', 'c']], dtype=object)
with pytest.raises(ValueError, match='3 != 1'):
    a + b
s = pd.Series(a)
with pytest.raises(ValueError, match='3 != 1'):
    s + b
```

## Next Steps


---

*Source: test_string.py:217 | Complexity: Advanced | Last updated: 2026-06-02*