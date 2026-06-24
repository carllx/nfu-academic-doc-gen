# How To: Infs N Nans

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test infs n nans

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
# Fixtures: grps, vals, ties_method, ascending, na_option, exp
```

## Step-by-Step Guide

### Step 1: Assign key = np.repeat(...)

```python
key = np.repeat(grps, len(vals))
```

### Step 2: Assign vals = value

```python
vals = vals * len(grps)
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame({'key': key, 'val': vals})
```

### Step 4: Assign result = df.groupby.rank(...)

```python
result = df.groupby('key').rank(method=ties_method, ascending=ascending, na_option=na_option)
```

### Step 5: Assign exp_df = DataFrame(...)

```python
exp_df = DataFrame(exp * len(grps), columns=['val'])
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, exp_df)
```


## Complete Example

```python
# Setup
# Fixtures: grps, vals, ties_method, ascending, na_option, exp

# Workflow
key = np.repeat(grps, len(vals))
vals = vals * len(grps)
df = DataFrame({'key': key, 'val': vals})
result = df.groupby('key').rank(method=ties_method, ascending=ascending, na_option=na_option)
exp_df = DataFrame(exp * len(grps), columns=['val'])
tm.assert_frame_equal(result, exp_df)
```

## Next Steps


---

*Source: test_rank.py:182 | Complexity: Intermediate | Last updated: 2026-06-02*