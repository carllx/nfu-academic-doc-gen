# How To: Metadata Propagation

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test metadata propagation

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `copy`
- `numpy`
- `pytest`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: frame_or_series
```

## Step-by-Step Guide

### Step 1: Assign o = construct(...)

```python
o = construct(frame_or_series, shape=3)
```

### Step 2: Assign o.name = 'foo'

```python
o.name = 'foo'
```

### Step 3: Assign o2 = construct(...)

```python
o2 = construct(frame_or_series, shape=3)
```

### Step 4: Assign o2.name = 'bar'

```python
o2.name = 'bar'
```

### Step 5: Assign result = o.combine_first(...)

```python
result = o.combine_first(o2)
```

### Step 6: Call tm.assert_metadata_equivalent()

```python
tm.assert_metadata_equivalent(o, result)
```

### Step 7: Assign result = value

```python
result = o + o2
```

### Step 8: Call tm.assert_metadata_equivalent()

```python
tm.assert_metadata_equivalent(result)
```

### Step 9: Assign result = getattr(...)

```python
result = getattr(o, op)(1)
```

### Step 10: Call tm.assert_metadata_equivalent()

```python
tm.assert_metadata_equivalent(o, result)
```

### Step 11: Assign result = getattr(...)

```python
result = getattr(o, op)(o)
```

### Step 12: Call tm.assert_metadata_equivalent()

```python
tm.assert_metadata_equivalent(o, result)
```

### Step 13: Assign v1 = getattr(...)

```python
v1 = getattr(o, op)(o)
```

### Step 14: Call tm.assert_metadata_equivalent()

```python
tm.assert_metadata_equivalent(o, v1)
```

### Step 15: Call tm.assert_metadata_equivalent()

```python
tm.assert_metadata_equivalent(o, v1 & v1)
```

### Step 16: Call tm.assert_metadata_equivalent()

```python
tm.assert_metadata_equivalent(o, v1 | v1)
```

### Step 17: Assign v1 = getattr(...)

```python
v1 = getattr(o, op)(o)
```

### Step 18: Assign v2 = getattr(...)

```python
v2 = getattr(o, op)(o2)
```

### Step 19: Call tm.assert_metadata_equivalent()

```python
tm.assert_metadata_equivalent(v2)
```

### Step 20: Call tm.assert_metadata_equivalent()

```python
tm.assert_metadata_equivalent(v1 & v2)
```

### Step 21: Call tm.assert_metadata_equivalent()

```python
tm.assert_metadata_equivalent(v1 | v2)
```


## Complete Example

```python
# Setup
# Fixtures: frame_or_series

# Workflow
o = construct(frame_or_series, shape=3)
o.name = 'foo'
o2 = construct(frame_or_series, shape=3)
o2.name = 'bar'
for op in ['__add__', '__sub__', '__truediv__', '__mul__']:
    result = getattr(o, op)(1)
    tm.assert_metadata_equivalent(o, result)
for op in ['__add__', '__sub__', '__truediv__', '__mul__']:
    result = getattr(o, op)(o)
    tm.assert_metadata_equivalent(o, result)
for op in ['__eq__', '__le__', '__ge__']:
    v1 = getattr(o, op)(o)
    tm.assert_metadata_equivalent(o, v1)
    tm.assert_metadata_equivalent(o, v1 & v1)
    tm.assert_metadata_equivalent(o, v1 | v1)
result = o.combine_first(o2)
tm.assert_metadata_equivalent(o, result)
result = o + o2
tm.assert_metadata_equivalent(result)
for op in ['__eq__', '__le__', '__ge__']:
    v1 = getattr(o, op)(o)
    v2 = getattr(o, op)(o2)
    tm.assert_metadata_equivalent(v2)
    tm.assert_metadata_equivalent(v1 & v2)
    tm.assert_metadata_equivalent(v1 | v2)
```

## Next Steps


---

*Source: test_generic.py:174 | Complexity: Advanced | Last updated: 2026-06-02*