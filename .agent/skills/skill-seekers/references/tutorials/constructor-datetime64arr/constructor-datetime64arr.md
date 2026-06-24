# How To: Constructor Datetime64Arr

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test constructor datetime64arr

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs.tslibs.period`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign vals = np.arange(...)

```python
vals = np.arange(100000, 100000 + 10000, 100, dtype=np.int64)
```

### Step 2: Assign vals = vals.view(...)

```python
vals = vals.view(np.dtype('M8[us]'))
```

### Step 3: Assign pi = PeriodIndex(...)

```python
pi = PeriodIndex(vals, freq='D')
```

### Step 4: Assign expected = PeriodIndex(...)

```python
expected = PeriodIndex(vals.astype('M8[ns]'), freq='D')
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(pi, expected)
```


## Complete Example

```python
# Workflow
vals = np.arange(100000, 100000 + 10000, 100, dtype=np.int64)
vals = vals.view(np.dtype('M8[us]'))
pi = PeriodIndex(vals, freq='D')
expected = PeriodIndex(vals.astype('M8[ns]'), freq='D')
tm.assert_index_equal(pi, expected)
```

## Next Steps


---

*Source: test_constructors.py:289 | Complexity: Intermediate | Last updated: 2026-06-02*