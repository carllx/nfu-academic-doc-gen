# How To: Index Ops Defer To Unknown Subclasses

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test index ops defer to unknown subclasses

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `decimal`
- `operator`
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`

**Setup Required:**
```python
# Fixtures: other
```

## Step-by-Step Guide

### Step 1: Assign values = np.array(...)

```python
values = np.array([datetime.date(2000, 1, 1), datetime.date(2000, 1, 2)], dtype=object)
```

**Verification:**
```python
assert isinstance(result, MyIndex)
```

### Step 2: Assign a = MyIndex._simple_new(...)

```python
a = MyIndex._simple_new(values)
```

**Verification:**
```python
assert a._calls == 1
```

### Step 3: Assign other = pd.Index(...)

```python
other = pd.Index(other)
```

### Step 4: Assign result = value

```python
result = other + a
```

**Verification:**
```python
assert isinstance(result, MyIndex)
```


## Complete Example

```python
# Setup
# Fixtures: other

# Workflow
values = np.array([datetime.date(2000, 1, 1), datetime.date(2000, 1, 2)], dtype=object)
a = MyIndex._simple_new(values)
other = pd.Index(other)
result = other + a
assert isinstance(result, MyIndex)
assert a._calls == 1
```

## Next Steps


---

*Source: test_object.py:405 | Complexity: Intermediate | Last updated: 2026-06-02*