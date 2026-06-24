# How To: Setitem Raises Incompatible Freq

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test setitem raises incompatible freq

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

### Step 1: Assign arr = PeriodArray(...)

```python
arr = PeriodArray(np.arange(3), dtype='period[D]')
```

### Step 2: Assign other = PeriodArray._from_sequence(...)

```python
other = PeriodArray._from_sequence(['2000', '2001'], dtype='period[Y]')
```

### Step 3: Assign unknown = pd.Period(...)

```python
arr[0] = pd.Period('2000', freq='Y')
```

### Step 4: Assign unknown = other

```python
arr[[0, 1]] = other
```


## Complete Example

```python
# Workflow
arr = PeriodArray(np.arange(3), dtype='period[D]')
with pytest.raises(IncompatibleFrequency, match='freq'):
    arr[0] = pd.Period('2000', freq='Y')
other = PeriodArray._from_sequence(['2000', '2001'], dtype='period[Y]')
with pytest.raises(IncompatibleFrequency, match='freq'):
    arr[[0, 1]] = other
```

## Next Steps


---

*Source: test_period.py:82 | Complexity: Intermediate | Last updated: 2026-06-02*