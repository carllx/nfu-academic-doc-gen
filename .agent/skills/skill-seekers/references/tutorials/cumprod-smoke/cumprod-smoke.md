# How To: Cumprod Smoke

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test cumprod smoke

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: datetime_frame
```

## Step-by-Step Guide

### Step 1: Assign unknown = value

```python
datetime_frame.iloc[5:10, 0] = np.nan
```

### Step 2: Assign unknown = value

```python
datetime_frame.iloc[10:15, 1] = np.nan
```

### Step 3: Assign unknown = value

```python
datetime_frame.iloc[15:, 2] = np.nan
```

### Step 4: Assign df = datetime_frame.fillna.astype(...)

```python
df = datetime_frame.fillna(0).astype(int)
```

### Step 5: Call df.cumprod()

```python
df.cumprod(0)
```

### Step 6: Call df.cumprod()

```python
df.cumprod(1)
```

### Step 7: Assign df = datetime_frame.fillna.astype(...)

```python
df = datetime_frame.fillna(0).astype(np.int32)
```

### Step 8: Call df.cumprod()

```python
df.cumprod(0)
```

### Step 9: Call df.cumprod()

```python
df.cumprod(1)
```


## Complete Example

```python
# Setup
# Fixtures: datetime_frame

# Workflow
datetime_frame.iloc[5:10, 0] = np.nan
datetime_frame.iloc[10:15, 1] = np.nan
datetime_frame.iloc[15:, 2] = np.nan
df = datetime_frame.fillna(0).astype(int)
df.cumprod(0)
df.cumprod(1)
df = datetime_frame.fillna(0).astype(np.int32)
df.cumprod(0)
df.cumprod(1)
```

## Next Steps


---

*Source: test_cumulative.py:34 | Complexity: Advanced | Last updated: 2026-06-02*