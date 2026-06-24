# How To: Asfreq Keep Index Name

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test asfreq keep index name

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs.tslibs.offsets`
- `pandas`
- `pandas._testing`
- `pandas.tseries`

**Setup Required:**
```python
# Fixtures: frame_or_series
```

## Step-by-Step Guide

### Step 1: Assign index_name = 'bar'

```python
index_name = 'bar'
```

**Verification:**
```python
assert index_name == obj.index.name
```

### Step 2: Assign index = date_range(...)

```python
index = date_range('20130101', periods=20, name=index_name)
```

**Verification:**
```python
assert index_name == obj.asfreq('10D').index.name
```

### Step 3: Assign obj = DataFrame(...)

```python
obj = DataFrame(list(range(20)), columns=['foo'], index=index)
```

### Step 4: Assign obj = tm.get_obj(...)

```python
obj = tm.get_obj(obj, frame_or_series)
```

**Verification:**
```python
assert index_name == obj.index.name
```


## Complete Example

```python
# Setup
# Fixtures: frame_or_series

# Workflow
index_name = 'bar'
index = date_range('20130101', periods=20, name=index_name)
obj = DataFrame(list(range(20)), columns=['foo'], index=index)
obj = tm.get_obj(obj, frame_or_series)
assert index_name == obj.index.name
assert index_name == obj.asfreq('10D').index.name
```

## Next Steps


---

*Source: test_asfreq.py:97 | Complexity: Intermediate | Last updated: 2026-06-02*