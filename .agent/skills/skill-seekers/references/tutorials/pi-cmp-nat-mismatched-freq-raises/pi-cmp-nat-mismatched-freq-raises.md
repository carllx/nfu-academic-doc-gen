# How To: Pi Cmp Nat Mismatched Freq Raises

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test pi cmp nat mismatched freq raises

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `operator`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`
- `pandas.core.arrays`
- `pandas.tests.arithmetic.common`

**Setup Required:**
```python
# Fixtures: freq
```

## Step-by-Step Guide

### Step 1: Assign idx1 = PeriodIndex(...)

```python
idx1 = PeriodIndex(['2011-01', '2011-02', 'NaT', '2011-05'], freq=freq)
```

### Step 2: Assign diff = PeriodIndex(...)

```python
diff = PeriodIndex(['2011-02', '2011-01', '2011-04', 'NaT'], freq='4M')
```

### Step 3: Assign msg = value

```python
msg = f'Invalid comparison between dtype=period\\[{freq}\\] and PeriodArray'
```

### Step 4: Assign result = value

```python
result = idx1 == diff
```

### Step 5: Assign expected = np.array(...)

```python
expected = np.array([False, False, False, False], dtype=bool)
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 7: idx1 > diff

```python
idx1 > diff
```


## Complete Example

```python
# Setup
# Fixtures: freq

# Workflow
idx1 = PeriodIndex(['2011-01', '2011-02', 'NaT', '2011-05'], freq=freq)
diff = PeriodIndex(['2011-02', '2011-01', '2011-04', 'NaT'], freq='4M')
msg = f'Invalid comparison between dtype=period\\[{freq}\\] and PeriodArray'
with pytest.raises(TypeError, match=msg):
    idx1 > diff
result = idx1 == diff
expected = np.array([False, False, False, False], dtype=bool)
tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_period.py:399 | Complexity: Intermediate | Last updated: 2026-06-02*