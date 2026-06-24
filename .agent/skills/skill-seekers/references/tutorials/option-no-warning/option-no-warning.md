# How To: Option No Warning

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test option no warning

## Prerequisites

**Required Modules:**
- `datetime`
- `subprocess`
- `sys`
- `numpy`
- `pytest`
- `pandas._config.config`
- `pandas._libs.tslibs`
- `pandas`
- `pandas._testing`
- `pandas.plotting`
- `pandas.tseries.offsets`
- `pandas.plotting._matplotlib`


## Step-by-Step Guide

### Step 1: Call pytest.importorskip()

```python
pytest.importorskip('matplotlib.pyplot')
```

### Step 2: Assign ctx = cf.option_context(...)

```python
ctx = cf.option_context('plotting.matplotlib.register_converters', False)
```

### Step 3: Assign plt = pytest.importorskip(...)

```python
plt = pytest.importorskip('matplotlib.pyplot')
```

### Step 4: Assign s = Series(...)

```python
s = Series(range(12), index=date_range('2017', periods=12))
```

### Step 5: Assign unknown = plt.subplots(...)

```python
_, ax = plt.subplots()
```

### Step 6: Call register_matplotlib_converters()

```python
register_matplotlib_converters()
```

### Step 7: Call plt.close()

```python
plt.close()
```

### Step 8: Call ax.plot()

```python
ax.plot(s.index, s.values)
```

### Step 9: Call ax.plot()

```python
ax.plot(s.index, s.values)
```


## Complete Example

```python
# Workflow
pytest.importorskip('matplotlib.pyplot')
ctx = cf.option_context('plotting.matplotlib.register_converters', False)
plt = pytest.importorskip('matplotlib.pyplot')
s = Series(range(12), index=date_range('2017', periods=12))
_, ax = plt.subplots()
with ctx:
    ax.plot(s.index, s.values)
register_matplotlib_converters()
with ctx:
    ax.plot(s.index, s.values)
plt.close()
```

## Next Steps


---

*Source: test_converter.py:115 | Complexity: Advanced | Last updated: 2026-06-02*