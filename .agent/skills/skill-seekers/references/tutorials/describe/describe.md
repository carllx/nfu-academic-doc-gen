# How To: Describe

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test describe

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: df, gb, gni
```

## Step-by-Step Guide

### Step 1: Assign expected_index = Index(...)

```python
expected_index = Index([1, 3], name='A')
```

### Step 2: Assign expected_col = MultiIndex(...)

```python
expected_col = MultiIndex(levels=[['B'], ['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max']], codes=[[0] * 8, list(range(8))])
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame([[1.0, 2.0, np.nan, 2.0, 2.0, 2.0, 2.0, 2.0], [0.0, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]], index=expected_index, columns=expected_col)
```

### Step 4: Assign result = gb.describe(...)

```python
result = gb.describe()
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign expected = expected.reset_index(...)

```python
expected = expected.reset_index()
```

### Step 7: Assign result = gni.describe(...)

```python
result = gni.describe()
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: df, gb, gni

# Workflow
expected_index = Index([1, 3], name='A')
expected_col = MultiIndex(levels=[['B'], ['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max']], codes=[[0] * 8, list(range(8))])
expected = DataFrame([[1.0, 2.0, np.nan, 2.0, 2.0, 2.0, 2.0, 2.0], [0.0, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]], index=expected_index, columns=expected_col)
result = gb.describe()
tm.assert_frame_equal(result, expected)
expected = expected.reset_index()
result = gni.describe()
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_describe.py:256 | Complexity: Advanced | Last updated: 2026-06-02*