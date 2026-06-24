# How To: Tab Complete Warning

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test tab complete warning

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `pandas._testing`
- `IPython.core.completer`

**Setup Required:**
```python
# Fixtures: ip
```

## Step-by-Step Guide

### Step 1: Call pytest.importorskip()

```python
pytest.importorskip('IPython', minversion='6.0.0')
```

### Step 2: Assign code = 'import pandas as pd; c = pd.Categorical([])'

```python
code = 'import pandas as pd; c = pd.Categorical([])'
```

### Step 3: Call ip.run_cell()

```python
ip.run_cell(code)
```

### Step 4: Call list()

```python
list(ip.Completer.completions('c.', 1))
```


## Complete Example

```python
# Setup
# Fixtures: ip

# Workflow
pytest.importorskip('IPython', minversion='6.0.0')
from IPython.core.completer import provisionalcompleter
code = 'import pandas as pd; c = pd.Categorical([])'
ip.run_cell(code)
with tm.assert_produces_warning(None, raise_on_extra_warnings=False):
    with provisionalcompleter('ignore'):
        list(ip.Completer.completions('c.', 1))
```

## Next Steps


---

*Source: test_warnings.py:7 | Complexity: Intermediate | Last updated: 2026-06-02*