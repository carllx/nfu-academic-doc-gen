# How To: Legend Name

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test legend name

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas.tests.plotting.common`
- `pandas.util.version`
- `matplotlib.collections`
- `matplotlib.lines`


## Step-by-Step Guide

### Step 1: Assign multi = DataFrame(...)

```python
multi = DataFrame(np.random.default_rng(2).standard_normal((4, 4)), columns=[np.array(['a', 'a', 'b', 'b']), np.array(['x', 'y', 'x', 'y'])])
```

### Step 2: Assign multi.columns.names = value

```python
multi.columns.names = ['group', 'individual']
```

### Step 3: Assign ax = multi.plot(...)

```python
ax = multi.plot()
```

### Step 4: Assign leg_title = ax.legend_.get_title(...)

```python
leg_title = ax.legend_.get_title()
```

### Step 5: Call _check_text_labels()

```python
_check_text_labels(leg_title, 'group,individual')
```

### Step 6: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((5, 5)))
```

### Step 7: Assign ax = df.plot(...)

```python
ax = df.plot(legend=True, ax=ax)
```

### Step 8: Assign leg_title = ax.legend_.get_title(...)

```python
leg_title = ax.legend_.get_title()
```

### Step 9: Call _check_text_labels()

```python
_check_text_labels(leg_title, 'group,individual')
```

### Step 10: Assign df.columns.name = 'new'

```python
df.columns.name = 'new'
```

### Step 11: Assign ax = df.plot(...)

```python
ax = df.plot(legend=False, ax=ax)
```

### Step 12: Assign leg_title = ax.legend_.get_title(...)

```python
leg_title = ax.legend_.get_title()
```

### Step 13: Call _check_text_labels()

```python
_check_text_labels(leg_title, 'group,individual')
```

### Step 14: Assign ax = df.plot(...)

```python
ax = df.plot(legend=True, ax=ax)
```

### Step 15: Assign leg_title = ax.legend_.get_title(...)

```python
leg_title = ax.legend_.get_title()
```

### Step 16: Call _check_text_labels()

```python
_check_text_labels(leg_title, 'new')
```


## Complete Example

```python
# Workflow
multi = DataFrame(np.random.default_rng(2).standard_normal((4, 4)), columns=[np.array(['a', 'a', 'b', 'b']), np.array(['x', 'y', 'x', 'y'])])
multi.columns.names = ['group', 'individual']
ax = multi.plot()
leg_title = ax.legend_.get_title()
_check_text_labels(leg_title, 'group,individual')
df = DataFrame(np.random.default_rng(2).standard_normal((5, 5)))
ax = df.plot(legend=True, ax=ax)
leg_title = ax.legend_.get_title()
_check_text_labels(leg_title, 'group,individual')
df.columns.name = 'new'
ax = df.plot(legend=False, ax=ax)
leg_title = ax.legend_.get_title()
_check_text_labels(leg_title, 'group,individual')
ax = df.plot(legend=True, ax=ax)
leg_title = ax.legend_.get_title()
_check_text_labels(leg_title, 'new')
```

## Next Steps


---

*Source: test_frame_legend.py:203 | Complexity: Advanced | Last updated: 2026-06-02*