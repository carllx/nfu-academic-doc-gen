# How To: Join Period Index

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test join period index

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.reshape.concat`

**Setup Required:**
```python
# Fixtures: frame_with_period_index
```

## Step-by-Step Guide

### Step 1: Assign other = frame_with_period_index.rename(...)

```python
other = frame_with_period_index.rename(columns=lambda key: f'{key}{key}')
```

### Step 2: Assign joined_values = np.concatenate(...)

```python
joined_values = np.concatenate([frame_with_period_index.values] * 2, axis=1)
```

### Step 3: Assign joined_cols = frame_with_period_index.columns.append(...)

```python
joined_cols = frame_with_period_index.columns.append(other.columns)
```

### Step 4: Assign joined = frame_with_period_index.join(...)

```python
joined = frame_with_period_index.join(other)
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame(data=joined_values, columns=joined_cols, index=frame_with_period_index.index)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(joined, expected)
```


## Complete Example

```python
# Setup
# Fixtures: frame_with_period_index

# Workflow
other = frame_with_period_index.rename(columns=lambda key: f'{key}{key}')
joined_values = np.concatenate([frame_with_period_index.values] * 2, axis=1)
joined_cols = frame_with_period_index.columns.append(other.columns)
joined = frame_with_period_index.join(other)
expected = DataFrame(data=joined_values, columns=joined_cols, index=frame_with_period_index.index)
tm.assert_frame_equal(joined, expected)
```

## Next Steps


---

*Source: test_join.py:350 | Complexity: Intermediate | Last updated: 2026-06-02*