# How To: Asof Nanosecond Index Access

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test asof nanosecond index access

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign ts = value

```python
ts = Timestamp('20130101').as_unit('ns')._value
```

**Verification:**
```python
assert dti.resolution == 'nanosecond'
```

### Step 2: Assign dti = DatetimeIndex(...)

```python
dti = DatetimeIndex([ts + 50 + i for i in range(100)])
```

**Verification:**
```python
assert first_value == ser['2013-01-01 00:00:00.000000050']
```

### Step 3: Assign ser = Series(...)

```python
ser = Series(np.random.default_rng(2).standard_normal(100), index=dti)
```

**Verification:**
```python
assert first_value == ser[Timestamp(expected_ts)]
```

### Step 4: Assign first_value = ser.asof(...)

```python
first_value = ser.asof(ser.index[0])
```

**Verification:**
```python
assert dti.resolution == 'nanosecond'
```

### Step 5: Assign expected_ts = np.datetime64(...)

```python
expected_ts = np.datetime64('2013-01-01 00:00:00.000000050', 'ns')
```

**Verification:**
```python
assert first_value == ser[Timestamp(expected_ts)]
```


## Complete Example

```python
# Workflow
ts = Timestamp('20130101').as_unit('ns')._value
dti = DatetimeIndex([ts + 50 + i for i in range(100)])
ser = Series(np.random.default_rng(2).standard_normal(100), index=dti)
first_value = ser.asof(ser.index[0])
assert dti.resolution == 'nanosecond'
assert first_value == ser['2013-01-01 00:00:00.000000050']
expected_ts = np.datetime64('2013-01-01 00:00:00.000000050', 'ns')
assert first_value == ser[Timestamp(expected_ts)]
```

## Next Steps


---

*Source: test_asof.py:21 | Complexity: Intermediate | Last updated: 2026-06-02*