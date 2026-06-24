# How To: Df Legend Labels Time Series No Mutate

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test df legend labels time series no mutate

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

**Verification:**
```python
assert df5.columns.tolist() == ['b', 'c']
```

### Step 2: Assign ind = date_range(...)

```python
ind = date_range('1/1/2014', periods=3)
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((3, 3)), columns=['a', 'b', 'c'], index=ind)
```

### Step 4: Assign df5 = df.set_index(...)

```python
df5 = df.set_index('a')
```

### Step 5: Assign ax = df5.plot(...)

```python
ax = df5.plot(y='b')
```

### Step 6: Call _check_legend_labels()

```python
_check_legend_labels(ax, labels=['b'])
```

### Step 7: Assign ax = df5.plot(...)

```python
ax = df5.plot(y='b', label='LABEL_b')
```

### Step 8: Call _check_legend_labels()

```python
_check_legend_labels(ax, labels=['LABEL_b'])
```

### Step 9: Call _check_text_labels()

```python
_check_text_labels(ax.xaxis.get_label(), 'a')
```

### Step 10: Assign ax = df5.plot(...)

```python
ax = df5.plot(y='c', label='LABEL_c', ax=ax)
```

### Step 11: Call _check_legend_labels()

```python
_check_legend_labels(ax, labels=['LABEL_b', 'LABEL_c'])
```

**Verification:**
```python
assert df5.columns.tolist() == ['b', 'c']
```


## Complete Example

```python
# Workflow
pytest.importorskip('scipy')
ind = date_range('1/1/2014', periods=3)
df = DataFrame(np.random.default_rng(2).standard_normal((3, 3)), columns=['a', 'b', 'c'], index=ind)
df5 = df.set_index('a')
ax = df5.plot(y='b')
_check_legend_labels(ax, labels=['b'])
ax = df5.plot(y='b', label='LABEL_b')
_check_legend_labels(ax, labels=['LABEL_b'])
_check_text_labels(ax.xaxis.get_label(), 'a')
ax = df5.plot(y='c', label='LABEL_c', ax=ax)
_check_legend_labels(ax, labels=['LABEL_b', 'LABEL_c'])
assert df5.columns.tolist() == ['b', 'c']
```

## Next Steps


---

*Source: test_frame_legend.py:159 | Complexity: Advanced | Last updated: 2026-06-02*