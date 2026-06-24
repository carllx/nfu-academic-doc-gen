# How To: Indexing Over Size Cutoff Period Index

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: mock, workflow, integration

## Overview

Workflow: test indexing over size cutoff period index

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `re`
- `dateutil.tz`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: monkeypatch
```

## Step-by-Step Guide

### Step 1: Call monkeypatch.setattr()

```python
monkeypatch.setattr(libindex, '_SIZE_CUTOFF', 1000)
```

**Verification:**
```python
assert idx._engine.over_size_threshold
```

### Step 2: Assign n = 1100

```python
n = 1100
```

**Verification:**
```python
assert timestamp in s.index
```

### Step 3: Assign idx = period_range(...)

```python
idx = period_range('1/1/2000', freq='min', periods=n)
```

**Verification:**
```python
assert len(s.loc[[timestamp]]) > 0
```

### Step 4: Assign s = Series(...)

```python
s = Series(np.random.default_rng(2).standard_normal(len(idx)), index=idx)
```

### Step 5: Assign pos = value

```python
pos = n - 1
```

### Step 6: Assign timestamp = value

```python
timestamp = idx[pos]
```

**Verification:**
```python
assert timestamp in s.index
```

### Step 7: s[timestamp]

```python
s[timestamp]
```

**Verification:**
```python
assert len(s.loc[[timestamp]]) > 0
```


## Complete Example

```python
# Setup
# Fixtures: monkeypatch

# Workflow
monkeypatch.setattr(libindex, '_SIZE_CUTOFF', 1000)
n = 1100
idx = period_range('1/1/2000', freq='min', periods=n)
assert idx._engine.over_size_threshold
s = Series(np.random.default_rng(2).standard_normal(len(idx)), index=idx)
pos = n - 1
timestamp = idx[pos]
assert timestamp in s.index
s[timestamp]
assert len(s.loc[[timestamp]]) > 0
```

## Next Steps


---

*Source: test_datetime.py:352 | Complexity: Intermediate | Last updated: 2026-06-02*