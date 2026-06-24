# How To: Describe Duplicate Columns

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test describe duplicate columns

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame([[0, 1, 2, 3]])
```

### Step 2: Assign df.columns = value

```python
df.columns = [0, 1, 2, 0]
```

### Step 3: Assign gb = df.groupby(...)

```python
gb = df.groupby(df[1])
```

### Step 4: Assign result = gb.describe(...)

```python
result = gb.describe(percentiles=[])
```

### Step 5: Assign columns = value

```python
columns = ['count', 'mean', 'std', 'min', '50%', 'max']
```

### Step 6: Assign frames = value

```python
frames = [DataFrame([[1.0, val, np.nan, val, val, val]], index=[1], columns=columns) for val in (0.0, 2.0, 3.0)]
```

### Step 7: Assign expected = pd.concat(...)

```python
expected = pd.concat(frames, axis=1)
```

### Step 8: Assign expected.columns = MultiIndex(...)

```python
expected.columns = MultiIndex(levels=[[0, 2], columns], codes=[6 * [0] + 6 * [1] + 6 * [0], 3 * list(range(6))])
```

### Step 9: Assign expected.index.names = value

```python
expected.index.names = [1]
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame([[0, 1, 2, 3]])
df.columns = [0, 1, 2, 0]
gb = df.groupby(df[1])
result = gb.describe(percentiles=[])
columns = ['count', 'mean', 'std', 'min', '50%', 'max']
frames = [DataFrame([[1.0, val, np.nan, val, val, val]], index=[1], columns=columns) for val in (0.0, 2.0, 3.0)]
expected = pd.concat(frames, axis=1)
expected.columns = MultiIndex(levels=[[0, 2], columns], codes=[6 * [0] + 6 * [1] + 6 * [0], 3 * list(range(6))])
expected.index.names = [1]
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_describe.py:213 | Complexity: Advanced | Last updated: 2026-06-02*