# How To: Parallel Coordinates With Sorted Labels

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: For #15908

## Prerequisites

**Required Modules:**
- `os`
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`
- `pandas.tests.plotting.common`
- `pandas.plotting`
- `pandas.plotting`
- `pandas.plotting`
- `pandas.plotting`
- `pandas.plotting`
- `pandas.plotting`
- `pandas.plotting`
- `pandas.plotting`
- `matplotlib`
- `pandas.plotting`
- `pandas.plotting`
- `pandas.plotting`
- `pandas.plotting`
- `pandas.plotting`
- `pandas.plotting`
- `matplotlib`
- `pandas.plotting`
- `pandas.plotting`
- `pandas.plotting._matplotlib.style`
- `pandas.plotting._matplotlib.style`
- `matplotlib`
- `pandas.plotting._matplotlib.style`
- `matplotlib.text`
- `matplotlib.text`
- `matplotlib.text`


## Step-by-Step Guide

### Step 1: 'For #15908'

```python
'For #15908'
```

**Verification:**
```python
assert prev[1] < nxt[1] and prev[0] < nxt[0]
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'feat': list(range(30)), 'class': [2 for _ in range(10)] + [3 for _ in range(10)] + [1 for _ in range(10)]})
```

### Step 3: Assign ax = parallel_coordinates(...)

```python
ax = parallel_coordinates(df, 'class', sort_labels=True)
```

### Step 4: Assign unknown = ax.get_legend_handles_labels(...)

```python
polylines, labels = ax.get_legend_handles_labels()
```

### Step 5: Assign color_label_tuples = zip(...)

```python
color_label_tuples = zip([polyline.get_color() for polyline in polylines], labels)
```

### Step 6: Assign ordered_color_label_tuples = sorted(...)

```python
ordered_color_label_tuples = sorted(color_label_tuples, key=lambda x: x[1])
```

### Step 7: Assign prev_next_tupels = zip(...)

```python
prev_next_tupels = zip(list(ordered_color_label_tuples[0:-1]), list(ordered_color_label_tuples[1:]))
```

**Verification:**
```python
assert prev[1] < nxt[1] and prev[0] < nxt[0]
```


## Complete Example

```python
# Workflow
'For #15908'
from pandas.plotting import parallel_coordinates
df = DataFrame({'feat': list(range(30)), 'class': [2 for _ in range(10)] + [3 for _ in range(10)] + [1 for _ in range(10)]})
ax = parallel_coordinates(df, 'class', sort_labels=True)
polylines, labels = ax.get_legend_handles_labels()
color_label_tuples = zip([polyline.get_color() for polyline in polylines], labels)
ordered_color_label_tuples = sorted(color_label_tuples, key=lambda x: x[1])
prev_next_tupels = zip(list(ordered_color_label_tuples[0:-1]), list(ordered_color_label_tuples[1:]))
for prev, nxt in prev_next_tupels:
    assert prev[1] < nxt[1] and prev[0] < nxt[0]
```

## Next Steps


---

*Source: test_misc.py:335 | Complexity: Intermediate | Last updated: 2026-06-02*