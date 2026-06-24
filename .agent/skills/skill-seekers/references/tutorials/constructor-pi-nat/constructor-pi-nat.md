# How To: Constructor Pi Nat

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test constructor pi nat

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

### Step 1: Assign idx = PeriodIndex(...)

```python
idx = PeriodIndex([Period('2011-01', freq='M'), NaT, Period('2011-01', freq='M')])
```

### Step 2: Assign exp = PeriodIndex(...)

```python
exp = PeriodIndex(['2011-01', 'NaT', '2011-01'], freq='M')
```

### Step 3: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx, exp)
```

### Step 4: Assign idx = PeriodIndex(...)

```python
idx = PeriodIndex(np.array([Period('2011-01', freq='M'), NaT, Period('2011-01', freq='M')]))
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx, exp)
```

### Step 6: Assign idx = PeriodIndex(...)

```python
idx = PeriodIndex([NaT, NaT, Period('2011-01', freq='M'), Period('2011-01', freq='M')])
```

### Step 7: Assign exp = PeriodIndex(...)

```python
exp = PeriodIndex(['NaT', 'NaT', '2011-01', '2011-01'], freq='M')
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx, exp)
```

### Step 9: Assign idx = PeriodIndex(...)

```python
idx = PeriodIndex(np.array([NaT, NaT, Period('2011-01', freq='M'), Period('2011-01', freq='M')]))
```

### Step 10: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx, exp)
```

### Step 11: Assign idx = PeriodIndex(...)

```python
idx = PeriodIndex([NaT, NaT, '2011-01', '2011-01'], freq='M')
```

### Step 12: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx, exp)
```

### Step 13: Call PeriodIndex()

```python
PeriodIndex([NaT, NaT])
```

### Step 14: Call PeriodIndex()

```python
PeriodIndex(np.array([NaT, NaT]))
```

### Step 15: Call PeriodIndex()

```python
PeriodIndex(['NaT', 'NaT'])
```

### Step 16: Call PeriodIndex()

```python
PeriodIndex(np.array(['NaT', 'NaT']))
```


## Complete Example

```python
# Workflow
idx = PeriodIndex([Period('2011-01', freq='M'), NaT, Period('2011-01', freq='M')])
exp = PeriodIndex(['2011-01', 'NaT', '2011-01'], freq='M')
tm.assert_index_equal(idx, exp)
idx = PeriodIndex(np.array([Period('2011-01', freq='M'), NaT, Period('2011-01', freq='M')]))
tm.assert_index_equal(idx, exp)
idx = PeriodIndex([NaT, NaT, Period('2011-01', freq='M'), Period('2011-01', freq='M')])
exp = PeriodIndex(['NaT', 'NaT', '2011-01', '2011-01'], freq='M')
tm.assert_index_equal(idx, exp)
idx = PeriodIndex(np.array([NaT, NaT, Period('2011-01', freq='M'), Period('2011-01', freq='M')]))
tm.assert_index_equal(idx, exp)
idx = PeriodIndex([NaT, NaT, '2011-01', '2011-01'], freq='M')
tm.assert_index_equal(idx, exp)
with pytest.raises(ValueError, match='freq not specified'):
    PeriodIndex([NaT, NaT])
with pytest.raises(ValueError, match='freq not specified'):
    PeriodIndex(np.array([NaT, NaT]))
with pytest.raises(ValueError, match='freq not specified'):
    PeriodIndex(['NaT', 'NaT'])
with pytest.raises(ValueError, match='freq not specified'):
    PeriodIndex(np.array(['NaT', 'NaT']))
```

## Next Steps


---

*Source: test_constructors.py:351 | Complexity: Advanced | Last updated: 2026-06-02*