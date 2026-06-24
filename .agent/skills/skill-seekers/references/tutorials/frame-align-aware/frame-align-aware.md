# How To: Frame Align Aware

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test frame align aware

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx1 = date_range(...)

```python
idx1 = date_range('2001', periods=5, freq='h', tz='US/Eastern')
```

**Verification:**
```python
assert df1.index.tz == new1.index.tz
```

### Step 2: Assign idx2 = date_range(...)

```python
idx2 = date_range('2001', periods=5, freq='2h', tz='US/Eastern')
```

**Verification:**
```python
assert df2.index.tz == new2.index.tz
```

### Step 3: Assign df1 = DataFrame(...)

```python
df1 = DataFrame(np.random.default_rng(2).standard_normal((len(idx1), 3)), idx1)
```

**Verification:**
```python
assert new1.index.tz is timezone.utc
```

### Step 4: Assign df2 = DataFrame(...)

```python
df2 = DataFrame(np.random.default_rng(2).standard_normal((len(idx2), 3)), idx2)
```

**Verification:**
```python
assert new2.index.tz is timezone.utc
```

### Step 5: Assign unknown = df1.align(...)

```python
new1, new2 = df1.align(df2)
```

**Verification:**
```python
assert new1.index.tz is timezone.utc
```

### Step 6: Assign df1_central = df1.tz_convert(...)

```python
df1_central = df1.tz_convert('US/Central')
```

**Verification:**
```python
assert new2.index.tz is timezone.utc
```

### Step 7: Assign unknown = df1.align(...)

```python
new1, new2 = df1.align(df1_central)
```

**Verification:**
```python
assert new1.index.tz is timezone.utc
```

### Step 8: Assign unknown = df1.align(...)

```python
new1, new2 = df1.align(df1_central[0], axis=0)
```

**Verification:**
```python
assert new2.index.tz is timezone.utc
```

### Step 9: Call unknown.align()

```python
df1[0].align(df1_central, axis=0)
```

**Verification:**
```python
assert new1.index.tz is timezone.utc
```


## Complete Example

```python
# Workflow
idx1 = date_range('2001', periods=5, freq='h', tz='US/Eastern')
idx2 = date_range('2001', periods=5, freq='2h', tz='US/Eastern')
df1 = DataFrame(np.random.default_rng(2).standard_normal((len(idx1), 3)), idx1)
df2 = DataFrame(np.random.default_rng(2).standard_normal((len(idx2), 3)), idx2)
new1, new2 = df1.align(df2)
assert df1.index.tz == new1.index.tz
assert df2.index.tz == new2.index.tz
df1_central = df1.tz_convert('US/Central')
new1, new2 = df1.align(df1_central)
assert new1.index.tz is timezone.utc
assert new2.index.tz is timezone.utc
new1, new2 = df1.align(df1_central[0], axis=0)
assert new1.index.tz is timezone.utc
assert new2.index.tz is timezone.utc
df1[0].align(df1_central, axis=0)
assert new1.index.tz is timezone.utc
assert new2.index.tz is timezone.utc
```

## Next Steps


---

*Source: test_align.py:25 | Complexity: Advanced | Last updated: 2026-06-02*