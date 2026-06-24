# How To: Naive Aware Conflicts

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test naive aware conflicts

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.tseries.offsets`


## Step-by-Step Guide

### Step 1: Assign unknown = value

```python
start, end = (datetime(2009, 1, 1), datetime(2010, 1, 1))
```

### Step 2: Assign naive = date_range(...)

```python
naive = date_range(start, end, freq=BDay(), tz=None)
```

### Step 3: Assign aware = date_range(...)

```python
aware = date_range(start, end, freq=BDay(), tz='Asia/Hong_Kong')
```

### Step 4: Assign msg = 'tz-naive.*tz-aware'

```python
msg = 'tz-naive.*tz-aware'
```

### Step 5: Call naive.join()

```python
naive.join(aware)
```

### Step 6: Call aware.join()

```python
aware.join(naive)
```


## Complete Example

```python
# Workflow
start, end = (datetime(2009, 1, 1), datetime(2010, 1, 1))
naive = date_range(start, end, freq=BDay(), tz=None)
aware = date_range(start, end, freq=BDay(), tz='Asia/Hong_Kong')
msg = 'tz-naive.*tz-aware'
with pytest.raises(TypeError, match=msg):
    naive.join(aware)
with pytest.raises(TypeError, match=msg):
    aware.join(naive)
```

## Next Steps


---

*Source: test_join.py:130 | Complexity: Intermediate | Last updated: 2026-06-02*