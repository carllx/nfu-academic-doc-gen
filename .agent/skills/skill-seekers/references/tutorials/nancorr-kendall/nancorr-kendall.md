# How To: Nancorr Kendall

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test nancorr kendall

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

### Step 1: Assign sp_stats = pytest.importorskip(...)

```python
sp_stats = pytest.importorskip('scipy.stats')
```

### Step 2: Assign targ0 = value

```python
targ0 = sp_stats.kendalltau(self.arr_float_2d, self.arr_float1_2d)[0]
```

### Step 3: Assign targ1 = value

```python
targ1 = sp_stats.kendalltau(self.arr_float_2d.flat, self.arr_float1_2d.flat)[0]
```

### Step 4: Call self.check_nancorr_nancov_2d()

```python
self.check_nancorr_nancov_2d(nanops.nancorr, targ0, targ1, method='kendall')
```

### Step 5: Assign targ0 = value

```python
targ0 = sp_stats.kendalltau(self.arr_float_1d, self.arr_float1_1d)[0]
```

### Step 6: Assign targ1 = value

```python
targ1 = sp_stats.kendalltau(self.arr_float_1d.flat, self.arr_float1_1d.flat)[0]
```

### Step 7: Call self.check_nancorr_nancov_1d()

```python
self.check_nancorr_nancov_1d(nanops.nancorr, targ0, targ1, method='kendall')
```


## Complete Example

```python
# Workflow
sp_stats = pytest.importorskip('scipy.stats')
targ0 = sp_stats.kendalltau(self.arr_float_2d, self.arr_float1_2d)[0]
targ1 = sp_stats.kendalltau(self.arr_float_2d.flat, self.arr_float1_2d.flat)[0]
self.check_nancorr_nancov_2d(nanops.nancorr, targ0, targ1, method='kendall')
targ0 = sp_stats.kendalltau(self.arr_float_1d, self.arr_float1_1d)[0]
targ1 = sp_stats.kendalltau(self.arr_float_1d.flat, self.arr_float1_1d.flat)[0]
self.check_nancorr_nancov_1d(nanops.nancorr, targ0, targ1, method='kendall')
```

## Next Steps


---

*Source: test_nanops.py:706 | Complexity: Intermediate | Last updated: 2026-06-02*