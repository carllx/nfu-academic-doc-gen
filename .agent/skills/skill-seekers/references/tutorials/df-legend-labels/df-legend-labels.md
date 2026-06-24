# How To: Df Legend Labels

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test df legend labels

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas.tests.plotting.common`
- `pandas.util.version`
- `matplotlib.collections`
- `matplotlib.lines`

**Setup Required:**
```python
# Fixtures: kind
```

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

### Step 5: Assign df4 = DataFrame(...)

```python
df4 = DataFrame(np.random.default_rng(2).random((3, 3)), columns=['j', 'k', 'l'])
```

### Step 6: Assign ax = df.plot(...)

```python
ax = df.plot(kind=kind, legend=True)
```

### Step 7: Call _check_legend_labels()

```python
_check_legend_labels(ax, labels=df.columns)
```

### Step 8: Assign ax = df2.plot(...)

```python
ax = df2.plot(kind=kind, legend=False, ax=ax)
```

### Step 9: Call _check_legend_labels()

```python
_check_legend_labels(ax, labels=df.columns)
```

### Step 10: Assign ax = df3.plot(...)

```python
ax = df3.plot(kind=kind, legend=True, ax=ax)
```

### Step 11: Call _check_legend_labels()

```python
_check_legend_labels(ax, labels=df.columns.union(df3.columns))
```

### Step 12: Assign ax = df4.plot(...)

```python
ax = df4.plot(kind=kind, legend='reverse', ax=ax)
```

### Step 13: Assign expected = value

```python
expected = list(df.columns.union(df3.columns)) + list(reversed(df4.columns))
```

### Step 14: Call _check_legend_labels()

```python
_check_legend_labels(ax, labels=expected)
```


## Complete Example

```python
# Setup
# Fixtures: kind

# Workflow
pytest.importorskip('scipy')
df = DataFrame(np.random.default_rng(2).random((3, 3)), columns=['a', 'b', 'c'])
df2 = DataFrame(np.random.default_rng(2).random((3, 3)), columns=['d', 'e', 'f'])
df3 = DataFrame(np.random.default_rng(2).random((3, 3)), columns=['g', 'h', 'i'])
df4 = DataFrame(np.random.default_rng(2).random((3, 3)), columns=['j', 'k', 'l'])
ax = df.plot(kind=kind, legend=True)
_check_legend_labels(ax, labels=df.columns)
ax = df2.plot(kind=kind, legend=False, ax=ax)
_check_legend_labels(ax, labels=df.columns)
ax = df3.plot(kind=kind, legend=True, ax=ax)
_check_legend_labels(ax, labels=df.columns.union(df3.columns))
ax = df4.plot(kind=kind, legend='reverse', ax=ax)
expected = list(df.columns.union(df3.columns)) + list(reversed(df4.columns))
_check_legend_labels(ax, labels=expected)
```

## Next Steps


---

*Source: test_frame_legend.py:63 | Complexity: Advanced | Last updated: 2026-06-02*