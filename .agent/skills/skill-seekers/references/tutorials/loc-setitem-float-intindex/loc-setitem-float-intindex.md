# How To: Loc Setitem Float Intindex

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test loc setitem float intindex

## Prerequisites

**Required Modules:**
- `collections`
- `contextlib`
- `datetime`
- `re`
- `dateutil.tz`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas._libs`
- `pandas.compat.numpy`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.api.types`
- `pandas.core.indexing`
- `pandas.tests.indexing.common`


## Step-by-Step Guide

### Step 1: Assign rand_data = np.random.default_rng.standard_normal(...)

```python
rand_data = np.random.default_rng(2).standard_normal((8, 4))
```

### Step 2: Assign result = DataFrame(...)

```python
result = DataFrame(rand_data)
```

### Step 3: Assign unknown = value

```python
result.loc[:, 0.5] = np.nan
```

### Step 4: Assign expected_data = np.hstack(...)

```python
expected_data = np.hstack((rand_data, np.array([np.nan] * 8).reshape(8, 1)))
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame(expected_data, columns=[0.0, 1.0, 2.0, 3.0, 0.5])
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Assign result = DataFrame(...)

```python
result = DataFrame(rand_data)
```

### Step 8: Assign unknown = value

```python
result.loc[:, 0.5] = np.nan
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
rand_data = np.random.default_rng(2).standard_normal((8, 4))
result = DataFrame(rand_data)
result.loc[:, 0.5] = np.nan
expected_data = np.hstack((rand_data, np.array([np.nan] * 8).reshape(8, 1)))
expected = DataFrame(expected_data, columns=[0.0, 1.0, 2.0, 3.0, 0.5])
tm.assert_frame_equal(result, expected)
result = DataFrame(rand_data)
result.loc[:, 0.5] = np.nan
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_loc.py:2878 | Complexity: Advanced | Last updated: 2026-06-02*