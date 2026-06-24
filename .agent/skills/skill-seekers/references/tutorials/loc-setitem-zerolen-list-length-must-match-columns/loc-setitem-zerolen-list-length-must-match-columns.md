# How To: Loc Setitem Zerolen List Length Must Match Columns

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test loc setitem zerolen list length must match columns

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
df = DataFrame(columns=['A', 'B'])
```

### Step 2: Assign msg = 'cannot set a row with mismatched columns'

```python
msg = 'cannot set a row with mismatched columns'
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame(columns=['A', 'B'])
```

### Step 4: Assign unknown = value

```python
df.loc[3] = [6, 7]
```

### Step 5: Assign exp = DataFrame(...)

```python
exp = DataFrame([[6, 7]], index=[3], columns=['A', 'B'], dtype=np.int64)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, exp)
```

### Step 7: Assign unknown = value

```python
df.loc[0] = [1, 2, 3]
```


## Complete Example

```python
# Workflow
df = DataFrame(columns=['A', 'B'])
msg = 'cannot set a row with mismatched columns'
with pytest.raises(ValueError, match=msg):
    df.loc[0] = [1, 2, 3]
df = DataFrame(columns=['A', 'B'])
df.loc[3] = [6, 7]
exp = DataFrame([[6, 7]], index=[3], columns=['A', 'B'], dtype=np.int64)
tm.assert_frame_equal(df, exp)
```

## Next Steps


---

*Source: test_partial.py:64 | Complexity: Intermediate | Last updated: 2026-06-02*