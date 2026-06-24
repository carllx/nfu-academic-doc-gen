# How To: Floordiv Numeric

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test floordiv numeric

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `sys`
- `hypothesis`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas._libs.tslibs`
- `pandas._libs.tslibs.dtypes`
- `pandas.errors`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: td
```

## Step-by-Step Guide

### Step 1: Assign res = value

```python
res = td // 2
```

**Verification:**
```python
assert td // np.nan is NaT
```

### Step 2: Assign res = value

```python
res = td // 2.0
```

**Verification:**
```python
assert res._value == td._value // 2
```

### Step 3: Assign res = value

```python
res = td // np.array(2)
```

**Verification:**
```python
assert res._creso == td._creso
```

### Step 4: Assign res = value

```python
res = td // np.array(2.0)
```

**Verification:**
```python
assert res._value == td._value // 2
```


## Complete Example

```python
# Setup
# Fixtures: td

# Workflow
assert td // np.nan is NaT
res = td // 2
assert res._value == td._value // 2
assert res._creso == td._creso
res = td // 2.0
assert res._value == td._value // 2
assert res._creso == td._creso
assert td // np.array(np.nan) is NaT
res = td // np.array(2)
assert res._value == td._value // 2
assert res._creso == td._creso
res = td // np.array(2.0)
assert res._value == td._value // 2
assert res._creso == td._creso
```

## Next Steps


---

*Source: test_timedelta.py:163 | Complexity: Intermediate | Last updated: 2026-06-02*