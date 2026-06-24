# How To: Df Legend Labels Time Series

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test df legend labels time series

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

### Step 2: Assign ind = date_range(...)

```python
ind = date_range('1/1/2014', periods=3)
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((3, 3)), columns=['a', 'b', 'c'], index=ind)
```

### Step 4: Assign df2 = DataFrame(...)

```python
df2 = DataFrame(np.random.default_rng(2).standard_normal((3, 3)), columns=['d', 'e', 'f'], index=ind)
```

### Step 5: Assign df3 = DataFrame(...)

```python
df3 = DataFrame(np.random.default_rng(2).standard_normal((3, 3)), columns=['g', 'h', 'i'], index=ind)
```

### Step 6: Assign ax = df.plot(...)

```python
ax = df.plot(legend=True, secondary_y='b')
```

### Step 7: Call _check_legend_labels()

```python
_check_legend_labels(ax, labels=['a', 'b (right)', 'c'])
```

### Step 8: Assign ax = df2.plot(...)

```python
ax = df2.plot(legend=False, ax=ax)
```

### Step 9: Call _check_legend_labels()

```python
_check_legend_labels(ax, labels=['a', 'b (right)', 'c'])
```

### Step 10: Assign ax = df3.plot(...)

```python
ax = df3.plot(legend=True, ax=ax)
```

### Step 11: Call _check_legend_labels()

```python
_check_legend_labels(ax, labels=['a', 'b (right)', 'c', 'g', 'h', 'i'])
```


## Complete Example

```python
# Workflow
pytest.importorskip('scipy')
ind = date_range('1/1/2014', periods=3)
df = DataFrame(np.random.default_rng(2).standard_normal((3, 3)), columns=['a', 'b', 'c'], index=ind)
df2 = DataFrame(np.random.default_rng(2).standard_normal((3, 3)), columns=['d', 'e', 'f'], index=ind)
df3 = DataFrame(np.random.default_rng(2).standard_normal((3, 3)), columns=['g', 'h', 'i'], index=ind)
ax = df.plot(legend=True, secondary_y='b')
_check_legend_labels(ax, labels=['a', 'b (right)', 'c'])
ax = df2.plot(legend=False, ax=ax)
_check_legend_labels(ax, labels=['a', 'b (right)', 'c'])
ax = df3.plot(legend=True, ax=ax)
_check_legend_labels(ax, labels=['a', 'b (right)', 'c', 'g', 'h', 'i'])
```

## Next Steps


---

*Source: test_frame_legend.py:106 | Complexity: Advanced | Last updated: 2026-06-02*