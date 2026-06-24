# How To: Tab Complete Ipython6 Warning

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: workflow, integration

## Overview

Workflow: test tab complete ipython6 warning

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `textwrap`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.indexes.datetimes`
- `IPython.core.completer`

**Setup Required:**
```python
# Fixtures: ip
```

## Step-by-Step Guide

### Step 1: Assign code = dedent(...)

```python
code = dedent('    import numpy as np\n    from pandas import Series, date_range\n    data = np.arange(10, dtype=np.float64)\n    index = date_range("2020-01-01", periods=len(data))\n    s = Series(data, index=index)\n    rs = s.resample("D")\n    ')
```

### Step 2: Call ip.run_cell()

```python
ip.run_cell(code)
```

### Step 3: Call list()

```python
list(ip.Completer.completions('rs.', 1))
```


## Complete Example

```python
# Setup
# Fixtures: ip

# Workflow
from IPython.core.completer import provisionalcompleter
code = dedent('    import numpy as np\n    from pandas import Series, date_range\n    data = np.arange(10, dtype=np.float64)\n    index = date_range("2020-01-01", periods=len(data))\n    s = Series(data, index=index)\n    rs = s.resample("D")\n    ')
ip.run_cell(code)
with tm.assert_produces_warning(None, raise_on_extra_warnings=False):
    with provisionalcompleter('ignore'):
        list(ip.Completer.completions('rs.', 1))
```

## Next Steps


---

*Source: test_resampler_grouper.py:28 | Complexity: Beginner | Last updated: 2026-06-02*