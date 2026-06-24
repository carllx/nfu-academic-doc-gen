# How To: Step

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test step

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: step
```

## Step-by-Step Guide

### Step 1: Assign data = value

```python
data = [['x', f'x{i}'] for i in range(5)]
```

### Step 2: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame(data, columns=['A', 'B'])
```

### Step 3: Assign grouped = df.groupby(...)

```python
grouped = df.groupby('A', as_index=False)
```

### Step 4: Assign result = value

```python
result = grouped._positional_selector[::step]
```

### Step 5: Assign data = value

```python
data = [['x', f'x{i}'] for i in range(0, 5, step)]
```

### Step 6: Assign index = value

```python
index = [0 + i for i in range(0, 5, step)]
```

### Step 7: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame(data, columns=['A', 'B'], index=index)
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: step

# Workflow
data = [['x', f'x{i}'] for i in range(5)]
data += [['y', f'y{i}'] for i in range(4)]
data += [['z', f'z{i}'] for i in range(3)]
df = pd.DataFrame(data, columns=['A', 'B'])
grouped = df.groupby('A', as_index=False)
result = grouped._positional_selector[::step]
data = [['x', f'x{i}'] for i in range(0, 5, step)]
data += [['y', f'y{i}'] for i in range(0, 4, step)]
data += [['z', f'z{i}'] for i in range(0, 3, step)]
index = [0 + i for i in range(0, 5, step)]
index += [5 + i for i in range(0, 4, step)]
index += [9 + i for i in range(0, 3, step)]
expected = pd.DataFrame(data, columns=['A', 'B'], index=index)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_indexing.py:250 | Complexity: Advanced | Last updated: 2026-06-02*