# How To: Reset Index Rename Multiindex

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test reset index rename multiindex

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `itertools`
- `numpy`
- `pytest`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: float_frame
```

## Step-by-Step Guide

### Step 1: Assign stacked_df = value

```python
stacked_df = float_frame.stack(future_stack=True)[::2]
```

### Step 2: Assign stacked_df = DataFrame(...)

```python
stacked_df = DataFrame({'foo': stacked_df, 'bar': stacked_df})
```

### Step 3: Assign names = value

```python
names = ['first', 'second']
```

### Step 4: Assign stacked_df.index.names = names

```python
stacked_df.index.names = names
```

### Step 5: Assign result = stacked_df.reset_index(...)

```python
result = stacked_df.reset_index()
```

### Step 6: Assign expected = stacked_df.reset_index(...)

```python
expected = stacked_df.reset_index(names=['new_first', 'new_second'])
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result['first'], expected['new_first'], check_names=False)
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result['second'], expected['new_second'], check_names=False)
```


## Complete Example

```python
# Setup
# Fixtures: float_frame

# Workflow
stacked_df = float_frame.stack(future_stack=True)[::2]
stacked_df = DataFrame({'foo': stacked_df, 'bar': stacked_df})
names = ['first', 'second']
stacked_df.index.names = names
result = stacked_df.reset_index()
expected = stacked_df.reset_index(names=['new_first', 'new_second'])
tm.assert_series_equal(result['first'], expected['new_first'], check_names=False)
tm.assert_series_equal(result['second'], expected['new_second'], check_names=False)
```

## Next Steps


---

*Source: test_reset_index.py:742 | Complexity: Advanced | Last updated: 2026-06-02*