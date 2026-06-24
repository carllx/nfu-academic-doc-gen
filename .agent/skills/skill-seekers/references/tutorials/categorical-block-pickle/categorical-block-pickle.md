# How To: Categorical Block Pickle

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test categorical block pickle

## Prerequisites

**Required Modules:**
- `datetime`
- `itertools`
- `re`
- `numpy`
- `pytest`
- `pandas._libs.internals`
- `pandas.compat`
- `pandas.util._test_decorators`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.algorithms`
- `pandas.core.arrays`
- `pandas.core.internals`
- `pandas.core.internals.blocks`


## Step-by-Step Guide

### Step 1: Assign mgr = create_mgr(...)

```python
mgr = create_mgr('a: category')
```

### Step 2: Assign mgr2 = tm.round_trip_pickle(...)

```python
mgr2 = tm.round_trip_pickle(mgr)
```

### Step 3: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(DataFrame._from_mgr(mgr, axes=mgr.axes), DataFrame._from_mgr(mgr2, axes=mgr2.axes))
```

### Step 4: Assign smgr = create_single_mgr(...)

```python
smgr = create_single_mgr('category')
```

### Step 5: Assign smgr2 = tm.round_trip_pickle(...)

```python
smgr2 = tm.round_trip_pickle(smgr)
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(Series()._constructor_from_mgr(smgr, axes=smgr.axes), Series()._constructor_from_mgr(smgr2, axes=smgr2.axes))
```


## Complete Example

```python
# Workflow
mgr = create_mgr('a: category')
mgr2 = tm.round_trip_pickle(mgr)
tm.assert_frame_equal(DataFrame._from_mgr(mgr, axes=mgr.axes), DataFrame._from_mgr(mgr2, axes=mgr2.axes))
smgr = create_single_mgr('category')
smgr2 = tm.round_trip_pickle(smgr)
tm.assert_series_equal(Series()._constructor_from_mgr(smgr, axes=smgr.axes), Series()._constructor_from_mgr(smgr2, axes=smgr2.axes))
```

## Next Steps


---

*Source: test_internals.py:422 | Complexity: Intermediate | Last updated: 2026-06-02*