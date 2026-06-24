# How To: Usecols With Multi Byte Characters

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test usecols with multi byte characters

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `io`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: all_parsers, usecols
```

## Step-by-Step Guide

### Step 1: Assign data = 'あああ,いい,ううう,ええええ\n0.056674973,8,True,a\n2.613230982,2,False,b\n3.568935038,7,False,a'

```python
data = 'あああ,いい,ううう,ええええ\n0.056674973,8,True,a\n2.613230982,2,False,b\n3.568935038,7,False,a'
```

### Step 2: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 3: Assign exp_data = value

```python
exp_data = {'あああ': {0: 0.056674973, 1: 2.6132309819999997, 2: 3.5689350380000002}, 'いい': {0: 8, 1: 2, 2: 7}}
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame(exp_data)
```

### Step 5: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), usecols=usecols)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers, usecols

# Workflow
data = 'あああ,いい,ううう,ええええ\n0.056674973,8,True,a\n2.613230982,2,False,b\n3.568935038,7,False,a'
parser = all_parsers
exp_data = {'あああ': {0: 0.056674973, 1: 2.6132309819999997, 2: 3.5689350380000002}, 'いい': {0: 8, 1: 2, 2: 7}}
expected = DataFrame(exp_data)
result = parser.read_csv(StringIO(data), usecols=usecols)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_strings.py:78 | Complexity: Intermediate | Last updated: 2026-06-02*