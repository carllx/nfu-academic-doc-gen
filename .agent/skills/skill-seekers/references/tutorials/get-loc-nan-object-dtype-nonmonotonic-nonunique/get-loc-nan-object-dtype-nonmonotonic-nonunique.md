# How To: Get Loc Nan Object Dtype Nonmonotonic Nonunique

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test get loc nan object dtype nonmonotonic nonunique

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx = Index(...)

```python
idx = Index(['foo', np.nan, None, 'foo', 1.0, None], dtype=object)
```

**Verification:**
```python
assert res == 1
```

### Step 2: Assign res = idx.get_loc(...)

```python
res = idx.get_loc(np.nan)
```

**Verification:**
```python
assert res == 1
```

### Step 3: Assign res = idx.get_loc(...)

```python
res = idx.get_loc(None)
```

### Step 4: Assign expected = np.array(...)

```python
expected = np.array([False, False, True, False, False, True])
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(res, expected)
```

### Step 6: Call idx.get_loc()

```python
idx.get_loc(NaT)
```


## Complete Example

```python
# Workflow
idx = Index(['foo', np.nan, None, 'foo', 1.0, None], dtype=object)
res = idx.get_loc(np.nan)
assert res == 1
res = idx.get_loc(None)
expected = np.array([False, False, True, False, False, True])
tm.assert_numpy_array_equal(res, expected)
with pytest.raises(KeyError, match='NaT'):
    idx.get_loc(NaT)
```

## Next Steps


---

*Source: test_indexing.py:81 | Complexity: Intermediate | Last updated: 2026-06-02*