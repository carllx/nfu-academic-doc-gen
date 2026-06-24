# How To: Rolling Corr Cov Other Same Size As Groups

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test rolling corr cov other same size as groups

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.api.indexers`
- `pandas.core.groupby.groupby`

**Setup Required:**
```python
# Fixtures: f, expected_val
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame.set_index(...)

```python
df = DataFrame({'value': range(10), 'idx1': [1] * 5 + [2] * 5, 'idx2': [1, 2, 3, 4, 5] * 2}).set_index(['idx1', 'idx2'])
```

### Step 2: Assign other = DataFrame.set_index(...)

```python
other = DataFrame({'value': range(5), 'idx2': [1, 2, 3, 4, 5]}).set_index('idx2')
```

### Step 3: Assign result = getattr(...)

```python
result = getattr(df.groupby(level=0).rolling(2), f)(other)
```

### Step 4: Assign expected_data = value

```python
expected_data = ([np.nan] + [expected_val] * 4) * 2
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame(expected_data, columns=['value'], index=MultiIndex.from_arrays([[1] * 5 + [2] * 5, [1] * 5 + [2] * 5, list(range(1, 6)) * 2], names=['idx1', 'idx1', 'idx2']))
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: f, expected_val

# Workflow
df = DataFrame({'value': range(10), 'idx1': [1] * 5 + [2] * 5, 'idx2': [1, 2, 3, 4, 5] * 2}).set_index(['idx1', 'idx2'])
other = DataFrame({'value': range(5), 'idx2': [1, 2, 3, 4, 5]}).set_index('idx2')
result = getattr(df.groupby(level=0).rolling(2), f)(other)
expected_data = ([np.nan] + [expected_val] * 4) * 2
expected = DataFrame(expected_data, columns=['value'], index=MultiIndex.from_arrays([[1] * 5 + [2] * 5, [1] * 5 + [2] * 5, list(range(1, 6)) * 2], names=['idx1', 'idx1', 'idx2']))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_groupby.py:150 | Complexity: Intermediate | Last updated: 2026-06-02*