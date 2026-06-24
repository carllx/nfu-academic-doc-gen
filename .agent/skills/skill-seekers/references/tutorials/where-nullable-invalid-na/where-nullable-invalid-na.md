# How To: Where Nullable Invalid Na

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test where nullable invalid na

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `hypothesis`
- `numpy`
- `pytest`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas._testing._hypothesis`

**Setup Required:**
```python
# Fixtures: frame_or_series, any_numeric_ea_dtype
```

## Step-by-Step Guide

### Step 1: Assign arr = pd.array(...)

```python
arr = pd.array([1, 2, 3], dtype=any_numeric_ea_dtype)
```

### Step 2: Assign obj = frame_or_series(...)

```python
obj = frame_or_series(arr)
```

### Step 3: Assign mask = value

```python
mask = np.array([True, True, False], ndmin=obj.ndim).T
```

### Step 4: Assign msg = "Invalid value '.*' for dtype '(U?Int|Float)\\d{1,2}'"

```python
msg = "Invalid value '.*' for dtype '(U?Int|Float)\\d{1,2}'"
```

### Step 5: Call obj.where()

```python
obj.where(mask, null)
```

### Step 6: Call obj.mask()

```python
obj.mask(mask, null)
```


## Complete Example

```python
# Setup
# Fixtures: frame_or_series, any_numeric_ea_dtype

# Workflow
arr = pd.array([1, 2, 3], dtype=any_numeric_ea_dtype)
obj = frame_or_series(arr)
mask = np.array([True, True, False], ndmin=obj.ndim).T
msg = "Invalid value '.*' for dtype '(U?Int|Float)\\d{1,2}'"
for null in tm.NP_NAT_OBJECTS + [pd.NaT]:
    with pytest.raises(TypeError, match=msg):
        obj.where(mask, null)
    with pytest.raises(TypeError, match=msg):
        obj.mask(mask, null)
```

## Next Steps


---

*Source: test_where.py:972 | Complexity: Intermediate | Last updated: 2026-06-02*