# How To: Array Strptime Resolution Todaynow

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test array strptime resolution todaynow

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs.tslibs.dtypes`
- `pandas._libs.tslibs.strptime`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign vals = np.array(...)

```python
vals = np.array(['today', np.datetime64('2017-01-01', 'us')], dtype=object)
```

**Verification:**
```python
assert res.dtype == 'M8[us]'
```

### Step 2: Assign now = value

```python
now = Timestamp('now').asm8
```

**Verification:**
```python
assert abs(res[0] - now) < tolerance
```

### Step 3: Assign unknown = array_strptime(...)

```python
res, _ = array_strptime(vals, fmt='%Y-%m-%d', utc=False, creso=creso_infer)
```

**Verification:**
```python
assert res[1] == vals[1]
```

### Step 4: Assign unknown = array_strptime(...)

```python
res2, _ = array_strptime(vals[::-1], fmt='%Y-%m-%d', utc=False, creso=creso_infer)
```

**Verification:**
```python
assert res2.dtype == 'M8[us]'
```

### Step 5: Assign tolerance = np.timedelta64(...)

```python
tolerance = np.timedelta64(1, 's')
```

**Verification:**
```python
assert abs(res2[1] - now) < tolerance * 2
```


## Complete Example

```python
# Workflow
vals = np.array(['today', np.datetime64('2017-01-01', 'us')], dtype=object)
now = Timestamp('now').asm8
res, _ = array_strptime(vals, fmt='%Y-%m-%d', utc=False, creso=creso_infer)
res2, _ = array_strptime(vals[::-1], fmt='%Y-%m-%d', utc=False, creso=creso_infer)
tolerance = np.timedelta64(1, 's')
assert res.dtype == 'M8[us]'
assert abs(res[0] - now) < tolerance
assert res[1] == vals[1]
assert res2.dtype == 'M8[us]'
assert abs(res2[1] - now) < tolerance * 2
assert res2[0] == vals[1]
```

## Next Steps


---

*Source: test_strptime.py:76 | Complexity: Intermediate | Last updated: 2026-06-02*