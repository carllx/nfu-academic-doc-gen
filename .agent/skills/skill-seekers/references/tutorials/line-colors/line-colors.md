# How To: Line Colors

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test line colors

## Prerequisites

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.plotting.common`
- `pandas.util.version`
- `matplotlib.collections`
- `matplotlib`
- `matplotlib.collections`
- `matplotlib`
- `matplotlib.collections`
- `cycler`


## Step-by-Step Guide

### Step 1: Assign custom_colors = 'rgcby'

```python
custom_colors = 'rgcby'
```

**Verification:**
```python
assert l1.get_color() == l2.get_color()
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((5, 5)))
```

### Step 3: Assign ax = df.plot(...)

```python
ax = df.plot(color=custom_colors)
```

### Step 4: Call _check_colors()

```python
_check_colors(ax.get_lines(), linecolors=custom_colors)
```

### Step 5: Call plt.close()

```python
plt.close('all')
```

### Step 6: Assign ax2 = df.plot(...)

```python
ax2 = df.plot(color=custom_colors)
```

### Step 7: Assign lines2 = ax2.get_lines(...)

```python
lines2 = ax2.get_lines()
```

**Verification:**
```python
assert l1.get_color() == l2.get_color()
```


## Complete Example

```python
# Workflow
custom_colors = 'rgcby'
df = DataFrame(np.random.default_rng(2).standard_normal((5, 5)))
ax = df.plot(color=custom_colors)
_check_colors(ax.get_lines(), linecolors=custom_colors)
plt.close('all')
ax2 = df.plot(color=custom_colors)
lines2 = ax2.get_lines()
for l1, l2 in zip(ax.get_lines(), lines2):
    assert l1.get_color() == l2.get_color()
```

## Next Steps


---

*Source: test_frame_color.py:252 | Complexity: Intermediate | Last updated: 2026-06-02*