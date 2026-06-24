# How To: Agg Apply

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test agg apply

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: raw
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'A': range(5), 'B': range(0, 10, 2)})
```

### Step 2: Assign r = df.rolling(...)

```python
r = df.rolling(window=3)
```

### Step 3: Assign a_sum = unknown.sum(...)

```python
a_sum = r['A'].sum()
```

### Step 4: Assign rcustom = unknown.apply(...)

```python
rcustom = r['B'].apply(lambda x: np.std(x, ddof=1), raw=raw)
```

### Step 5: Assign expected = concat(...)

```python
expected = concat([a_sum, rcustom], axis=1)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected, check_like=True)
```

### Step 7: Assign result = r.agg(...)

```python
result = r.agg({'A': np.sum, 'B': lambda x: np.std(x, ddof=1)})
```


## Complete Example

```python
# Setup
# Fixtures: raw

# Workflow
df = DataFrame({'A': range(5), 'B': range(0, 10, 2)})
r = df.rolling(window=3)
a_sum = r['A'].sum()
with tm.assert_produces_warning(FutureWarning, match='using Rolling.[sum|std]'):
    result = r.agg({'A': np.sum, 'B': lambda x: np.std(x, ddof=1)})
rcustom = r['B'].apply(lambda x: np.std(x, ddof=1), raw=raw)
expected = concat([a_sum, rcustom], axis=1)
tm.assert_frame_equal(result, expected, check_like=True)
```

## Next Steps


---

*Source: test_api.py:143 | Complexity: Intermediate | Last updated: 2026-06-02*