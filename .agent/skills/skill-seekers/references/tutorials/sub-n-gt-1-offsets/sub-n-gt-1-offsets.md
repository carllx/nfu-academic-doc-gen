# How To: Sub N Gt 1 Offsets

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test sub n gt 1 offsets

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs.tslibs.period`
- `pandas`

**Setup Required:**
```python
# Fixtures: offset, kwd_name, n, normalize
```

## Step-by-Step Guide

### Step 1: Assign kwds = value

```python
kwds = {kwd_name: 3} if kwd_name is not None else {}
```

**Verification:**
```python
assert p2 - p1 == expected
```

### Step 2: Assign p1_d = '19910905'

```python
p1_d = '19910905'
```

### Step 3: Assign p2_d = '19920406'

```python
p2_d = '19920406'
```

### Step 4: Assign p1 = Period(...)

```python
p1 = Period(p1_d, freq=offset(n, normalize, **kwds))
```

### Step 5: Assign p2 = Period(...)

```python
p2 = Period(p2_d, freq=offset(n, normalize, **kwds))
```

### Step 6: Assign expected = value

```python
expected = Period(p2_d, freq=p2.freq.base) - Period(p1_d, freq=p1.freq.base)
```

**Verification:**
```python
assert p2 - p1 == expected
```


## Complete Example

```python
# Setup
# Fixtures: offset, kwd_name, n, normalize

# Workflow
kwds = {kwd_name: 3} if kwd_name is not None else {}
p1_d = '19910905'
p2_d = '19920406'
p1 = Period(p1_d, freq=offset(n, normalize, **kwds))
p2 = Period(p2_d, freq=offset(n, normalize, **kwds))
expected = Period(p2_d, freq=p2.freq.base) - Period(p1_d, freq=p1.freq.base)
assert p2 - p1 == expected
```

## Next Steps


---

*Source: test_arithmetic.py:107 | Complexity: Intermediate | Last updated: 2026-06-02*