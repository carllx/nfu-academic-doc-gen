# How To: Multi Column Dtype Assignment

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test multi column dtype assignment

## Prerequisites

**Required Modules:**
- `re`
- `weakref`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.tslibs.dtypes`
- `pandas.core.dtypes.base`
- `pandas.core.dtypes.common`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays.sparse`


## Step-by-Step Guide

### Step 1: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame({'a': [0.0], 'b': 0.0})
```

### Step 2: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame({'a': [0], 'b': 0})
```

### Step 3: Assign unknown = 0

```python
df[['a', 'b']] = 0
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, expected)
```

### Step 5: Assign unknown = 0

```python
df['b'] = 0
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, expected)
```


## Complete Example

```python
# Workflow
df = pd.DataFrame({'a': [0.0], 'b': 0.0})
expected = pd.DataFrame({'a': [0], 'b': 0})
df[['a', 'b']] = 0
tm.assert_frame_equal(df, expected)
df['b'] = 0
tm.assert_frame_equal(df, expected)
```

## Next Steps


---

*Source: test_dtypes.py:1225 | Complexity: Intermediate | Last updated: 2026-06-02*