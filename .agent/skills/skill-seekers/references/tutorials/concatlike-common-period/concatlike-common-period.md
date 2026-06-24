# How To: Concatlike Common Period

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test concatlike common period

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign pi1 = pd.PeriodIndex(...)

```python
pi1 = pd.PeriodIndex(['2011-01', '2011-02'], freq='M')
```

### Step 2: Assign pi2 = pd.PeriodIndex(...)

```python
pi2 = pd.PeriodIndex(['2012-01', '2012-02'], freq='M')
```

### Step 3: Assign exp = pd.PeriodIndex(...)

```python
exp = pd.PeriodIndex(['2011-01', '2011-02', '2012-01', '2012-02'], freq='M')
```

### Step 4: Assign res = pi1.append(...)

```python
res = pi1.append(pi2)
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(res, exp)
```

### Step 6: Assign ps1 = Series(...)

```python
ps1 = Series(pi1)
```

### Step 7: Assign ps2 = Series(...)

```python
ps2 = Series(pi2)
```

### Step 8: Assign res = ps1._append(...)

```python
res = ps1._append(ps2)
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, Series(exp, index=[0, 1, 0, 1]))
```

### Step 10: Assign res = pd.concat(...)

```python
res = pd.concat([ps1, ps2])
```

### Step 11: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, Series(exp, index=[0, 1, 0, 1]))
```


## Complete Example

```python
# Workflow
pi1 = pd.PeriodIndex(['2011-01', '2011-02'], freq='M')
pi2 = pd.PeriodIndex(['2012-01', '2012-02'], freq='M')
exp = pd.PeriodIndex(['2011-01', '2011-02', '2012-01', '2012-02'], freq='M')
res = pi1.append(pi2)
tm.assert_index_equal(res, exp)
ps1 = Series(pi1)
ps2 = Series(pi2)
res = ps1._append(ps2)
tm.assert_series_equal(res, Series(exp, index=[0, 1, 0, 1]))
res = pd.concat([ps1, ps2])
tm.assert_series_equal(res, Series(exp, index=[0, 1, 0, 1]))
```

## Next Steps


---

*Source: test_append_common.py:379 | Complexity: Advanced | Last updated: 2026-06-02*