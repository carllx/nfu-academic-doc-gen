# How To: Tz Localize To Utc Ambiguous Infer

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test tz localize to utc ambiguous infer

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.tslibs.tzconversion`


## Step-by-Step Guide

### Step 1: Assign val = 1320541200000000000

```python
val = 1320541200000000000
```

### Step 2: Assign vals = np.array(...)

```python
vals = np.array([val, val - 1, val], dtype=np.int64)
```

### Step 3: Assign msg = 'There are 2 dst switches when there should only be 1'

```python
msg = 'There are 2 dst switches when there should only be 1'
```

### Step 4: Call tz_localize_to_utc()

```python
tz_localize_to_utc(vals, pytz.timezone('US/Eastern'), ambiguous='infer')
```

### Step 5: Call tz_localize_to_utc()

```python
tz_localize_to_utc(vals[:1], pytz.timezone('US/Eastern'), ambiguous='infer')
```

### Step 6: Call tz_localize_to_utc()

```python
tz_localize_to_utc(vals, pytz.timezone('US/Eastern'), ambiguous='infer')
```


## Complete Example

```python
# Workflow
val = 1320541200000000000
vals = np.array([val, val - 1, val], dtype=np.int64)
with pytest.raises(pytz.AmbiguousTimeError, match='2011-11-06 01:00:00'):
    tz_localize_to_utc(vals, pytz.timezone('US/Eastern'), ambiguous='infer')
with pytest.raises(pytz.AmbiguousTimeError, match='are no repeated times'):
    tz_localize_to_utc(vals[:1], pytz.timezone('US/Eastern'), ambiguous='infer')
vals[1] += 1
msg = 'There are 2 dst switches when there should only be 1'
with pytest.raises(pytz.AmbiguousTimeError, match=msg):
    tz_localize_to_utc(vals, pytz.timezone('US/Eastern'), ambiguous='infer')
```

## Next Steps


---

*Source: test_tzconversion.py:9 | Complexity: Intermediate | Last updated: 2026-06-02*