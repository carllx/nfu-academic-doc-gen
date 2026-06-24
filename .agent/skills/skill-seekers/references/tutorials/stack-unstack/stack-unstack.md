# How To: Stack Unstack

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test stack unstack

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `itertools`
- `re`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.reshape`

**Setup Required:**
```python
# Fixtures: float_frame, future_stack
```

## Step-by-Step Guide

### Step 1: Assign df = float_frame.copy(...)

```python
df = float_frame.copy()
```

### Step 2: Assign unknown = np.arange.reshape(...)

```python
df[:] = np.arange(np.prod(df.shape)).reshape(df.shape)
```

### Step 3: Assign stacked = df.stack(...)

```python
stacked = df.stack(future_stack=future_stack)
```

### Step 4: Assign stacked_df = DataFrame(...)

```python
stacked_df = DataFrame({'foo': stacked, 'bar': stacked})
```

### Step 5: Assign unstacked = stacked.unstack(...)

```python
unstacked = stacked.unstack()
```

### Step 6: Assign unstacked_df = stacked_df.unstack(...)

```python
unstacked_df = stacked_df.unstack()
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(unstacked, df)
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(unstacked_df['bar'], df)
```

### Step 9: Assign unstacked_cols = stacked.unstack(...)

```python
unstacked_cols = stacked.unstack(0)
```

### Step 10: Assign unstacked_cols_df = stacked_df.unstack(...)

```python
unstacked_cols_df = stacked_df.unstack(0)
```

### Step 11: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(unstacked_cols.T, df)
```

### Step 12: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(unstacked_cols_df['bar'].T, df)
```


## Complete Example

```python
# Setup
# Fixtures: float_frame, future_stack

# Workflow
df = float_frame.copy()
df[:] = np.arange(np.prod(df.shape)).reshape(df.shape)
stacked = df.stack(future_stack=future_stack)
stacked_df = DataFrame({'foo': stacked, 'bar': stacked})
unstacked = stacked.unstack()
unstacked_df = stacked_df.unstack()
tm.assert_frame_equal(unstacked, df)
tm.assert_frame_equal(unstacked_df['bar'], df)
unstacked_cols = stacked.unstack(0)
unstacked_cols_df = stacked_df.unstack(0)
tm.assert_frame_equal(unstacked_cols.T, df)
tm.assert_frame_equal(unstacked_cols_df['bar'].T, df)
```

## Next Steps


---

*Source: test_stack_unstack.py:31 | Complexity: Advanced | Last updated: 2026-06-02*