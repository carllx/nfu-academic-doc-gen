# How To: Errors

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test errors

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign s = Series(...)

```python
s = Series([1, 2, 3], index=[Timestamp('20130101'), Timestamp('20130103'), Timestamp('20130102')])
```

**Verification:**
```python
assert not s.index.is_monotonic_increasing
```

### Step 2: Assign N = 10

```python
N = 10
```

### Step 3: Assign rng = date_range(...)

```python
rng = date_range('1/1/1990', periods=N, freq='53s')
```

### Step 4: Assign s = Series(...)

```python
s = Series(np.random.default_rng(2).standard_normal(N), index=rng)
```

### Step 5: Call s.asof()

```python
s.asof(s.index[0])
```

### Step 6: Call s.asof()

```python
s.asof(s.index[0], subset='foo')
```


## Complete Example

```python
# Workflow
s = Series([1, 2, 3], index=[Timestamp('20130101'), Timestamp('20130103'), Timestamp('20130102')])
assert not s.index.is_monotonic_increasing
with pytest.raises(ValueError, match='requires a sorted index'):
    s.asof(s.index[0])
N = 10
rng = date_range('1/1/1990', periods=N, freq='53s')
s = Series(np.random.default_rng(2).standard_normal(N), index=rng)
with pytest.raises(ValueError, match='not valid for Series'):
    s.asof(s.index[0], subset='foo')
```

## Next Steps


---

*Source: test_asof.py:166 | Complexity: Intermediate | Last updated: 2026-06-02*