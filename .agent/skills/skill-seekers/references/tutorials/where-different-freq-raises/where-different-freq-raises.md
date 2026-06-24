# How To: Where Different Freq Raises

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test where different freq raises

## Prerequisites

- [ ] Setup code must be executed first

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

**Setup Required:**
```python
# Fixtures: other
```

## Step-by-Step Guide

### Step 1: Assign ser = pd.Series(...)

```python
ser = pd.Series(PeriodArray._from_sequence(['2000', '2001', '2002'], dtype='period[D]'))
```

### Step 2: Assign cond = np.array(...)

```python
cond = np.array([True, False, True])
```

### Step 3: Assign res = ser.where(...)

```python
res = ser.where(cond, other)
```

### Step 4: Assign expected = ser.astype.where(...)

```python
expected = ser.astype(object).where(cond, other)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, expected)
```

### Step 6: Call ser.array._where()

```python
ser.array._where(cond, other)
```


## Complete Example

```python
# Setup
# Fixtures: other

# Workflow
ser = pd.Series(PeriodArray._from_sequence(['2000', '2001', '2002'], dtype='period[D]'))
cond = np.array([True, False, True])
with pytest.raises(IncompatibleFrequency, match='freq'):
    ser.array._where(cond, other)
res = ser.where(cond, other)
expected = ser.astype(object).where(cond, other)
tm.assert_series_equal(res, expected)
```

## Next Steps


---

*Source: test_period.py:140 | Complexity: Intermediate | Last updated: 2026-06-02*