# How To: Clip Against Frame

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test clip against frame

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: axis
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((1000, 2)))
```

### Step 2: Assign lb = DataFrame(...)

```python
lb = DataFrame(np.random.default_rng(2).standard_normal((1000, 2)))
```

### Step 3: Assign ub = value

```python
ub = lb + 1
```

### Step 4: Assign clipped_df = df.clip(...)

```python
clipped_df = df.clip(lb, ub, axis=axis)
```

### Step 5: Assign lb_mask = value

```python
lb_mask = df <= lb
```

### Step 6: Assign ub_mask = value

```python
ub_mask = df >= ub
```

### Step 7: Assign mask = value

```python
mask = ~lb_mask & ~ub_mask
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(clipped_df[lb_mask], lb[lb_mask])
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(clipped_df[ub_mask], ub[ub_mask])
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(clipped_df[mask], df[mask])
```


## Complete Example

```python
# Setup
# Fixtures: axis

# Workflow
df = DataFrame(np.random.default_rng(2).standard_normal((1000, 2)))
lb = DataFrame(np.random.default_rng(2).standard_normal((1000, 2)))
ub = lb + 1
clipped_df = df.clip(lb, ub, axis=axis)
lb_mask = df <= lb
ub_mask = df >= ub
mask = ~lb_mask & ~ub_mask
tm.assert_frame_equal(clipped_df[lb_mask], lb[lb_mask])
tm.assert_frame_equal(clipped_df[ub_mask], ub[ub_mask])
tm.assert_frame_equal(clipped_df[mask], df[mask])
```

## Next Steps


---

*Source: test_clip.py:113 | Complexity: Advanced | Last updated: 2026-06-02*