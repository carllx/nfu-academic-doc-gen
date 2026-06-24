# How To: Freq Deprecated

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test freq deprecated

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas._libs.tslibs.offsets`
- `pandas._libs.tslibs.period`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign data = np.arange.astype(...)

```python
data = np.arange(5).astype(np.int64)
```

### Step 2: Assign msg = "The 'freq' keyword in the PeriodArray constructor is deprecated"

```python
msg = "The 'freq' keyword in the PeriodArray constructor is deprecated"
```

### Step 3: Assign expected = PeriodArray(...)

```python
expected = PeriodArray(data, dtype='period[M]')
```

### Step 4: Call tm.assert_equal()

```python
tm.assert_equal(res, expected)
```

### Step 5: Assign res = PeriodArray(...)

```python
res = PeriodArray(data, freq='M')
```


## Complete Example

```python
# Workflow
data = np.arange(5).astype(np.int64)
msg = "The 'freq' keyword in the PeriodArray constructor is deprecated"
with tm.assert_produces_warning(FutureWarning, match=msg):
    res = PeriodArray(data, freq='M')
expected = PeriodArray(data, dtype='period[M]')
tm.assert_equal(res, expected)
```

## Next Steps


---

*Source: test_constructors.py:138 | Complexity: Intermediate | Last updated: 2026-06-02*