# How To: Get Loc Non Scalar Hashable

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test get loc non scalar hashable

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.errors`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas._testing`
- `enum`

**Setup Required:**
```python
# Fixtures: index
```

## Step-by-Step Guide

### Step 1: Assign exc = KeyError

```python
exc = KeyError
```

**Verification:**
```python
assert not is_scalar(E.X1)
```

### Step 2: Assign msg = "<E.X1: 'x1'>"

```python
msg = "<E.X1: 'x1'>"
```

### Step 3: Assign X1 = 'x1'

```python
X1 = 'x1'
```

### Step 4: Assign exc = InvalidIndexError

```python
exc = InvalidIndexError
```

### Step 5: Assign msg = 'E.X1'

```python
msg = 'E.X1'
```

### Step 6: Call index.get_loc()

```python
index.get_loc(E.X1)
```


## Complete Example

```python
# Setup
# Fixtures: index

# Workflow
from enum import Enum

class E(Enum):
    X1 = 'x1'
assert not is_scalar(E.X1)
exc = KeyError
msg = "<E.X1: 'x1'>"
if isinstance(index, (DatetimeIndex, TimedeltaIndex, PeriodIndex, IntervalIndex)):
    exc = InvalidIndexError
    msg = 'E.X1'
with pytest.raises(exc, match=msg):
    index.get_loc(E.X1)
```

## Next Steps


---

*Source: test_indexing.py:188 | Complexity: Intermediate | Last updated: 2026-06-02*