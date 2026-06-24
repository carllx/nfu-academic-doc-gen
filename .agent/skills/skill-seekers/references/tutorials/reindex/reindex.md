# How To: Reindex

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test reindex

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: datetime_series, string_series
```

## Step-by-Step Guide

### Step 1: Assign identity = string_series.reindex(...)

```python
identity = string_series.reindex(string_series.index)
```

**Verification:**
```python
assert tm.shares_memory(string_series.index, identity.index)
```

### Step 2: Assign subIndex = value

```python
subIndex = string_series.index[10:20]
```

**Verification:**
```python
assert identity.index.is_(string_series.index)
```

### Step 3: Assign subSeries = string_series.reindex(...)

```python
subSeries = string_series.reindex(subIndex)
```

**Verification:**
```python
assert identity.index.identical(string_series.index)
```

### Step 4: Assign subIndex2 = value

```python
subIndex2 = datetime_series.index[10:20]
```

**Verification:**
```python
assert val == string_series[idx]
```

### Step 5: Assign subTS = datetime_series.reindex(...)

```python
subTS = datetime_series.reindex(subIndex2)
```

**Verification:**
```python
assert val == datetime_series[idx]
```

### Step 6: Assign stuffSeries = datetime_series.reindex(...)

```python
stuffSeries = datetime_series.reindex(subIndex)
```

**Verification:**
```python
assert np.isnan(stuffSeries).all()
```

### Step 7: Assign nonContigIndex = value

```python
nonContigIndex = datetime_series.index[::2]
```

**Verification:**
```python
assert val == datetime_series[idx]
```

### Step 8: Assign subNonContig = datetime_series.reindex(...)

```python
subNonContig = datetime_series.reindex(nonContigIndex)
```

**Verification:**
```python
assert result is not datetime_series
```

### Step 9: Assign result = datetime_series.reindex(...)

```python
result = datetime_series.reindex()
```

**Verification:**
```python
assert result is not datetime_series
```


## Complete Example

```python
# Setup
# Fixtures: datetime_series, string_series

# Workflow
identity = string_series.reindex(string_series.index)
assert tm.shares_memory(string_series.index, identity.index)
assert identity.index.is_(string_series.index)
assert identity.index.identical(string_series.index)
subIndex = string_series.index[10:20]
subSeries = string_series.reindex(subIndex)
for idx, val in subSeries.items():
    assert val == string_series[idx]
subIndex2 = datetime_series.index[10:20]
subTS = datetime_series.reindex(subIndex2)
for idx, val in subTS.items():
    assert val == datetime_series[idx]
stuffSeries = datetime_series.reindex(subIndex)
assert np.isnan(stuffSeries).all()
nonContigIndex = datetime_series.index[::2]
subNonContig = datetime_series.reindex(nonContigIndex)
for idx, val in subNonContig.items():
    assert val == datetime_series[idx]
result = datetime_series.reindex()
assert result is not datetime_series
```

## Next Steps


---

*Source: test_reindex.py:25 | Complexity: Advanced | Last updated: 2026-06-02*