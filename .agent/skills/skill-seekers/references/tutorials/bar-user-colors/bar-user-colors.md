# How To: Bar User Colors

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: mock, workflow, integration

## Overview

Workflow: test bar user colors

## Prerequisites

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.plotting.common`
- `pandas.util.version`
- `matplotlib.collections`
- `matplotlib`
- `matplotlib.collections`
- `matplotlib`
- `matplotlib.collections`
- `cycler`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'A': range(4), 'B': range(1, 5), 'color': ['red', 'blue', 'blue', 'red']})
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign ax = df.plot.bar(...)

```python
ax = df.plot.bar(y='A', color=df['color'])
```

### Step 3: Assign result = value

```python
result = [p.get_facecolor() for p in ax.patches]
```

### Step 4: Assign expected = value

```python
expected = [(1.0, 0.0, 0.0, 1.0), (0.0, 0.0, 1.0, 1.0), (0.0, 0.0, 1.0, 1.0), (1.0, 0.0, 0.0, 1.0)]
```

**Verification:**
```python
assert result == expected
```


## Complete Example

```python
# Workflow
df = DataFrame({'A': range(4), 'B': range(1, 5), 'color': ['red', 'blue', 'blue', 'red']})
ax = df.plot.bar(y='A', color=df['color'])
result = [p.get_facecolor() for p in ax.patches]
expected = [(1.0, 0.0, 0.0, 1.0), (0.0, 0.0, 1.0, 1.0), (0.0, 0.0, 1.0, 1.0), (1.0, 0.0, 0.0, 1.0)]
assert result == expected
```

## Next Steps


---

*Source: test_frame_color.py:129 | Complexity: Intermediate | Last updated: 2026-06-02*