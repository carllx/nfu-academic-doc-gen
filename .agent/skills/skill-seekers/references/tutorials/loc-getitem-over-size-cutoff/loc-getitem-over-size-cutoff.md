# How To: Loc Getitem Over Size Cutoff

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: mock, workflow, integration

## Overview

Workflow: test loc getitem over size cutoff

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
assert timestamp in df.index
```

### Step 2: Assign dates = value

```python
dates = []
```

**Verification:**
```python
assert len(df.loc[[timestamp]]) > 0
```

### Step 3: Assign sec = timedelta(...)

```python
sec = timedelta(seconds=1)
```

### Step 4: Assign half_sec = timedelta(...)

```python
half_sec = timedelta(microseconds=500000)
```

### Step 5: Assign d = datetime(...)

```python
d = datetime(2011, 12, 5, 20, 30)
```

### Step 6: Assign n = 1100

```python
n = 1100
```

### Step 7: Assign duplicate_positions = np.random.default_rng.integers(...)

```python
duplicate_positions = np.random.default_rng(2).integers(0, len(dates) - 1, 20)
```

### Step 8: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((len(dates), 4)), index=dates, columns=list('ABCD'))
```

### Step 9: Assign pos = value

```python
pos = n * 3
```

### Step 10: Assign timestamp = value

```python
timestamp = df.index[pos]
```

**Verification:**
```python
assert timestamp in df.index
```

### Step 11: df.loc[timestamp]

```python
df.loc[timestamp]
```

**Verification:**
```python
assert len(df.loc[[timestamp]]) > 0
```

### Step 12: Call dates.append()

```python
dates.append(d)
```

### Step 13: Call dates.append()

```python
dates.append(d + sec)
```

### Step 14: Call dates.append()

```python
dates.append(d + sec + half_sec)
```

### Step 15: Call dates.append()

```python
dates.append(d + sec + sec + half_sec)
```

### Step 16: Assign unknown = value

```python
dates[p + 1] = dates[p]
```


## Complete Example

```python
# Setup
# Fixtures: monkeypatch

# Workflow
monkeypatch.setattr(libindex, '_SIZE_CUTOFF', 1000)
dates = []
sec = timedelta(seconds=1)
half_sec = timedelta(microseconds=500000)
d = datetime(2011, 12, 5, 20, 30)
n = 1100
for i in range(n):
    dates.append(d)
    dates.append(d + sec)
    dates.append(d + sec + half_sec)
    dates.append(d + sec + sec + half_sec)
    d += 3 * sec
duplicate_positions = np.random.default_rng(2).integers(0, len(dates) - 1, 20)
for p in duplicate_positions:
    dates[p + 1] = dates[p]
df = DataFrame(np.random.default_rng(2).standard_normal((len(dates), 4)), index=dates, columns=list('ABCD'))
pos = n * 3
timestamp = df.index[pos]
assert timestamp in df.index
df.loc[timestamp]
assert len(df.loc[[timestamp]]) > 0
```

## Next Steps


---

*Source: test_datetime.py:314 | Complexity: Advanced | Last updated: 2026-06-02*