# How To: Nunique Null

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test nunique null

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.tests.base.common`

**Setup Required:**
```python
# Fixtures: null_obj, index_or_series_obj
```

## Step-by-Step Guide

### Step 1: Assign obj = index_or_series_obj

```python
obj = index_or_series_obj
```

**Verification:**
```python
assert obj.nunique() == len(obj.categories)
```

### Step 2: Assign values = value

```python
values = obj._values
```

**Verification:**
```python
assert obj.nunique(dropna=False) == len(obj.categories) + 1
```

### Step 3: Assign unknown = null_obj

```python
values[0:2] = null_obj
```

**Verification:**
```python
assert obj.nunique() == max(0, num_unique_values - 1)
```

### Step 4: Assign klass = type(...)

```python
klass = type(obj)
```

**Verification:**
```python
assert obj.nunique(dropna=False) == max(0, num_unique_values)
```

### Step 5: Assign repeated_values = np.repeat(...)

```python
repeated_values = np.repeat(values, range(1, len(values) + 1))
```

### Step 6: Assign obj = klass(...)

```python
obj = klass(repeated_values, dtype=obj.dtype)
```

### Step 7: Call pytest.skip()

```python
pytest.skip("type doesn't allow for NA operations")
```

**Verification:**
```python
assert obj.nunique() == len(obj.categories)
```

### Step 8: Assign num_unique_values = len(...)

```python
num_unique_values = len(obj.unique())
```

**Verification:**
```python
assert obj.nunique() == max(0, num_unique_values - 1)
```

### Step 9: Call pytest.skip()

```python
pytest.skip(f"MultiIndex can't hold '{null_obj}'")
```


## Complete Example

```python
# Setup
# Fixtures: null_obj, index_or_series_obj

# Workflow
obj = index_or_series_obj
if not allow_na_ops(obj):
    pytest.skip("type doesn't allow for NA operations")
elif isinstance(obj, pd.MultiIndex):
    pytest.skip(f"MultiIndex can't hold '{null_obj}'")
values = obj._values
values[0:2] = null_obj
klass = type(obj)
repeated_values = np.repeat(values, range(1, len(values) + 1))
obj = klass(repeated_values, dtype=obj.dtype)
if isinstance(obj, pd.CategoricalIndex):
    assert obj.nunique() == len(obj.categories)
    assert obj.nunique(dropna=False) == len(obj.categories) + 1
else:
    num_unique_values = len(obj.unique())
    assert obj.nunique() == max(0, num_unique_values - 1)
    assert obj.nunique(dropna=False) == max(0, num_unique_values)
```

## Next Steps


---

*Source: test_unique.py:76 | Complexity: Advanced | Last updated: 2026-06-02*