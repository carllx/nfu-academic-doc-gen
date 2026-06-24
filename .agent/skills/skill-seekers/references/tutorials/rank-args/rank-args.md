# How To: Rank Args

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test rank args

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
# Fixtures: grps, vals, ties_method, ascending, pct, exp
```

## Step-by-Step Guide

### Step 1: Assign key = np.repeat(...)

```python
key = np.repeat(grps, len(vals))
```

### Step 2: Assign orig_vals = vals

```python
orig_vals = vals
```

### Step 3: Assign vals = value

```python
vals = list(vals) * len(grps)
```

### Step 4: Assign df = DataFrame(...)

```python
df = DataFrame({'key': key, 'val': vals})
```

### Step 5: Assign result = df.groupby.rank(...)

```python
result = df.groupby('key').rank(method=ties_method, ascending=ascending, pct=pct)
```

### Step 6: Assign exp_df = DataFrame(...)

```python
exp_df = DataFrame(exp * len(grps), columns=['val'])
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, exp_df)
```

### Step 8: Assign vals = np.array(...)

```python
vals = np.array(vals, dtype=orig_vals.dtype)
```


## Complete Example

```python
# Setup
# Fixtures: grps, vals, ties_method, ascending, pct, exp

# Workflow
key = np.repeat(grps, len(vals))
orig_vals = vals
vals = list(vals) * len(grps)
if isinstance(orig_vals, np.ndarray):
    vals = np.array(vals, dtype=orig_vals.dtype)
df = DataFrame({'key': key, 'val': vals})
result = df.groupby('key').rank(method=ties_method, ascending=ascending, pct=pct)
exp_df = DataFrame(exp * len(grps), columns=['val'])
tm.assert_frame_equal(result, exp_df)
```

## Next Steps


---

*Source: test_rank.py:128 | Complexity: Advanced | Last updated: 2026-06-02*