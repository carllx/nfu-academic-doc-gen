# How To: Group Diff Datetimelike

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test group diff datetimelike

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: data, unit
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1, 2, 2], 'b': data})
```

### Step 2: Assign unknown = unknown.dt.as_unit(...)

```python
df['b'] = df['b'].dt.as_unit(unit)
```

### Step 3: Assign result = unknown.diff(...)

```python
result = df.groupby('a')['b'].diff()
```

### Step 4: Assign expected = Series.dt.as_unit(...)

```python
expected = Series([NaT, NaT, Timedelta('1 days')], name='b').dt.as_unit(unit)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: data, unit

# Workflow
df = DataFrame({'a': [1, 2, 2], 'b': data})
df['b'] = df['b'].dt.as_unit(unit)
result = df.groupby('a')['b'].diff()
expected = Series([NaT, NaT, Timedelta('1 days')], name='b').dt.as_unit(unit)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_groupby_shift_diff.py:120 | Complexity: Intermediate | Last updated: 2026-06-02*