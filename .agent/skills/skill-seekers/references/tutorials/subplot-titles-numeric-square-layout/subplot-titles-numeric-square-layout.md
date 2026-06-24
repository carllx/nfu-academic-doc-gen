# How To: Subplot Titles Numeric Square Layout

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test subplot titles numeric square layout

## Prerequisites

- [ ] Setup code must be executed first

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

**Setup Required:**
```python
# Fixtures: iris
```

## Step-by-Step Guide

### Step 1: Assign df = iris.drop.head(...)

```python
df = iris.drop('Name', axis=1).head()
```

**Verification:**
```python
assert title_list == title[:3] + ['']
```

### Step 2: Assign title = list(...)

```python
title = list(df.columns)
```

### Step 3: Assign plot = df.drop.plot(...)

```python
plot = df.drop('SepalWidth', axis=1).plot(subplots=True, layout=(2, 2), title=title[:-1])
```

### Step 4: Assign title_list = value

```python
title_list = [ax.get_title() for sublist in plot for ax in sublist]
```

**Verification:**
```python
assert title_list == title[:3] + ['']
```


## Complete Example

```python
# Setup
# Fixtures: iris

# Workflow
df = iris.drop('Name', axis=1).head()
title = list(df.columns)
plot = df.drop('SepalWidth', axis=1).plot(subplots=True, layout=(2, 2), title=title[:-1])
title_list = [ax.get_title() for sublist in plot for ax in sublist]
assert title_list == title[:3] + ['']
```

## Next Steps


---

*Source: test_misc.py:448 | Complexity: Intermediate | Last updated: 2026-06-02*