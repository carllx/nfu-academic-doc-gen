# How To: Is Copy

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test is copy

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: date_range_frame
```

## Step-by-Step Guide

### Step 1: Assign df = date_range_frame.astype(...)

```python
df = date_range_frame.astype({'A': 'float'})
```

### Step 2: Assign N = 50

```python
N = 50
```

### Step 3: Assign unknown = value

```python
df.loc[df.index[15:30], 'A'] = np.nan
```

### Step 4: Assign dates = date_range(...)

```python
dates = date_range('1/1/1990', periods=N * 3, freq='25s')
```

### Step 5: Assign result = df.asof(...)

```python
result = df.asof(dates)
```

### Step 6: Assign unknown = 1

```python
result['C'] = 1
```


## Complete Example

```python
# Setup
# Fixtures: date_range_frame

# Workflow
df = date_range_frame.astype({'A': 'float'})
N = 50
df.loc[df.index[15:30], 'A'] = np.nan
dates = date_range('1/1/1990', periods=N * 3, freq='25s')
result = df.asof(dates)
with tm.assert_produces_warning(None):
    result['C'] = 1
```

## Next Steps


---

*Source: test_asof.py:166 | Complexity: Intermediate | Last updated: 2026-06-02*