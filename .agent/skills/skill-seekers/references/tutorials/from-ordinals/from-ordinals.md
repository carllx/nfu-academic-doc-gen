# How To: From Ordinals

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test from ordinals

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

### Step 1: Call Period()

```python
Period(ordinal=-1000, freq='Y')
```

### Step 2: Call Period()

```python
Period(ordinal=0, freq='Y')
```

### Step 3: Assign msg = "The 'ordinal' keyword in PeriodIndex is deprecated"

```python
msg = "The 'ordinal' keyword in PeriodIndex is deprecated"
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx1, idx2)
```

### Step 5: Assign alt1 = PeriodIndex.from_ordinals(...)

```python
alt1 = PeriodIndex.from_ordinals([-1, 0, 1], freq='Y')
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(alt1, idx1)
```

### Step 7: Assign alt2 = PeriodIndex.from_ordinals(...)

```python
alt2 = PeriodIndex.from_ordinals(np.array([-1, 0, 1]), freq='Y')
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(alt2, idx2)
```

### Step 9: Assign idx1 = PeriodIndex(...)

```python
idx1 = PeriodIndex(ordinal=[-1, 0, 1], freq='Y')
```

### Step 10: Assign idx2 = PeriodIndex(...)

```python
idx2 = PeriodIndex(ordinal=np.array([-1, 0, 1]), freq='Y')
```


## Complete Example

```python
# Workflow
Period(ordinal=-1000, freq='Y')
Period(ordinal=0, freq='Y')
msg = "The 'ordinal' keyword in PeriodIndex is deprecated"
with tm.assert_produces_warning(FutureWarning, match=msg):
    idx1 = PeriodIndex(ordinal=[-1, 0, 1], freq='Y')
with tm.assert_produces_warning(FutureWarning, match=msg):
    idx2 = PeriodIndex(ordinal=np.array([-1, 0, 1]), freq='Y')
tm.assert_index_equal(idx1, idx2)
alt1 = PeriodIndex.from_ordinals([-1, 0, 1], freq='Y')
tm.assert_index_equal(alt1, idx1)
alt2 = PeriodIndex.from_ordinals(np.array([-1, 0, 1]), freq='Y')
tm.assert_index_equal(alt2, idx2)
```

## Next Steps


---

*Source: test_constructors.py:65 | Complexity: Advanced | Last updated: 2026-06-02*