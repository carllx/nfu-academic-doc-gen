# How To: Centered Axis Validation

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test centered axis validation

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
# Fixtures: step
```

## Step-by-Step Guide

### Step 1: Assign msg = "The 'axis' keyword in Series.rolling is deprecated"

```python
msg = "The 'axis' keyword in Series.rolling is deprecated"
```

### Step 2: Assign msg = 'No axis named 1 for object type Series'

```python
msg = 'No axis named 1 for object type Series'
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame(np.ones((10, 10)))
```

### Step 4: Assign msg = "The 'axis' keyword in DataFrame.rolling is deprecated"

```python
msg = "The 'axis' keyword in DataFrame.rolling is deprecated"
```

### Step 5: Assign msg = 'Support for axis=1 in DataFrame.rolling is deprecated'

```python
msg = 'Support for axis=1 in DataFrame.rolling is deprecated'
```

### Step 6: Assign msg = 'No axis named 2 for object type DataFrame'

```python
msg = 'No axis named 2 for object type DataFrame'
```

### Step 7: Call Series.rolling.mean()

```python
Series(np.ones(10)).rolling(window=3, center=True, axis=0, step=step).mean()
```

### Step 8: Call Series.rolling.mean()

```python
Series(np.ones(10)).rolling(window=3, center=True, axis=1, step=step).mean()
```

### Step 9: Call df.rolling.mean()

```python
df.rolling(window=3, center=True, axis=0, step=step).mean()
```

### Step 10: Call df.rolling.mean()

```python
df.rolling(window=3, center=True, axis=1, step=step).mean()
```

### Step 11: Call df.rolling.mean()

```python
df.rolling(window=3, center=True, axis=2, step=step).mean()
```


## Complete Example

```python
# Setup
# Fixtures: step

# Workflow
msg = "The 'axis' keyword in Series.rolling is deprecated"
with tm.assert_produces_warning(FutureWarning, match=msg):
    Series(np.ones(10)).rolling(window=3, center=True, axis=0, step=step).mean()
msg = 'No axis named 1 for object type Series'
with pytest.raises(ValueError, match=msg):
    Series(np.ones(10)).rolling(window=3, center=True, axis=1, step=step).mean()
df = DataFrame(np.ones((10, 10)))
msg = "The 'axis' keyword in DataFrame.rolling is deprecated"
with tm.assert_produces_warning(FutureWarning, match=msg):
    df.rolling(window=3, center=True, axis=0, step=step).mean()
msg = 'Support for axis=1 in DataFrame.rolling is deprecated'
with tm.assert_produces_warning(FutureWarning, match=msg):
    df.rolling(window=3, center=True, axis=1, step=step).mean()
msg = 'No axis named 2 for object type DataFrame'
with pytest.raises(ValueError, match=msg):
    df.rolling(window=3, center=True, axis=2, step=step).mean()
```

## Next Steps


---

*Source: test_api.py:355 | Complexity: Advanced | Last updated: 2026-06-02*