# How To: Any All

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test any all

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`

**Setup Required:**
```python
# Fixtures: values, exp_any, exp_all, exp_any_noskip, exp_all_noskip
```

## Step-by-Step Guide

### Step 1: Assign exp_any = value

```python
exp_any = pd.NA if exp_any is pd.NA else np.bool_(exp_any)
```

**Verification:**
```python
assert a.any() is exp_any
```

### Step 2: Assign exp_all = value

```python
exp_all = pd.NA if exp_all is pd.NA else np.bool_(exp_all)
```

**Verification:**
```python
assert a.all() is exp_all
```

### Step 3: Assign exp_any_noskip = value

```python
exp_any_noskip = pd.NA if exp_any_noskip is pd.NA else np.bool_(exp_any_noskip)
```

**Verification:**
```python
assert a.any(skipna=False) is exp_any_noskip
```

### Step 4: Assign exp_all_noskip = value

```python
exp_all_noskip = pd.NA if exp_all_noskip is pd.NA else np.bool_(exp_all_noskip)
```

**Verification:**
```python
assert a.all(skipna=False) is exp_all_noskip
```

### Step 5: Assign a = con(...)

```python
a = con(values, dtype='boolean')
```

**Verification:**
```python
assert np.any(a.any()) is exp_any
```


## Complete Example

```python
# Setup
# Fixtures: values, exp_any, exp_all, exp_any_noskip, exp_all_noskip

# Workflow
exp_any = pd.NA if exp_any is pd.NA else np.bool_(exp_any)
exp_all = pd.NA if exp_all is pd.NA else np.bool_(exp_all)
exp_any_noskip = pd.NA if exp_any_noskip is pd.NA else np.bool_(exp_any_noskip)
exp_all_noskip = pd.NA if exp_all_noskip is pd.NA else np.bool_(exp_all_noskip)
for con in [pd.array, pd.Series]:
    a = con(values, dtype='boolean')
    assert a.any() is exp_any
    assert a.all() is exp_all
    assert a.any(skipna=False) is exp_any_noskip
    assert a.all(skipna=False) is exp_all_noskip
    assert np.any(a.any()) is exp_any
    assert np.all(a.all()) is exp_all
```

## Next Steps


---

*Source: test_reduction.py:28 | Complexity: Intermediate | Last updated: 2026-06-02*