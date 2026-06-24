# How To: Sub Period Overflow

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test sub period overflow

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas._libs.tslibs.period`
- `pandas.core.dtypes.base`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign dti = pd.date_range(...)

```python
dti = pd.date_range('1677-09-22', periods=2, freq='D')
```

### Step 2: Assign pi = dti.to_period(...)

```python
pi = dti.to_period('ns')
```

### Step 3: Assign per = pd.Period._from_ordinal(...)

```python
per = pd.Period._from_ordinal(10 ** 14, pi.freq)
```

### Step 4: pi - per

```python
pi - per
```

### Step 5: per - pi

```python
per - pi
```


## Complete Example

```python
# Workflow
dti = pd.date_range('1677-09-22', periods=2, freq='D')
pi = dti.to_period('ns')
per = pd.Period._from_ordinal(10 ** 14, pi.freq)
with pytest.raises(OverflowError, match='Overflow in int64 addition'):
    pi - per
with pytest.raises(OverflowError, match='Overflow in int64 addition'):
    per - pi
```

## Next Steps


---

*Source: test_period.py:115 | Complexity: Intermediate | Last updated: 2026-06-02*