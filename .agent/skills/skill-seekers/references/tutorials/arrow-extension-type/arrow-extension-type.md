# How To: Arrow Extension Type

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test arrow extension type

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`
- `pandas.core.arrays.arrow.extension_types`
- `pandas.core.arrays.arrow.extension_types`
- `pandas.core.arrays.arrow.extension_types`
- `pandas.core.arrays.arrow.extension_types`


## Step-by-Step Guide

### Step 1: Assign pa = pytest.importorskip(...)

```python
pa = pytest.importorskip('pyarrow')
```

**Verification:**
```python
assert p1.closed == 'left'
```

### Step 2: Assign p1 = ArrowIntervalType(...)

```python
p1 = ArrowIntervalType(pa.int64(), 'left')
```

**Verification:**
```python
assert p1 == p2
```

### Step 3: Assign p2 = ArrowIntervalType(...)

```python
p2 = ArrowIntervalType(pa.int64(), 'left')
```

**Verification:**
```python
assert p1 != p3
```

### Step 4: Assign p3 = ArrowIntervalType(...)

```python
p3 = ArrowIntervalType(pa.int64(), 'right')
```

**Verification:**
```python
assert hash(p1) == hash(p2)
```


## Complete Example

```python
# Workflow
pa = pytest.importorskip('pyarrow')
from pandas.core.arrays.arrow.extension_types import ArrowIntervalType
p1 = ArrowIntervalType(pa.int64(), 'left')
p2 = ArrowIntervalType(pa.int64(), 'left')
p3 = ArrowIntervalType(pa.int64(), 'right')
assert p1.closed == 'left'
assert p1 == p2
assert p1 != p3
assert hash(p1) == hash(p2)
assert hash(p1) != hash(p3)
```

## Next Steps


---

*Source: test_interval_pyarrow.py:9 | Complexity: Intermediate | Last updated: 2026-06-02*