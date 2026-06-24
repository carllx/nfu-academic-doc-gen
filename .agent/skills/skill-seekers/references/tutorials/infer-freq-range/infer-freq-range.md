# How To: Infer Freq Range

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test infer freq range

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs.tslibs.ccalendar`
- `pandas._libs.tslibs.offsets`
- `pandas._libs.tslibs.period`
- `pandas.compat`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`
- `pandas.core.tools.datetimes`
- `pandas.tseries`

**Setup Required:**
```python
# Fixtures: periods, freq
```

## Step-by-Step Guide

### Step 1: Assign freq = freq.upper(...)

```python
freq = freq.upper()
```

**Verification:**
```python
assert frequencies.infer_freq(index) == gen.freqstr
```

### Step 2: Assign gen = date_range(...)

```python
gen = date_range('1/1/2000', periods=periods, freq=freq)
```

**Verification:**
```python
assert is_dec_range or is_nov_range or is_oct_range
```

### Step 3: Assign index = DatetimeIndex(...)

```python
index = DatetimeIndex(gen.values)
```

**Verification:**
```python
assert frequencies.infer_freq(index) == gen.freqstr
```

### Step 4: Assign inf_freq = frequencies.infer_freq(...)

```python
inf_freq = frequencies.infer_freq(index)
```

### Step 5: Assign is_dec_range = value

```python
is_dec_range = inf_freq == 'QE-DEC' and gen.freqstr in ('QE', 'QE-DEC', 'QE-SEP', 'QE-JUN', 'QE-MAR')
```

### Step 6: Assign is_nov_range = value

```python
is_nov_range = inf_freq == 'QE-NOV' and gen.freqstr in ('QE-NOV', 'QE-AUG', 'QE-MAY', 'QE-FEB')
```

### Step 7: Assign is_oct_range = value

```python
is_oct_range = inf_freq == 'QE-OCT' and gen.freqstr in ('QE-OCT', 'QE-JUL', 'QE-APR', 'QE-JAN')
```

**Verification:**
```python
assert is_dec_range or is_nov_range or is_oct_range
```


## Complete Example

```python
# Setup
# Fixtures: periods, freq

# Workflow
freq = freq.upper()
gen = date_range('1/1/2000', periods=periods, freq=freq)
index = DatetimeIndex(gen.values)
if not freq.startswith('QE-'):
    assert frequencies.infer_freq(index) == gen.freqstr
else:
    inf_freq = frequencies.infer_freq(index)
    is_dec_range = inf_freq == 'QE-DEC' and gen.freqstr in ('QE', 'QE-DEC', 'QE-SEP', 'QE-JUN', 'QE-MAR')
    is_nov_range = inf_freq == 'QE-NOV' and gen.freqstr in ('QE-NOV', 'QE-AUG', 'QE-MAY', 'QE-FEB')
    is_oct_range = inf_freq == 'QE-OCT' and gen.freqstr in ('QE-OCT', 'QE-JUL', 'QE-APR', 'QE-JAN')
    assert is_dec_range or is_nov_range or is_oct_range
```

## Next Steps


---

*Source: test_inference.py:65 | Complexity: Intermediate | Last updated: 2026-06-02*