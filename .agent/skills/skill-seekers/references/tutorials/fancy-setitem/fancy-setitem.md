# How To: Fancy Setitem

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test fancy setitem

## Prerequisites

**Required Modules:**
- `datetime`
- `re`
- `dateutil.tz`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign dti = date_range(...)

```python
dti = date_range(freq='WOM-1FRI', start=datetime(2005, 1, 1), end=datetime(2010, 1, 1))
```

**Verification:**
```python
assert s.iloc[48] == -1
```

### Step 2: Assign s = Series(...)

```python
s = Series(np.arange(len(dti)), index=dti)
```

**Verification:**
```python
assert s.iloc[48] == -2
```

### Step 3: Assign msg = 'Series.__setitem__ treating keys as positions is deprecated'

```python
msg = 'Series.__setitem__ treating keys as positions is deprecated'
```

**Verification:**
```python
assert (s[48:54] == -3).all()
```

### Step 4: Assign unknown = value

```python
s['1/2/2009'] = -2
```

**Verification:**
```python
assert s.iloc[48] == -2
```

### Step 5: Assign unknown = value

```python
s['1/2/2009':'2009-06-05'] = -3
```

**Verification:**
```python
assert (s[48:54] == -3).all()
```

### Step 6: Assign unknown = value

```python
s[48] = -1
```


## Complete Example

```python
# Workflow
dti = date_range(freq='WOM-1FRI', start=datetime(2005, 1, 1), end=datetime(2010, 1, 1))
s = Series(np.arange(len(dti)), index=dti)
msg = 'Series.__setitem__ treating keys as positions is deprecated'
with tm.assert_produces_warning(FutureWarning, match=msg):
    s[48] = -1
assert s.iloc[48] == -1
s['1/2/2009'] = -2
assert s.iloc[48] == -2
s['1/2/2009':'2009-06-05'] = -3
assert (s[48:54] == -3).all()
```

## Next Steps


---

*Source: test_datetime.py:52 | Complexity: Intermediate | Last updated: 2026-06-02*