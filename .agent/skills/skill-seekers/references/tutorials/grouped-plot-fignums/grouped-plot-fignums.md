# How To: Grouped Plot Fignums

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test grouped plot fignums

## Prerequisites

**Required Modules:**
- `__future__`
- `itertools`
- `string`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.tests.plotting.common`
- `pandas.util.version`
- `pandas.io.formats.printing`
- `matplotlib.pyplot`
- `matplotlib.pyplot`


## Step-by-Step Guide

### Step 1: Assign n = 10

```python
n = 10
```

**Verification:**
```python
assert len(mpl.pyplot.get_fignums()) == 2
```

### Step 2: Assign weight = Series(...)

```python
weight = Series(np.random.default_rng(2).normal(166, 20, size=n))
```

**Verification:**
```python
assert len(res) == 2
```

### Step 3: Assign height = Series(...)

```python
height = Series(np.random.default_rng(2).normal(60, 10, size=n))
```

**Verification:**
```python
assert len(mpl.pyplot.get_fignums()) == 1
```

### Step 4: Assign gender = np.random.default_rng.choice(...)

```python
gender = np.random.default_rng(2).choice(['male', 'female'], size=n)
```

**Verification:**
```python
assert len(res) == 2
```

### Step 5: Assign df = DataFrame(...)

```python
df = DataFrame({'height': height, 'weight': weight, 'gender': gender})
```

### Step 6: Assign gb = df.groupby(...)

```python
gb = df.groupby('gender')
```

### Step 7: Assign res = gb.plot(...)

```python
res = gb.plot()
```

**Verification:**
```python
assert len(mpl.pyplot.get_fignums()) == 2
```

### Step 8: Call plt.close()

```python
plt.close('all')
```

### Step 9: Assign res = gb.boxplot(...)

```python
res = gb.boxplot(return_type='axes')
```

**Verification:**
```python
assert len(mpl.pyplot.get_fignums()) == 1
```


## Complete Example

```python
# Workflow
n = 10
weight = Series(np.random.default_rng(2).normal(166, 20, size=n))
height = Series(np.random.default_rng(2).normal(60, 10, size=n))
gender = np.random.default_rng(2).choice(['male', 'female'], size=n)
df = DataFrame({'height': height, 'weight': weight, 'gender': gender})
gb = df.groupby('gender')
res = gb.plot()
assert len(mpl.pyplot.get_fignums()) == 2
assert len(res) == 2
plt.close('all')
res = gb.boxplot(return_type='axes')
assert len(mpl.pyplot.get_fignums()) == 1
assert len(res) == 2
```

## Next Steps


---

*Source: test_boxplot_method.py:473 | Complexity: Advanced | Last updated: 2026-06-02*