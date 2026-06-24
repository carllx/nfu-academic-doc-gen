# How To: Cythonized Aggers

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test cythonized aggers

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.common`

**Setup Required:**
```python
# Fixtures: op_name
```

## Step-by-Step Guide

### Step 1: Assign data = value

```python
data = {'A': [0, 0, 0, 0, 1, 1, 1, 1, 1, 1.0, np.nan, np.nan], 'B': ['A', 'B'] * 6, 'C': np.random.default_rng(2).standard_normal(12)}
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(data)
```

### Step 3: Assign unknown = value

```python
df.loc[2:10:2, 'C'] = np.nan
```

### Step 4: Assign op = value

```python
op = lambda x: getattr(x, op_name)()
```

### Step 5: Assign grouped = df.drop.groupby(...)

```python
grouped = df.drop(['B'], axis=1).groupby('A')
```

### Step 6: Assign exp = value

```python
exp = {cat: op(group['C']) for cat, group in grouped}
```

### Step 7: Assign exp = DataFrame(...)

```python
exp = DataFrame({'C': exp})
```

### Step 8: Assign exp.index.name = 'A'

```python
exp.index.name = 'A'
```

### Step 9: Assign result = op(...)

```python
result = op(grouped)
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, exp)
```

### Step 11: Assign grouped = df.groupby(...)

```python
grouped = df.groupby(['A', 'B'])
```

### Step 12: Assign expd = value

```python
expd = {}
```

### Step 13: Assign exp = DataFrame.T.stack(...)

```python
exp = DataFrame(expd).T.stack(future_stack=True)
```

### Step 14: Assign exp.index.names = value

```python
exp.index.names = ['A', 'B']
```

### Step 15: Assign exp.name = 'C'

```python
exp.name = 'C'
```

### Step 16: Assign result = value

```python
result = op(grouped)['C']
```

### Step 17: Assign unknown = op(...)

```python
expd.setdefault(cat1, {})[cat2] = op(group['C'])
```

### Step 18: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, exp)
```


## Complete Example

```python
# Setup
# Fixtures: op_name

# Workflow
data = {'A': [0, 0, 0, 0, 1, 1, 1, 1, 1, 1.0, np.nan, np.nan], 'B': ['A', 'B'] * 6, 'C': np.random.default_rng(2).standard_normal(12)}
df = DataFrame(data)
df.loc[2:10:2, 'C'] = np.nan
op = lambda x: getattr(x, op_name)()
grouped = df.drop(['B'], axis=1).groupby('A')
exp = {cat: op(group['C']) for cat, group in grouped}
exp = DataFrame({'C': exp})
exp.index.name = 'A'
result = op(grouped)
tm.assert_frame_equal(result, exp)
grouped = df.groupby(['A', 'B'])
expd = {}
for (cat1, cat2), group in grouped:
    expd.setdefault(cat1, {})[cat2] = op(group['C'])
exp = DataFrame(expd).T.stack(future_stack=True)
exp.index.names = ['A', 'B']
exp.name = 'C'
result = op(grouped)['C']
if op_name in ['sum', 'prod']:
    tm.assert_series_equal(result, exp)
```

## Next Steps


---

*Source: test_cython.py:47 | Complexity: Advanced | Last updated: 2026-06-02*