# How To: Not Contains Requires Timestamp

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test not contains requires timestamp

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas`

**Setup Required:**
```python
# Fixtures: scalar
```

## Step-by-Step Guide

### Step 1: Assign dti1 = pd.date_range(...)

```python
dti1 = pd.date_range('2016-01-01', periods=3)
```

### Step 2: Assign dti2 = dti1.insert(...)

```python
dti2 = dti1.insert(1, pd.NaT)
```

### Step 3: Assign dti3 = dti1.insert(...)

```python
dti3 = dti1.insert(3, dti1[0])
```

### Step 4: Assign dti4 = pd.date_range(...)

```python
dti4 = pd.date_range('2016-01-01', freq='ns', periods=2000000)
```

### Step 5: Assign dti5 = dti4.insert(...)

```python
dti5 = dti4.insert(0, dti4[0])
```

### Step 6: Assign msg = unknown.join(...)

```python
msg = '|'.join([re.escape(str(scalar)), re.escape(repr(scalar))])
```

### Step 7: scalar in dti._engine

```python
scalar in dti._engine
```

### Step 8: Call dti._engine.get_loc()

```python
dti._engine.get_loc(scalar)
```


## Complete Example

```python
# Setup
# Fixtures: scalar

# Workflow
dti1 = pd.date_range('2016-01-01', periods=3)
dti2 = dti1.insert(1, pd.NaT)
dti3 = dti1.insert(3, dti1[0])
dti4 = pd.date_range('2016-01-01', freq='ns', periods=2000000)
dti5 = dti4.insert(0, dti4[0])
msg = '|'.join([re.escape(str(scalar)), re.escape(repr(scalar))])
for dti in [dti1, dti2, dti3, dti4, dti5]:
    with pytest.raises(TypeError, match=msg):
        scalar in dti._engine
    with pytest.raises(KeyError, match=msg):
        dti._engine.get_loc(scalar)
```

## Next Steps


---

*Source: test_engines.py:40 | Complexity: Advanced | Last updated: 2026-06-02*