# How To: Construct From Kwargs Overflow

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test construct from kwargs overflow

## Prerequisites

**Required Modules:**
- `datetime`
- `itertools`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas._libs.tslibs.dtypes`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign msg = 'seconds=86400000000000000000, milliseconds=0, microseconds=0, nanoseconds=0'

```python
msg = 'seconds=86400000000000000000, milliseconds=0, microseconds=0, nanoseconds=0'
```

### Step 2: Assign msg = 'seconds=60000000000000000000, milliseconds=0, microseconds=0, nanoseconds=0'

```python
msg = 'seconds=60000000000000000000, milliseconds=0, microseconds=0, nanoseconds=0'
```

### Step 3: Call Timedelta()

```python
Timedelta(days=10 ** 6)
```

### Step 4: Call Timedelta()

```python
Timedelta(minutes=10 ** 9)
```


## Complete Example

```python
# Workflow
msg = 'seconds=86400000000000000000, milliseconds=0, microseconds=0, nanoseconds=0'
with pytest.raises(OutOfBoundsTimedelta, match=msg):
    Timedelta(days=10 ** 6)
msg = 'seconds=60000000000000000000, milliseconds=0, microseconds=0, nanoseconds=0'
with pytest.raises(OutOfBoundsTimedelta, match=msg):
    Timedelta(minutes=10 ** 9)
```

## Next Steps


---

*Source: test_constructors.py:174 | Complexity: Intermediate | Last updated: 2026-06-02*