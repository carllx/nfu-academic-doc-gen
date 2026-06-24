# How To: Setitem Multiindex2

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test setitem multiindex2

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(np.arange(25).reshape(5, 5), columns='A,B,C,D,E'.split(','), dtype=float)
```

### Step 2: Assign unknown = 99

```python
df['F'] = 99
```

### Step 3: Assign row_selection = value

```python
row_selection = df['A'] % 2 == 0
```

### Step 4: Assign col_selection = value

```python
col_selection = ['B', 'C']
```

### Step 5: Assign unknown = value

```python
df.loc[row_selection, col_selection] = df['F']
```

### Step 6: Assign output = DataFrame(...)

```python
output = DataFrame(99.0, index=[0, 2, 4], columns=['B', 'C'])
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df.loc[row_selection, col_selection], output)
```

### Step 8: Call self.check()

```python
self.check(target=df, indexers=(row_selection, col_selection), value=df['F'], compare_fn=tm.assert_frame_equal, expected=output)
```


## Complete Example

```python
# Workflow
df = DataFrame(np.arange(25).reshape(5, 5), columns='A,B,C,D,E'.split(','), dtype=float)
df['F'] = 99
row_selection = df['A'] % 2 == 0
col_selection = ['B', 'C']
df.loc[row_selection, col_selection] = df['F']
output = DataFrame(99.0, index=[0, 2, 4], columns=['B', 'C'])
tm.assert_frame_equal(df.loc[row_selection, col_selection], output)
self.check(target=df, indexers=(row_selection, col_selection), value=df['F'], compare_fn=tm.assert_frame_equal, expected=output)
```

## Next Steps


---

*Source: test_setitem.py:61 | Complexity: Advanced | Last updated: 2026-06-02*