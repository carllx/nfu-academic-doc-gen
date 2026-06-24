# How To: Check Subprocess Call Non Matching Regex

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test check subprocess call non matching regex

## Prerequisites

**Required Modules:**
- `re`
- `sys`
- `joblib.testing`


## Step-by-Step Guide

### Step 1: Assign code = '42'

```python
code = '42'
```

### Step 2: Assign non_matching_pattern = '_no_way_this_matches_anything_'

```python
non_matching_pattern = '_no_way_this_matches_anything_'
```

### Step 3: Call excinfo.match()

```python
excinfo.match('Unexpected stdout.+{}'.format(non_matching_pattern))
```

### Step 4: Call check_subprocess_call()

```python
check_subprocess_call([sys.executable, '-c', code], stdout_regex=non_matching_pattern)
```


## Complete Example

```python
# Workflow
code = '42'
non_matching_pattern = '_no_way_this_matches_anything_'
with raises(ValueError) as excinfo:
    check_subprocess_call([sys.executable, '-c', code], stdout_regex=non_matching_pattern)
excinfo.match('Unexpected stdout.+{}'.format(non_matching_pattern))
```

## Next Steps


---

*Source: test_testing.py:22 | Complexity: Intermediate | Last updated: 2026-06-02*