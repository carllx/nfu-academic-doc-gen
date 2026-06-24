# How To: Round

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test round

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs.tslibs.offsets`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign t1 = timedelta_range(...)

```python
t1 = timedelta_range('1 days', periods=3, freq='1 min 2 s 3 us')
```

### Step 2: Assign t2 = value

```python
t2 = -1 * t1
```

### Step 3: Assign t1a = timedelta_range(...)

```python
t1a = timedelta_range('1 days', periods=3, freq='1 min 2 s')
```

### Step 4: Assign t1c = TimedeltaIndex.as_unit(...)

```python
t1c = TimedeltaIndex(np.array([1, 1, 1], 'm8[D]')).as_unit('ns')
```

### Step 5: Assign r1 = t1.round(...)

```python
r1 = t1.round(freq)
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(r1, s1)
```

### Step 7: Assign r2 = t2.round(...)

```python
r2 = t2.round(freq)
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(r2, s2)
```


## Complete Example

```python
# Workflow
t1 = timedelta_range('1 days', periods=3, freq='1 min 2 s 3 us')
t2 = -1 * t1
t1a = timedelta_range('1 days', periods=3, freq='1 min 2 s')
t1c = TimedeltaIndex(np.array([1, 1, 1], 'm8[D]')).as_unit('ns')
for freq, s1, s2 in [('ns', t1, t2), ('us', t1, t2), ('ms', t1a, TimedeltaIndex(['-1 days +00:00:00', '-2 days +23:58:58', '-2 days +23:57:56'])), ('s', t1a, TimedeltaIndex(['-1 days +00:00:00', '-2 days +23:58:58', '-2 days +23:57:56'])), ('12min', t1c, TimedeltaIndex(['-1 days', '-1 days', '-1 days'])), ('h', t1c, TimedeltaIndex(['-1 days', '-1 days', '-1 days'])), ('d', t1c, -1 * t1c)]:
    r1 = t1.round(freq)
    tm.assert_index_equal(r1, s1)
    r2 = t2.round(freq)
    tm.assert_index_equal(r2, s2)
```

## Next Steps


---

*Source: test_scalar_compat.py:99 | Complexity: Advanced | Last updated: 2026-06-02*