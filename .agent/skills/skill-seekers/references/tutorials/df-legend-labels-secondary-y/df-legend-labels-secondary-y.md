# How To: Df Legend Labels Secondary Y

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test df legend labels secondary y

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

### Step 1: Call pytest.importorskip()

```python
pytest.importorskip('scipy')
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).random((3, 3)), columns=['a', 'b', 'c'])
```

### Step 3: Assign df2 = DataFrame(...)

```python
df2 = DataFrame(np.random.default_rng(2).random((3, 3)), columns=['d', 'e', 'f'])
```

### Step 4: Assign df3 = DataFrame(...)

```python
df3 = DataFrame(np.random.default_rng(2).random((3, 3)), columns=['g', 'h', 'i'])
```

### Step 5: Assign ax = df.plot(...)

```python
ax = df.plot(legend=True, secondary_y='b')
```

### Step 6: Call _check_legend_labels()

```python
_check_legend_labels(ax, labels=['a', 'b (right)', 'c'])
```

### Step 7: Assign ax = df2.plot(...)

```python
ax = df2.plot(legend=False, ax=ax)
```

### Step 8: Call _check_legend_labels()

```python
_check_legend_labels(ax, labels=['a', 'b (right)', 'c'])
```

### Step 9: Assign ax = df3.plot(...)

```python
ax = df3.plot(kind='bar', legend=True, secondary_y='h', ax=ax)
```

### Step 10: Call _check_legend_labels()

```python
_check_legend_labels(ax, labels=['a', 'b (right)', 'c', 'g', 'h (right)', 'i'])
```


## Complete Example

```python
# Workflow
pytest.importorskip('scipy')
df = DataFrame(np.random.default_rng(2).random((3, 3)), columns=['a', 'b', 'c'])
df2 = DataFrame(np.random.default_rng(2).random((3, 3)), columns=['d', 'e', 'f'])
df3 = DataFrame(np.random.default_rng(2).random((3, 3)), columns=['g', 'h', 'i'])
ax = df.plot(legend=True, secondary_y='b')
_check_legend_labels(ax, labels=['a', 'b (right)', 'c'])
ax = df2.plot(legend=False, ax=ax)
_check_legend_labels(ax, labels=['a', 'b (right)', 'c'])
ax = df3.plot(kind='bar', legend=True, secondary_y='h', ax=ax)
_check_legend_labels(ax, labels=['a', 'b (right)', 'c', 'g', 'h (right)', 'i'])
```

## Next Steps


---

*Source: test_frame_legend.py:89 | Complexity: Advanced | Last updated: 2026-06-02*