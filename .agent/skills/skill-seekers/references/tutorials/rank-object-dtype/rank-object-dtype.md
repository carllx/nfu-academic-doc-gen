# How To: Rank Object Dtype

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test rank object dtype

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: ties_method, ascending, na_option, pct, vals
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'key': ['foo'] * 5, 'val': vals})
```

### Step 2: Assign mask = unknown.isna(...)

```python
mask = df['val'].isna()
```

### Step 3: Assign gb = df.groupby(...)

```python
gb = df.groupby('key')
```

### Step 4: Assign res = gb.rank(...)

```python
res = gb.rank(method=ties_method, ascending=ascending, na_option=na_option, pct=pct)
```

### Step 5: Assign gb2 = df2.groupby(...)

```python
gb2 = df2.groupby('key')
```

### Step 6: Assign alt = gb2.rank(...)

```python
alt = gb2.rank(method=ties_method, ascending=ascending, na_option=na_option, pct=pct)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res, alt)
```

### Step 8: Assign df2 = DataFrame(...)

```python
df2 = DataFrame({'key': ['foo'] * 5, 'val': [0, np.nan, 2, np.nan, 1]})
```

### Step 9: Assign df2 = DataFrame(...)

```python
df2 = DataFrame({'key': ['foo'] * 5, 'val': [0, 0, 2, 0, 1]})
```


## Complete Example

```python
# Setup
# Fixtures: ties_method, ascending, na_option, pct, vals

# Workflow
df = DataFrame({'key': ['foo'] * 5, 'val': vals})
mask = df['val'].isna()
gb = df.groupby('key')
res = gb.rank(method=ties_method, ascending=ascending, na_option=na_option, pct=pct)
if mask.any():
    df2 = DataFrame({'key': ['foo'] * 5, 'val': [0, np.nan, 2, np.nan, 1]})
else:
    df2 = DataFrame({'key': ['foo'] * 5, 'val': [0, 0, 2, 0, 1]})
gb2 = df2.groupby('key')
alt = gb2.rank(method=ties_method, ascending=ascending, na_option=na_option, pct=pct)
tm.assert_frame_equal(res, alt)
```

## Next Steps


---

*Source: test_rank.py:490 | Complexity: Advanced | Last updated: 2026-06-02*