# How To: Series Box Timestamp

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test series box timestamp

## Prerequisites

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.errors`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign rng = date_range(...)

```python
rng = date_range('20090415', '20090519', freq='B')
```

**Verification:**
```python
assert isinstance(ser[0], Timestamp)
```

### Step 2: Assign ser = Series(...)

```python
ser = Series(rng)
```

**Verification:**
```python
assert isinstance(ser.at[1], Timestamp)
```

### Step 3: Assign ser = Series(...)

```python
ser = Series(rng, index=rng)
```

**Verification:**
```python
assert isinstance(ser.iat[2], Timestamp)
```

### Step 4: Assign msg = 'Series.__getitem__ treating keys as positions is deprecated'

```python
msg = 'Series.__getitem__ treating keys as positions is deprecated'
```

**Verification:**
```python
assert isinstance(ser.loc[3], Timestamp)
```


## Complete Example

```python
# Workflow
rng = date_range('20090415', '20090519', freq='B')
ser = Series(rng)
assert isinstance(ser[0], Timestamp)
assert isinstance(ser.at[1], Timestamp)
assert isinstance(ser.iat[2], Timestamp)
assert isinstance(ser.loc[3], Timestamp)
assert isinstance(ser.iloc[4], Timestamp)
ser = Series(rng, index=rng)
msg = 'Series.__getitem__ treating keys as positions is deprecated'
with tm.assert_produces_warning(FutureWarning, match=msg):
    assert isinstance(ser[0], Timestamp)
assert isinstance(ser.at[rng[1]], Timestamp)
assert isinstance(ser.iat[2], Timestamp)
assert isinstance(ser.loc[rng[3]], Timestamp)
assert isinstance(ser.iloc[4], Timestamp)
```

## Next Steps


---

*Source: test_indexing.py:149 | Complexity: Intermediate | Last updated: 2026-06-02*