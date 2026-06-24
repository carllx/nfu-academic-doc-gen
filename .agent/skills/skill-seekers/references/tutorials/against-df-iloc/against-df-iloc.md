# How To: Against Df Iloc

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test against df iloc

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: start, stop, step
```

## Step-by-Step Guide

### Step 1: Assign n_rows = 30

```python
n_rows = 30
```

### Step 2: Assign data = value

```python
data = {'group': ['group 0'] * n_rows, 'value': list(range(n_rows))}
```

### Step 3: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame(data)
```

### Step 4: Assign grouped = df.groupby(...)

```python
grouped = df.groupby('group', as_index=False)
```

### Step 5: Assign result = value

```python
result = grouped._positional_selector[start:stop:step]
```

### Step 6: Assign expected = value

```python
expected = df.iloc[start:stop:step]
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: start, stop, step

# Workflow
n_rows = 30
data = {'group': ['group 0'] * n_rows, 'value': list(range(n_rows))}
df = pd.DataFrame(data)
grouped = df.groupby('group', as_index=False)
result = grouped._positional_selector[start:stop:step]
expected = df.iloc[start:stop:step]
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_indexing.py:222 | Complexity: Intermediate | Last updated: 2026-06-02*