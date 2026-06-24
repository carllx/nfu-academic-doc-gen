# How To: Immutable

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test immutable

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas._libs.tslibs.offsets`
- `pandas._libs.tslibs.offsets`
- `pandas._libs.tslibs.period`
- `pandas.errors`
- `pandas`
- `pandas._testing`
- `pandas.tests.tseries.offsets.common`
- `pandas.tseries`
- `pandas.tseries.offsets`

**Setup Required:**
```python
# Fixtures: offset_types
```

## Step-by-Step Guide

### Step 1: Assign offset = _create_offset(...)

```python
offset = _create_offset(offset_types)
```

### Step 2: Assign msg = 'objects is not writable|DateOffset objects are immutable'

```python
msg = 'objects is not writable|DateOffset objects are immutable'
```

### Step 3: Assign offset.normalize = True

```python
offset.normalize = True
```

### Step 4: Assign offset.n = 91

```python
offset.n = 91
```


## Complete Example

```python
# Setup
# Fixtures: offset_types

# Workflow
offset = _create_offset(offset_types)
msg = 'objects is not writable|DateOffset objects are immutable'
with pytest.raises(AttributeError, match=msg):
    offset.normalize = True
with pytest.raises(AttributeError, match=msg):
    offset.n = 91
```

## Next Steps


---

*Source: test_offsets.py:181 | Complexity: Intermediate | Last updated: 2026-06-02*