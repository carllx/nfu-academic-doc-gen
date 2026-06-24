# How To: Not Contains Requires Timedelta

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test not contains requires timedelta

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

### Step 1: Assign tdi1 = pd.timedelta_range(...)

```python
tdi1 = pd.timedelta_range('42 days', freq='9h', periods=1234)
```

### Step 2: Assign tdi2 = tdi1.insert(...)

```python
tdi2 = tdi1.insert(1, pd.NaT)
```

### Step 3: Assign tdi3 = tdi1.insert(...)

```python
tdi3 = tdi1.insert(3, tdi1[0])
```

### Step 4: Assign tdi4 = pd.timedelta_range(...)

```python
tdi4 = pd.timedelta_range('42 days', freq='ns', periods=2000000)
```

### Step 5: Assign tdi5 = tdi4.insert(...)

```python
tdi5 = tdi4.insert(0, tdi4[0])
```

### Step 6: Assign msg = unknown.join(...)

```python
msg = '|'.join([re.escape(str(scalar)), re.escape(repr(scalar))])
```

### Step 7: scalar in tdi._engine

```python
scalar in tdi._engine
```

### Step 8: Call tdi._engine.get_loc()

```python
tdi._engine.get_loc(scalar)
```


## Complete Example

```python
# Setup
# Fixtures: scalar

# Workflow
tdi1 = pd.timedelta_range('42 days', freq='9h', periods=1234)
tdi2 = tdi1.insert(1, pd.NaT)
tdi3 = tdi1.insert(3, tdi1[0])
tdi4 = pd.timedelta_range('42 days', freq='ns', periods=2000000)
tdi5 = tdi4.insert(0, tdi4[0])
msg = '|'.join([re.escape(str(scalar)), re.escape(repr(scalar))])
for tdi in [tdi1, tdi2, tdi3, tdi4, tdi5]:
    with pytest.raises(TypeError, match=msg):
        scalar in tdi._engine
    with pytest.raises(KeyError, match=msg):
        tdi._engine.get_loc(scalar)
```

## Next Steps


---

*Source: test_engines.py:66 | Complexity: Advanced | Last updated: 2026-06-02*