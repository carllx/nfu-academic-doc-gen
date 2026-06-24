# How To: Nanvar Nans

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test nanvar nans

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `functools`
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`

**Setup Required:**
```python
# Fixtures: samples, variance
```

## Step-by-Step Guide

### Step 1: Assign samples_test = value

```python
samples_test = np.nan * np.ones(2 * samples.shape[0])
```

### Step 2: Assign unknown = samples

```python
samples_test[::2] = samples
```

### Step 3: Assign actual_variance = nanops.nanvar(...)

```python
actual_variance = nanops.nanvar(samples_test, skipna=True)
```

### Step 4: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(actual_variance, variance, rtol=0.01)
```

### Step 5: Assign actual_variance = nanops.nanvar(...)

```python
actual_variance = nanops.nanvar(samples_test, skipna=False)
```

### Step 6: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(actual_variance, np.nan, rtol=0.01)
```


## Complete Example

```python
# Setup
# Fixtures: samples, variance

# Workflow
samples_test = np.nan * np.ones(2 * samples.shape[0])
samples_test[::2] = samples
actual_variance = nanops.nanvar(samples_test, skipna=True)
tm.assert_almost_equal(actual_variance, variance, rtol=0.01)
actual_variance = nanops.nanvar(samples_test, skipna=False)
tm.assert_almost_equal(actual_variance, np.nan, rtol=0.01)
```

## Next Steps


---

*Source: test_nanops.py:900 | Complexity: Intermediate | Last updated: 2026-06-02*