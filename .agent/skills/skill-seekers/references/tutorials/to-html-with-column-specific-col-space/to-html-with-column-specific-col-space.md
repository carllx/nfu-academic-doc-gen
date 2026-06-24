# How To: To Html With Column Specific Col Space

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to html with column specific col space

## Prerequisites

**Required Modules:**
- `datetime`
- `io`
- `itertools`
- `re`
- `textwrap`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.io.formats.format`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).random(size=(3, 3)), columns=['a', 'b', 'c'])
```

**Verification:**
```python
assert 'min-width: 2em;">a</th>' in hdrs[1]
```

### Step 2: Assign result = df.to_html(...)

```python
result = df.to_html(col_space={'a': '2em', 'b': 23})
```

**Verification:**
```python
assert 'min-width: 23px;">b</th>' in hdrs[2]
```

### Step 3: Assign hdrs = value

```python
hdrs = [x for x in result.split('\n') if re.search('<th[>\\s]', x)]
```

**Verification:**
```python
assert '<th>c</th>' in hdrs[3]
```

### Step 4: Assign result = df.to_html(...)

```python
result = df.to_html(col_space=['1em', 2, 3])
```

**Verification:**
```python
assert 'min-width: 1em;">a</th>' in hdrs[1]
```

### Step 5: Assign hdrs = value

```python
hdrs = [x for x in result.split('\n') if re.search('<th[>\\s]', x)]
```

**Verification:**
```python
assert 'min-width: 2px;">b</th>' in hdrs[2]
```


## Complete Example

```python
# Workflow
df = DataFrame(np.random.default_rng(2).random(size=(3, 3)), columns=['a', 'b', 'c'])
result = df.to_html(col_space={'a': '2em', 'b': 23})
hdrs = [x for x in result.split('\n') if re.search('<th[>\\s]', x)]
assert 'min-width: 2em;">a</th>' in hdrs[1]
assert 'min-width: 23px;">b</th>' in hdrs[2]
assert '<th>c</th>' in hdrs[3]
result = df.to_html(col_space=['1em', 2, 3])
hdrs = [x for x in result.split('\n') if re.search('<th[>\\s]', x)]
assert 'min-width: 1em;">a</th>' in hdrs[1]
assert 'min-width: 2px;">b</th>' in hdrs[2]
assert 'min-width: 3px;">c</th>' in hdrs[3]
```

## Next Steps


---

*Source: test_to_html.py:112 | Complexity: Intermediate | Last updated: 2026-06-02*