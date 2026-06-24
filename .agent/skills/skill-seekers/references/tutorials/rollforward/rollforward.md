# How To: Rollforward

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test rollforward

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas._libs.tslibs.offsets`
- `pandas._libs.tslibs.offsets`
- `pandas._libs.tslibs.period`
- `pandas.errors`
- `pandas`
- `pandas._testing`
- `pandas.tests.tseries.offsets.common`
- `pandas.tseries`
- `pandas.tseries.offsets`

**Setup Required:**
```python
# Fixtures: offset_types, expecteds
```

## Step-by-Step Guide

### Step 1: Assign expecteds = expecteds.copy(...)

```python
expecteds = expecteds.copy()
```

### Step 2: Assign no_changes = value

```python
no_changes = ['Day', 'MonthBegin', 'SemiMonthBegin', 'YearBegin', 'Week', 'Hour', 'Minute', 'Second', 'Milli', 'Micro', 'Nano', 'DateOffset']
```

### Step 3: Assign unknown = Timestamp(...)

```python
expecteds['BusinessHour'] = Timestamp('2011-01-03 09:00:00')
```

### Step 4: Assign unknown = Timestamp(...)

```python
expecteds['CustomBusinessHour'] = Timestamp('2011-01-03 09:00:00')
```

### Step 5: Assign norm_expected = expecteds.copy(...)

```python
norm_expected = expecteds.copy()
```

### Step 6: Assign normalized = value

```python
normalized = {'Day': Timestamp('2011-01-02 00:00:00'), 'DateOffset': Timestamp('2011-01-02 00:00:00'), 'MonthBegin': Timestamp('2011-02-01 00:00:00'), 'SemiMonthBegin': Timestamp('2011-01-15 00:00:00'), 'YearBegin': Timestamp('2012-01-01 00:00:00'), 'Week': Timestamp('2011-01-08 00:00:00'), 'Hour': Timestamp('2011-01-01 00:00:00'), 'Minute': Timestamp('2011-01-01 00:00:00'), 'Second': Timestamp('2011-01-01 00:00:00'), 'Milli': Timestamp('2011-01-01 00:00:00'), 'Micro': Timestamp('2011-01-01 00:00:00')}
```

### Step 7: Call norm_expected.update()

```python
norm_expected.update(normalized)
```

### Step 8: Assign sdt = datetime(...)

```python
sdt = datetime(2011, 1, 1, 9, 0)
```

### Step 9: Assign ndt = np.datetime64(...)

```python
ndt = np.datetime64('2011-01-01 09:00')
```

### Step 10: Assign unknown = Timestamp(...)

```python
expecteds[n] = Timestamp('2011/01/01 09:00')
```

### Step 11: Assign unknown = Timestamp(...)

```python
norm_expected[k] = Timestamp(norm_expected[k].date())
```

### Step 12: Assign expected = value

```python
expected = expecteds[offset_types.__name__]
```

### Step 13: Call self._check_offsetfunc_works()

```python
self._check_offsetfunc_works(offset_types, 'rollforward', dt, expected)
```

### Step 14: Assign expected = value

```python
expected = norm_expected[offset_types.__name__]
```

### Step 15: Call self._check_offsetfunc_works()

```python
self._check_offsetfunc_works(offset_types, 'rollforward', dt, expected, normalize=True)
```


## Complete Example

```python
# Setup
# Fixtures: offset_types, expecteds

# Workflow
expecteds = expecteds.copy()
no_changes = ['Day', 'MonthBegin', 'SemiMonthBegin', 'YearBegin', 'Week', 'Hour', 'Minute', 'Second', 'Milli', 'Micro', 'Nano', 'DateOffset']
for n in no_changes:
    expecteds[n] = Timestamp('2011/01/01 09:00')
expecteds['BusinessHour'] = Timestamp('2011-01-03 09:00:00')
expecteds['CustomBusinessHour'] = Timestamp('2011-01-03 09:00:00')
norm_expected = expecteds.copy()
for k in norm_expected:
    norm_expected[k] = Timestamp(norm_expected[k].date())
normalized = {'Day': Timestamp('2011-01-02 00:00:00'), 'DateOffset': Timestamp('2011-01-02 00:00:00'), 'MonthBegin': Timestamp('2011-02-01 00:00:00'), 'SemiMonthBegin': Timestamp('2011-01-15 00:00:00'), 'YearBegin': Timestamp('2012-01-01 00:00:00'), 'Week': Timestamp('2011-01-08 00:00:00'), 'Hour': Timestamp('2011-01-01 00:00:00'), 'Minute': Timestamp('2011-01-01 00:00:00'), 'Second': Timestamp('2011-01-01 00:00:00'), 'Milli': Timestamp('2011-01-01 00:00:00'), 'Micro': Timestamp('2011-01-01 00:00:00')}
norm_expected.update(normalized)
sdt = datetime(2011, 1, 1, 9, 0)
ndt = np.datetime64('2011-01-01 09:00')
for dt in [sdt, ndt]:
    expected = expecteds[offset_types.__name__]
    self._check_offsetfunc_works(offset_types, 'rollforward', dt, expected)
    expected = norm_expected[offset_types.__name__]
    self._check_offsetfunc_works(offset_types, 'rollforward', dt, expected, normalize=True)
```

## Next Steps


---

*Source: test_offsets.py:319 | Complexity: Advanced | Last updated: 2026-06-02*