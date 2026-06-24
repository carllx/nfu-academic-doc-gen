# How To: 3Levels Leading Period Index

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test 3levels leading period index

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign pi = pd.PeriodIndex(...)

```python
pi = pd.PeriodIndex(['20181101 1100', '20181101 1200', '20181102 1300', '20181102 1400'], name='datetime', freq='D')
```

**Verification:**
```python
assert result == 0.0
```

### Step 2: Assign lev2 = value

```python
lev2 = ['A', 'A', 'Z', 'W']
```

### Step 3: Assign lev3 = value

```python
lev3 = ['B', 'C', 'Q', 'F']
```

### Step 4: Assign mi = MultiIndex.from_arrays(...)

```python
mi = MultiIndex.from_arrays([pi, lev2, lev3])
```

### Step 5: Assign ser = Series(...)

```python
ser = Series(range(4), index=mi, dtype=np.float64)
```

### Step 6: Assign result = value

```python
result = ser.loc[pi[0], 'A', 'B']
```

**Verification:**
```python
assert result == 0.0
```


## Complete Example

```python
# Workflow
pi = pd.PeriodIndex(['20181101 1100', '20181101 1200', '20181102 1300', '20181102 1400'], name='datetime', freq='D')
lev2 = ['A', 'A', 'Z', 'W']
lev3 = ['B', 'C', 'Q', 'F']
mi = MultiIndex.from_arrays([pi, lev2, lev3])
ser = Series(range(4), index=mi, dtype=np.float64)
result = ser.loc[pi[0], 'A', 'B']
assert result == 0.0
```

## Next Steps


---

*Source: test_loc.py:733 | Complexity: Intermediate | Last updated: 2026-06-02*