# How To: Legend False

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test legend false

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

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1, 1], 'b': [2, 3]})
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign df2 = DataFrame(...)

```python
df2 = DataFrame({'d': [2.5, 2.5]})
```

### Step 3: Assign ax = df.plot(...)

```python
ax = df.plot(legend=True, color={'a': 'blue', 'b': 'green'}, secondary_y='b')
```

### Step 4: Call df2.plot()

```python
df2.plot(legend=True, color={'d': 'red'}, ax=ax)
```

### Step 5: Assign legend = ax.get_legend(...)

```python
legend = ax.get_legend()
```

### Step 6: Assign result = value

```python
result = [handle.get_color() for handle in handles]
```

### Step 7: Assign expected = value

```python
expected = ['blue', 'green', 'red']
```

**Verification:**
```python
assert result == expected
```

### Step 8: Assign handles = value

```python
handles = legend.legendHandles
```

### Step 9: Assign handles = value

```python
handles = legend.legend_handles
```


## Complete Example

```python
# Workflow
df = DataFrame({'a': [1, 1], 'b': [2, 3]})
df2 = DataFrame({'d': [2.5, 2.5]})
ax = df.plot(legend=True, color={'a': 'blue', 'b': 'green'}, secondary_y='b')
df2.plot(legend=True, color={'d': 'red'}, ax=ax)
legend = ax.get_legend()
if Version(mpl.__version__) < Version('3.7'):
    handles = legend.legendHandles
else:
    handles = legend.legend_handles
result = [handle.get_color() for handle in handles]
expected = ['blue', 'green', 'red']
assert result == expected
```

## Next Steps


---

*Source: test_frame_legend.py:46 | Complexity: Advanced | Last updated: 2026-06-02*