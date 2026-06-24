# How To: Nancov

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test nancov

## Prerequisites

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


## Step-by-Step Guide

### Step 1: Assign targ0 = value

```python
targ0 = np.cov(self.arr_float_2d, self.arr_float1_2d)[0, 1]
```

### Step 2: Assign targ1 = value

```python
targ1 = np.cov(self.arr_float_2d.flat, self.arr_float1_2d.flat)[0, 1]
```

### Step 3: Call self.check_nancorr_nancov_2d()

```python
self.check_nancorr_nancov_2d(nanops.nancov, targ0, targ1)
```

### Step 4: Assign targ0 = value

```python
targ0 = np.cov(self.arr_float_1d, self.arr_float1_1d)[0, 1]
```

### Step 5: Assign targ1 = value

```python
targ1 = np.cov(self.arr_float_1d.flat, self.arr_float1_1d.flat)[0, 1]
```

### Step 6: Call self.check_nancorr_nancov_1d()

```python
self.check_nancorr_nancov_1d(nanops.nancov, targ0, targ1)
```


## Complete Example

```python
# Workflow
targ0 = np.cov(self.arr_float_2d, self.arr_float1_2d)[0, 1]
targ1 = np.cov(self.arr_float_2d.flat, self.arr_float1_2d.flat)[0, 1]
self.check_nancorr_nancov_2d(nanops.nancov, targ0, targ1)
targ0 = np.cov(self.arr_float_1d, self.arr_float1_1d)[0, 1]
targ1 = np.cov(self.arr_float_1d.flat, self.arr_float1_1d.flat)[0, 1]
self.check_nancorr_nancov_1d(nanops.nancov, targ0, targ1)
```

## Next Steps


---

*Source: test_nanops.py:734 | Complexity: Intermediate | Last updated: 2026-06-02*