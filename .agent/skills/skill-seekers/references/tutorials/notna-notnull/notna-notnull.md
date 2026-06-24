# How To: Notna Notnull

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test notna notnull

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `contextlib`
- `datetime`
- `decimal`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas._libs`
- `pandas._libs.tslibs`
- `pandas.compat.numpy`
- `pandas.core.dtypes.common`
- `pandas.core.dtypes.dtypes`
- `pandas.core.dtypes.missing`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: notna_f
```

## Step-by-Step Guide

### Step 1: Assign msg = 'use_inf_as_na option is deprecated'

```python
msg = 'use_inf_as_na option is deprecated'
```

**Verification:**
```python
assert notna_f(1.0)
```

### Step 2: Assign arr = np.array(...)

```python
arr = np.array([1.5, np.inf, 3.5, -np.inf])
```

**Verification:**
```python
assert not notna_f(None)
```

### Step 3: Assign result = notna_f(...)

```python
result = notna_f(arr)
```

**Verification:**
```python
assert not notna_f(np.nan)
```

### Step 4: Assign arr = np.array(...)

```python
arr = np.array([1.5, np.inf, 3.5, -np.inf])
```

**Verification:**
```python
assert notna_f(np.inf)
```

### Step 5: Assign result = notna_f(...)

```python
result = notna_f(arr)
```

**Verification:**
```python
assert notna_f(-np.inf)
```


## Complete Example

```python
# Setup
# Fixtures: notna_f

# Workflow
assert notna_f(1.0)
assert not notna_f(None)
assert not notna_f(np.nan)
msg = 'use_inf_as_na option is deprecated'
with tm.assert_produces_warning(FutureWarning, match=msg):
    with cf.option_context('mode.use_inf_as_na', False):
        assert notna_f(np.inf)
        assert notna_f(-np.inf)
        arr = np.array([1.5, np.inf, 3.5, -np.inf])
        result = notna_f(arr)
        assert result.all()
with tm.assert_produces_warning(FutureWarning, match=msg):
    with cf.option_context('mode.use_inf_as_na', True):
        assert not notna_f(np.inf)
        assert not notna_f(-np.inf)
        arr = np.array([1.5, np.inf, 3.5, -np.inf])
        result = notna_f(arr)
        assert result.sum() == 2
```

## Next Steps


---

*Source: test_missing.py:52 | Complexity: Intermediate | Last updated: 2026-06-02*