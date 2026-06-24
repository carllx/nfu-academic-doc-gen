# How To: Loc Nan Multiindex

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test loc nan multiindex

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: using_infer_string
```

## Step-by-Step Guide

### Step 1: Assign tups = value

```python
tups = [('Good Things', 'C', np.nan), ('Good Things', 'R', np.nan), ('Bad Things', 'C', np.nan), ('Bad Things', 'T', np.nan), ('Okay Things', 'N', 'B'), ('Okay Things', 'N', 'D'), ('Okay Things', 'B', np.nan), ('Okay Things', 'D', np.nan)]
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(np.ones((8, 4)), columns=Index(['d1', 'd2', 'd3', 'd4']), index=MultiIndex.from_tuples(tups, names=['u1', 'u2', 'u3']))
```

### Step 3: Assign result = value

```python
result = df.loc['Good Things'].loc['C']
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame(np.ones((1, 4)), index=Index([np.nan], dtype='object' if not using_infer_string else 'str', name='u3'), columns=Index(['d1', 'd2', 'd3', 'd4']))
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: using_infer_string

# Workflow
tups = [('Good Things', 'C', np.nan), ('Good Things', 'R', np.nan), ('Bad Things', 'C', np.nan), ('Bad Things', 'T', np.nan), ('Okay Things', 'N', 'B'), ('Okay Things', 'N', 'D'), ('Okay Things', 'B', np.nan), ('Okay Things', 'D', np.nan)]
df = DataFrame(np.ones((8, 4)), columns=Index(['d1', 'd2', 'd3', 'd4']), index=MultiIndex.from_tuples(tups, names=['u1', 'u2', 'u3']))
result = df.loc['Good Things'].loc['C']
expected = DataFrame(np.ones((1, 4)), index=Index([np.nan], dtype='object' if not using_infer_string else 'str', name='u3'), columns=Index(['d1', 'd2', 'd3', 'd4']))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_loc.py:577 | Complexity: Intermediate | Last updated: 2026-06-02*