# How To: Select Dtypes Exclude Include Int

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test select dtypes exclude include int

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`

**Setup Required:**
```python
# Fixtures: include
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': list('abc'), 'b': list(range(1, 4)), 'c': np.arange(3, 6, dtype='int32'), 'd': np.arange(4.0, 7.0, dtype='float64'), 'e': [True, False, True], 'f': pd.date_range('now', periods=3).values})
```

### Step 2: Assign exclude = value

```python
exclude = (np.datetime64,)
```

### Step 3: Assign result = df.select_dtypes(...)

```python
result = df.select_dtypes(include=include, exclude=exclude)
```

### Step 4: Assign expected = value

```python
expected = df[['b', 'c', 'e']]
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: include

# Workflow
df = DataFrame({'a': list('abc'), 'b': list(range(1, 4)), 'c': np.arange(3, 6, dtype='int32'), 'd': np.arange(4.0, 7.0, dtype='float64'), 'e': [True, False, True], 'f': pd.date_range('now', periods=3).values})
exclude = (np.datetime64,)
result = df.select_dtypes(include=include, exclude=exclude)
expected = df[['b', 'c', 'e']]
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_select_dtypes.py:149 | Complexity: Intermediate | Last updated: 2026-06-02*