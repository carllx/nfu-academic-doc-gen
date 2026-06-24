# How To: Td64 Mean

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test td64 mean

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `inspect`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: box
```

## Step-by-Step Guide

### Step 1: Assign m8values = np.array(...)

```python
m8values = np.array([0, 3, -2, -7, 1, 2, -1, 3, 5, -2, 4], 'm8[D]')
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign tdi = pd.TimedeltaIndex.as_unit(...)

```python
tdi = pd.TimedeltaIndex(m8values).as_unit('ns')
```

**Verification:**
```python
assert obj.mean(skipna=False) is pd.NaT
```

### Step 3: Assign tdarr = value

```python
tdarr = tdi._data
```

**Verification:**
```python
assert result2 == tdi[1:].mean()
```

### Step 4: Assign obj = box(...)

```python
obj = box(tdarr, copy=False)
```

**Verification:**
```python
assert result2.round('us') == (result * 11.0 / 10).round('us')
```

### Step 5: Assign result = obj.mean(...)

```python
result = obj.mean()
```

### Step 6: Assign expected = np.array.mean(...)

```python
expected = np.array(tdarr).mean()
```

**Verification:**
```python
assert result == expected
```

### Step 7: Assign unknown = value

```python
tdarr[0] = pd.NaT
```

**Verification:**
```python
assert obj.mean(skipna=False) is pd.NaT
```

### Step 8: Assign result2 = obj.mean(...)

```python
result2 = obj.mean(skipna=True)
```

**Verification:**
```python
assert result2 == tdi[1:].mean()
```


## Complete Example

```python
# Setup
# Fixtures: box

# Workflow
m8values = np.array([0, 3, -2, -7, 1, 2, -1, 3, 5, -2, 4], 'm8[D]')
tdi = pd.TimedeltaIndex(m8values).as_unit('ns')
tdarr = tdi._data
obj = box(tdarr, copy=False)
result = obj.mean()
expected = np.array(tdarr).mean()
assert result == expected
tdarr[0] = pd.NaT
assert obj.mean(skipna=False) is pd.NaT
result2 = obj.mean(skipna=True)
assert result2 == tdi[1:].mean()
assert result2.round('us') == (result * 11.0 / 10).round('us')
```

## Next Steps


---

*Source: test_stat_reductions.py:66 | Complexity: Advanced | Last updated: 2026-06-02*