# How To: Get Loc Naive Dti Aware Str Deprecated

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test get loc naive dti aware str deprecated

## Prerequisites

**Required Modules:**
- `re`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign ts = value

```python
ts = Timestamp('20130101')._value
```

### Step 2: Assign dti = pd.DatetimeIndex(...)

```python
dti = pd.DatetimeIndex([ts + 50 + i for i in range(100)])
```

### Step 3: Assign ser = Series(...)

```python
ser = Series(range(100), index=dti)
```

### Step 4: Assign key = '2013-01-01 00:00:00.000000050+0000'

```python
key = '2013-01-01 00:00:00.000000050+0000'
```

### Step 5: Assign msg = re.escape(...)

```python
msg = re.escape(repr(key))
```

### Step 6: ser[key]

```python
ser[key]
```

### Step 7: Call dti.get_loc()

```python
dti.get_loc(key)
```


## Complete Example

```python
# Workflow
ts = Timestamp('20130101')._value
dti = pd.DatetimeIndex([ts + 50 + i for i in range(100)])
ser = Series(range(100), index=dti)
key = '2013-01-01 00:00:00.000000050+0000'
msg = re.escape(repr(key))
with pytest.raises(KeyError, match=msg):
    ser[key]
with pytest.raises(KeyError, match=msg):
    dti.get_loc(key)
```

## Next Steps


---

*Source: test_datetime.py:17 | Complexity: Intermediate | Last updated: 2026-06-02*