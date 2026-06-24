# How To: Concat Same Index Names

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test concat same index names

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `copy`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: name_in1, name_in2, name_in3, name_out
```

## Step-by-Step Guide

### Step 1: Assign indices = value

```python
indices = [Index(['a', 'b', 'c'], name=name_in1), Index(['b', 'c', 'd'], name=name_in2), Index(['c', 'd', 'e'], name=name_in3)]
```

### Step 2: Assign frames = value

```python
frames = [DataFrame({c: [0, 1, 2]}, index=i) for i, c in zip(indices, ['x', 'y', 'z'])]
```

### Step 3: Assign result = concat(...)

```python
result = concat(frames, axis=1)
```

### Step 4: Assign exp_ind = Index(...)

```python
exp_ind = Index(['a', 'b', 'c', 'd', 'e'], name=name_out)
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame({'x': [0, 1, 2, np.nan, np.nan], 'y': [np.nan, 0, 1, 2, np.nan], 'z': [np.nan, np.nan, 0, 1, 2]}, index=exp_ind)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: name_in1, name_in2, name_in3, name_out

# Workflow
indices = [Index(['a', 'b', 'c'], name=name_in1), Index(['b', 'c', 'd'], name=name_in2), Index(['c', 'd', 'e'], name=name_in3)]
frames = [DataFrame({c: [0, 1, 2]}, index=i) for i, c in zip(indices, ['x', 'y', 'z'])]
result = concat(frames, axis=1)
exp_ind = Index(['a', 'b', 'c', 'd', 'e'], name=name_out)
expected = DataFrame({'x': [0, 1, 2, np.nan, np.nan], 'y': [np.nan, 0, 1, 2, np.nan], 'z': [np.nan, np.nan, 0, 1, 2]}, index=exp_ind)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_index.py:57 | Complexity: Intermediate | Last updated: 2026-06-02*