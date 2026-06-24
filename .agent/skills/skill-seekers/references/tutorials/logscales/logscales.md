# How To: Logscales

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test logscales

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `gc`
- `itertools`
- `re`
- `string`
- `weakref`
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas.core.dtypes.api`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.plotting.common`
- `pandas.util.version`
- `pandas.io.formats.printing`
- `matplotlib.pyplot`
- `matplotlib.patches`
- `matplotlib.patches`
- `matplotlib.pyplot`
- `matplotlib.pyplot`
- `matplotlib.pyplot`
- `matplotlib.pyplot`
- `matplotlib.pyplot`
- `matplotlib`
- `matplotlib.pyplot`
- `matplotlib`
- `matplotlib.pyplot`
- `mpl_toolkits.axes_grid1`
- `mpl_toolkits.axes_grid1.inset_locator`

**Setup Required:**
```python
# Fixtures: input_log, expected_log
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': np.arange(100)}, index=np.arange(100))
```

**Verification:**
```python
assert ax.get_yscale() == expected_log
```

### Step 2: Assign ax = df.plot(...)

```python
ax = df.plot(logy=input_log)
```

**Verification:**
```python
assert ax.get_xscale() == expected_log
```

### Step 3: Call _check_ax_scales()

```python
_check_ax_scales(ax, yaxis=expected_log)
```

**Verification:**
```python
assert ax.get_xscale() == expected_log
```

### Step 4: Assign ax = df.plot(...)

```python
ax = df.plot(logx=input_log)
```

**Verification:**
```python
assert ax.get_yscale() == expected_log
```

### Step 5: Call _check_ax_scales()

```python
_check_ax_scales(ax, xaxis=expected_log)
```

**Verification:**
```python
assert ax.get_xscale() == expected_log
```

### Step 6: Assign ax = df.plot(...)

```python
ax = df.plot(loglog=input_log)
```

### Step 7: Call _check_ax_scales()

```python
_check_ax_scales(ax, xaxis=expected_log, yaxis=expected_log)
```

**Verification:**
```python
assert ax.get_xscale() == expected_log
```


## Complete Example

```python
# Setup
# Fixtures: input_log, expected_log

# Workflow
df = DataFrame({'a': np.arange(100)}, index=np.arange(100))
ax = df.plot(logy=input_log)
_check_ax_scales(ax, yaxis=expected_log)
assert ax.get_yscale() == expected_log
ax = df.plot(logx=input_log)
_check_ax_scales(ax, xaxis=expected_log)
assert ax.get_xscale() == expected_log
ax = df.plot(loglog=input_log)
_check_ax_scales(ax, xaxis=expected_log, yaxis=expected_log)
assert ax.get_xscale() == expected_log
assert ax.get_yscale() == expected_log
```

## Next Steps


---

*Source: test_frame.py:348 | Complexity: Intermediate | Last updated: 2026-06-02*