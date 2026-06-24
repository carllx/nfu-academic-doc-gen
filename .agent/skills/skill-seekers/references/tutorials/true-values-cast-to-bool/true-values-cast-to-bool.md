# How To: True Values Cast To Bool

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test true values cast to bool

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `collections`
- `io`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`

**Setup Required:**
```python
# Fixtures: all_parsers
```

## Step-by-Step Guide

### Step 1: Assign text = 'a,b\nyes,xxx\nno,yyy\n1,zzz\n0,aaa\n    '

```python
text = 'a,b\nyes,xxx\nno,yyy\n1,zzz\n0,aaa\n    '
```

### Step 2: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 3: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(text), true_values=['yes'], false_values=['no'], dtype={'a': 'boolean'})
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': [True, False, True, False], 'b': ['xxx', 'yyy', 'zzz', 'aaa']})
```

### Step 5: Assign unknown = unknown.astype(...)

```python
expected['a'] = expected['a'].astype('boolean')
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers

# Workflow
text = 'a,b\nyes,xxx\nno,yyy\n1,zzz\n0,aaa\n    '
parser = all_parsers
result = parser.read_csv(StringIO(text), true_values=['yes'], false_values=['no'], dtype={'a': 'boolean'})
expected = DataFrame({'a': [True, False, True, False], 'b': ['xxx', 'yyy', 'zzz', 'aaa']})
expected['a'] = expected['a'].astype('boolean')
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_dtypes_basic.py:281 | Complexity: Intermediate | Last updated: 2026-06-02*