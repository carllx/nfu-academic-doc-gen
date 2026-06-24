# How To: Pivot Df Multiindex Index None

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test pivot df multiindex index none

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame([['A', 'A1', 'label1', 1], ['A', 'A2', 'label2', 2], ['B', 'A1', 'label1', 3], ['B', 'A2', 'label2', 4]], columns=['index_1', 'index_2', 'label', 'value'])
```

### Step 2: Assign df = df.set_index(...)

```python
df = df.set_index(['index_1', 'index_2'])
```

### Step 3: Assign result = df.pivot(...)

```python
result = df.pivot(columns='label', values='value')
```

### Step 4: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame([[1.0, np.nan], [np.nan, 2.0], [3.0, np.nan], [np.nan, 4.0]], index=df.index, columns=Index(['label1', 'label2'], name='label'))
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = pd.DataFrame([['A', 'A1', 'label1', 1], ['A', 'A2', 'label2', 2], ['B', 'A1', 'label1', 3], ['B', 'A2', 'label2', 4]], columns=['index_1', 'index_2', 'label', 'value'])
df = df.set_index(['index_1', 'index_2'])
result = df.pivot(columns='label', values='value')
expected = pd.DataFrame([[1.0, np.nan], [np.nan, 2.0], [3.0, np.nan], [np.nan, 4.0]], index=df.index, columns=Index(['label1', 'label2'], name='label'))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_pivot_multilevel.py:235 | Complexity: Intermediate | Last updated: 2026-06-02*