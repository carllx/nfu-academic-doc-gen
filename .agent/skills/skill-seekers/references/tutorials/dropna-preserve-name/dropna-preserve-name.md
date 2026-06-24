# How To: Dropna Preserve Name

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dropna preserve name

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: datetime_series
```

## Step-by-Step Guide

### Step 1: Assign unknown = value

```python
datetime_series[:5] = np.nan
```

**Verification:**
```python
assert result.name == datetime_series.name
```

### Step 2: Assign result = datetime_series.dropna(...)

```python
result = datetime_series.dropna()
```

**Verification:**
```python
assert return_value is None
```

### Step 3: Assign name = value

```python
name = datetime_series.name
```

**Verification:**
```python
assert ts.name == name
```

### Step 4: Assign ts = datetime_series.copy(...)

```python
ts = datetime_series.copy()
```

### Step 5: Assign return_value = ts.dropna(...)

```python
return_value = ts.dropna(inplace=True)
```

**Verification:**
```python
assert return_value is None
```


## Complete Example

```python
# Setup
# Fixtures: datetime_series

# Workflow
datetime_series[:5] = np.nan
result = datetime_series.dropna()
assert result.name == datetime_series.name
name = datetime_series.name
ts = datetime_series.copy()
return_value = ts.dropna(inplace=True)
assert return_value is None
assert ts.name == name
```

## Next Steps


---

*Source: test_dropna.py:29 | Complexity: Intermediate | Last updated: 2026-06-02*