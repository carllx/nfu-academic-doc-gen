# How To: Unstack Non Slice Like Blocks

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test unstack non slice like blocks

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `itertools`
- `re`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.reshape`

**Setup Required:**
```python
# Fixtures: using_array_manager
```

## Step-by-Step Guide

### Step 1: Assign mi = MultiIndex.from_product(...)

```python
mi = MultiIndex.from_product([range(5), ['A', 'B', 'C']])
```

**Verification:**
```python
assert any((not x.mgr_locs.is_slice_like for x in df._mgr.blocks))
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({0: np.random.default_rng(2).standard_normal(15), 1: np.random.default_rng(2).standard_normal(15).astype(np.int64), 2: np.random.default_rng(2).standard_normal(15), 3: np.random.default_rng(2).standard_normal(15)}, index=mi)
```

### Step 3: Assign res = df.unstack(...)

```python
res = df.unstack()
```

### Step 4: Assign expected = pd.concat(...)

```python
expected = pd.concat([df[n].unstack() for n in range(4)], keys=range(4), axis=1)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res, expected)
```

**Verification:**
```python
assert any((not x.mgr_locs.is_slice_like for x in df._mgr.blocks))
```


## Complete Example

```python
# Setup
# Fixtures: using_array_manager

# Workflow
mi = MultiIndex.from_product([range(5), ['A', 'B', 'C']])
df = DataFrame({0: np.random.default_rng(2).standard_normal(15), 1: np.random.default_rng(2).standard_normal(15).astype(np.int64), 2: np.random.default_rng(2).standard_normal(15), 3: np.random.default_rng(2).standard_normal(15)}, index=mi)
if not using_array_manager:
    assert any((not x.mgr_locs.is_slice_like for x in df._mgr.blocks))
res = df.unstack()
expected = pd.concat([df[n].unstack() for n in range(4)], keys=range(4), axis=1)
tm.assert_frame_equal(res, expected)
```

## Next Steps


---

*Source: test_stack_unstack.py:1505 | Complexity: Intermediate | Last updated: 2026-06-02*