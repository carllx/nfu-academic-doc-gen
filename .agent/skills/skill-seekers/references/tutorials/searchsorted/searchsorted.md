# How To: Searchsorted

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test searchsorted

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `sys`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas.compat`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: request, index_or_series_obj
```

## Step-by-Step Guide

### Step 1: Assign obj = index_or_series_obj

```python
obj = index_or_series_obj
```

**Verification:**
```python
assert 0 <= index <= len(obj)
```

### Step 2: Assign max_obj = max(...)

```python
max_obj = max(obj, default=0)
```

**Verification:**
```python
assert 0 <= index <= len(obj)
```

### Step 3: Assign index = np.searchsorted(...)

```python
index = np.searchsorted(obj, max_obj)
```

**Verification:**
```python
assert 0 <= index <= len(obj)
```

### Step 4: Assign index = np.searchsorted(...)

```python
index = np.searchsorted(obj, max_obj, sorter=range(len(obj)))
```

**Verification:**
```python
assert 0 <= index <= len(obj)
```

### Step 5: Call request.applymarker()

```python
request.applymarker(pytest.mark.xfail(reason="np.searchsorted doesn't work on pd.MultiIndex: GH 14833"))
```

### Step 6: Assign mark = pytest.mark.xfail(...)

```python
mark = pytest.mark.xfail(reason='complex objects are not comparable')
```

### Step 7: Call request.applymarker()

```python
request.applymarker(mark)
```


## Complete Example

```python
# Setup
# Fixtures: request, index_or_series_obj

# Workflow
obj = index_or_series_obj
if isinstance(obj, pd.MultiIndex):
    request.applymarker(pytest.mark.xfail(reason="np.searchsorted doesn't work on pd.MultiIndex: GH 14833"))
elif obj.dtype.kind == 'c' and isinstance(obj, Index):
    mark = pytest.mark.xfail(reason='complex objects are not comparable')
    request.applymarker(mark)
max_obj = max(obj, default=0)
index = np.searchsorted(obj, max_obj)
assert 0 <= index <= len(obj)
index = np.searchsorted(obj, max_obj, sorter=range(len(obj)))
assert 0 <= index <= len(obj)
```

## Next Steps


---

*Source: test_misc.py:142 | Complexity: Intermediate | Last updated: 2026-06-02*