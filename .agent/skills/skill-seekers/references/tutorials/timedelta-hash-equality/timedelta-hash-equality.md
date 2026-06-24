# How To: Timedelta Hash Equality

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test timedelta hash equality

## Prerequisites

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


## Step-by-Step Guide

### Step 1: Assign v = Timedelta(...)

```python
v = Timedelta(1, 'D')
```

**Verification:**
```python
assert hash(v) == hash(td)
```

### Step 2: Assign td = timedelta(...)

```python
td = timedelta(days=1)
```

**Verification:**
```python
assert d[v] == 2
```

### Step 3: Assign d = value

```python
d = {td: 2}
```

**Verification:**
```python
assert all((hash(td) == hash(td.to_pytimedelta()) for td in tds))
```

### Step 4: Assign tds = value

```python
tds = [Timedelta(seconds=1) + Timedelta(days=n) for n in range(20)]
```

**Verification:**
```python
assert hash(ns_td) != hash(ns_td.to_pytimedelta())
```

### Step 5: Assign ns_td = Timedelta(...)

```python
ns_td = Timedelta(1, 'ns')
```

**Verification:**
```python
assert hash(ns_td) != hash(ns_td.to_pytimedelta())
```


## Complete Example

```python
# Workflow
v = Timedelta(1, 'D')
td = timedelta(days=1)
assert hash(v) == hash(td)
d = {td: 2}
assert d[v] == 2
tds = [Timedelta(seconds=1) + Timedelta(days=n) for n in range(20)]
assert all((hash(td) == hash(td.to_pytimedelta()) for td in tds))
ns_td = Timedelta(1, 'ns')
assert hash(ns_td) != hash(ns_td.to_pytimedelta())
```

## Next Steps


---

*Source: test_timedelta.py:538 | Complexity: Intermediate | Last updated: 2026-06-02*