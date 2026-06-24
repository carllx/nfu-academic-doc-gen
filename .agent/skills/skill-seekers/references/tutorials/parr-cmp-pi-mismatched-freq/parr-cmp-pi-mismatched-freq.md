# How To: Parr Cmp Pi Mismatched Freq

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test parr cmp pi mismatched freq

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
# Fixtures: freq, box_with_array
```

## Step-by-Step Guide

### Step 1: Assign base = PeriodIndex(...)

```python
base = PeriodIndex(['2011-01', '2011-02', '2011-03', '2011-04'], freq=freq)
```

### Step 2: Assign base = tm.box_expected(...)

```python
base = tm.box_expected(base, box_with_array)
```

### Step 3: Assign msg = value

```python
msg = f'Invalid comparison between dtype=period\\[{freq}\\] and Period'
```

### Step 4: Assign idx = PeriodIndex(...)

```python
idx = PeriodIndex(['2011', '2012', '2013', '2014'], freq='Y')
```

### Step 5: Assign rev_msg = 'Invalid comparison between dtype=period\\[Y-DEC\\] and PeriodArray'

```python
rev_msg = 'Invalid comparison between dtype=period\\[Y-DEC\\] and PeriodArray'
```

### Step 6: Assign idx_msg = value

```python
idx_msg = rev_msg if box_with_array in [tm.to_array, pd.array] else msg
```

### Step 7: Assign msg = value

```python
msg = f'Invalid comparison between dtype=period\\[{freq}\\] and Period'
```

### Step 8: Assign idx = PeriodIndex(...)

```python
idx = PeriodIndex(['2011', '2012', '2013', '2014'], freq='4M')
```

### Step 9: Assign rev_msg = 'Invalid comparison between dtype=period\\[4M\\] and PeriodArray'

```python
rev_msg = 'Invalid comparison between dtype=period\\[4M\\] and PeriodArray'
```

### Step 10: Assign idx_msg = value

```python
idx_msg = rev_msg if box_with_array in [tm.to_array, pd.array] else msg
```

### Step 11: base <= Period('2011', freq='Y')

```python
base <= Period('2011', freq='Y')
```

### Step 12: Period('2011', freq='Y') >= base

```python
Period('2011', freq='Y') >= base
```

### Step 13: base <= idx

```python
base <= idx
```

### Step 14: base <= Period('2011', freq='4M')

```python
base <= Period('2011', freq='4M')
```

### Step 15: Period('2011', freq='4M') >= base

```python
Period('2011', freq='4M') >= base
```

### Step 16: base <= idx

```python
base <= idx
```


## Complete Example

```python
# Setup
# Fixtures: freq, box_with_array

# Workflow
base = PeriodIndex(['2011-01', '2011-02', '2011-03', '2011-04'], freq=freq)
base = tm.box_expected(base, box_with_array)
msg = f'Invalid comparison between dtype=period\\[{freq}\\] and Period'
with pytest.raises(TypeError, match=msg):
    base <= Period('2011', freq='Y')
with pytest.raises(TypeError, match=msg):
    Period('2011', freq='Y') >= base
idx = PeriodIndex(['2011', '2012', '2013', '2014'], freq='Y')
rev_msg = 'Invalid comparison between dtype=period\\[Y-DEC\\] and PeriodArray'
idx_msg = rev_msg if box_with_array in [tm.to_array, pd.array] else msg
with pytest.raises(TypeError, match=idx_msg):
    base <= idx
msg = f'Invalid comparison between dtype=period\\[{freq}\\] and Period'
with pytest.raises(TypeError, match=msg):
    base <= Period('2011', freq='4M')
with pytest.raises(TypeError, match=msg):
    Period('2011', freq='4M') >= base
idx = PeriodIndex(['2011', '2012', '2013', '2014'], freq='4M')
rev_msg = 'Invalid comparison between dtype=period\\[4M\\] and PeriodArray'
idx_msg = rev_msg if box_with_array in [tm.to_array, pd.array] else msg
with pytest.raises(TypeError, match=idx_msg):
    base <= idx
```

## Next Steps


---

*Source: test_period.py:320 | Complexity: Advanced | Last updated: 2026-06-02*