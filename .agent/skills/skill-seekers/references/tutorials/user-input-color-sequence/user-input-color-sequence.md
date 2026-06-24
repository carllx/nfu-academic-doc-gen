# How To: User Input Color Sequence

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test user input color sequence

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `pandas`
- `pandas.plotting._matplotlib.style`
- `matplotlib`
- `matplotlib.pyplot`
- `matplotlib`
- `matplotlib.pyplot`
- `matplotlib`
- `matplotlib.colors`

**Setup Required:**
```python
# Fixtures: num_colors, expected
```

## Step-by-Step Guide

### Step 1: Assign color = value

```python
color = ['red', 'green', (0.1, 0.2, 0.3)]
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign result = get_standard_colors(...)

```python
result = get_standard_colors(color=color, num_colors=num_colors)
```

**Verification:**
```python
assert result == expected
```


## Complete Example

```python
# Setup
# Fixtures: num_colors, expected

# Workflow
color = ['red', 'green', (0.1, 0.2, 0.3)]
result = get_standard_colors(color=color, num_colors=num_colors)
assert result == expected
```

## Next Steps


---

*Source: test_style.py:94 | Complexity: Beginner | Last updated: 2026-06-02*