# How To: To Frame Dtype Fidelity

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to frame dtype fidelity

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat.numpy`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign mi = MultiIndex.from_arrays(...)

```python
mi = MultiIndex.from_arrays([pd.date_range('19910905', periods=6, tz='US/Eastern'), [1, 1, 1, 2, 2, 2], pd.Categorical(['a', 'a', 'b', 'b', 'c', 'c'], ordered=True), ['x', 'x', 'y', 'z', 'x', 'y']], names=['dates', 'a', 'b', 'c'])
```

**Verification:**
```python
assert original_dtypes == df_dtypes
```

### Step 2: Assign original_dtypes = value

```python
original_dtypes = {name: mi.levels[i].dtype for i, name in enumerate(mi.names)}
```

### Step 3: Assign expected_df = DataFrame(...)

```python
expected_df = DataFrame({'dates': pd.date_range('19910905', periods=6, tz='US/Eastern'), 'a': [1, 1, 1, 2, 2, 2], 'b': pd.Categorical(['a', 'a', 'b', 'b', 'c', 'c'], ordered=True), 'c': ['x', 'x', 'y', 'z', 'x', 'y']})
```

### Step 4: Assign df = mi.to_frame(...)

```python
df = mi.to_frame(index=False)
```

### Step 5: Assign df_dtypes = df.dtypes.to_dict(...)

```python
df_dtypes = df.dtypes.to_dict()
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, expected_df)
```

**Verification:**
```python
assert original_dtypes == df_dtypes
```


## Complete Example

```python
# Workflow
mi = MultiIndex.from_arrays([pd.date_range('19910905', periods=6, tz='US/Eastern'), [1, 1, 1, 2, 2, 2], pd.Categorical(['a', 'a', 'b', 'b', 'c', 'c'], ordered=True), ['x', 'x', 'y', 'z', 'x', 'y']], names=['dates', 'a', 'b', 'c'])
original_dtypes = {name: mi.levels[i].dtype for i, name in enumerate(mi.names)}
expected_df = DataFrame({'dates': pd.date_range('19910905', periods=6, tz='US/Eastern'), 'a': [1, 1, 1, 2, 2, 2], 'b': pd.Categorical(['a', 'a', 'b', 'b', 'c', 'c'], ordered=True), 'c': ['x', 'x', 'y', 'z', 'x', 'y']})
df = mi.to_frame(index=False)
df_dtypes = df.dtypes.to_dict()
tm.assert_frame_equal(df, expected_df)
assert original_dtypes == df_dtypes
```

## Next Steps


---

*Source: test_conversion.py:128 | Complexity: Intermediate | Last updated: 2026-06-02*