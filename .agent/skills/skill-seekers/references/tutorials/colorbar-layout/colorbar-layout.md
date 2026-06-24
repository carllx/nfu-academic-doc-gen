# How To: Colorbar Layout

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test colorbar layout

## Prerequisites

**Required Modules:**
- `pytest`
- `pandas`
- `pandas.tests.plotting.common`


## Step-by-Step Guide

### Step 1: Assign fig = plt.figure(...)

```python
fig = plt.figure()
```

### Step 2: Assign axes = fig.subplot_mosaic(...)

```python
axes = fig.subplot_mosaic('\n            AB\n            CC\n            ')
```

### Step 3: Assign x = value

```python
x = [1, 2, 3]
```

### Step 4: Assign y = value

```python
y = [1, 2, 3]
```

### Step 5: Assign cs0 = unknown.scatter(...)

```python
cs0 = axes['A'].scatter(x, y)
```

### Step 6: Call unknown.scatter()

```python
axes['B'].scatter(x, y)
```

### Step 7: Call fig.colorbar()

```python
fig.colorbar(cs0, ax=[axes['A'], axes['B']], location='right')
```

### Step 8: Call DataFrame.plot()

```python
DataFrame(x).plot(ax=axes['C'])
```


## Complete Example

```python
# Workflow
fig = plt.figure()
axes = fig.subplot_mosaic('\n            AB\n            CC\n            ')
x = [1, 2, 3]
y = [1, 2, 3]
cs0 = axes['A'].scatter(x, y)
axes['B'].scatter(x, y)
fig.colorbar(cs0, ax=[axes['A'], axes['B']], location='right')
DataFrame(x).plot(ax=axes['C'])
```

## Next Steps


---

*Source: test_common.py:43 | Complexity: Advanced | Last updated: 2026-06-02*