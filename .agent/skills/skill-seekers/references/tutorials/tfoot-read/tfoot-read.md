# How To: Tfoot Read

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: Make sure that read_html reads tfoot, containing td or th.
Ignores empty tfoot

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `collections.abc`
- `functools`
- `io`
- `os`
- `pathlib`
- `re`
- `threading`
- `urllib.error`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.io.common`
- `pandas.io.html`
- `pyarrow`
- `pandas.arrays`

**Setup Required:**
```python
# Fixtures: flavor_read_html
```

## Step-by-Step Guide

### Step 1: '\n        Make sure that read_html reads tfoot, containing td or th.\n        Ignores empty tfoot\n        '

```python
'\n        Make sure that read_html reads tfoot, containing td or th.\n        Ignores empty tfoot\n        '
```

### Step 2: Assign data_template = '<table>\n            <thead>\n                <tr>\n                    <th>A</th>\n                    <th>B</th>\n                </tr>\n            </thead>\n            <tbody>\n                <tr>\n                    <td>bodyA</td>\n                    <td>bodyB</td>\n                </tr>\n            </tbody>\n            <tfoot>\n                {footer}\n            </tfoot>\n        </table>'

```python
data_template = '<table>\n            <thead>\n                <tr>\n                    <th>A</th>\n                    <th>B</th>\n                </tr>\n            </thead>\n            <tbody>\n                <tr>\n                    <td>bodyA</td>\n                    <td>bodyB</td>\n                </tr>\n            </tbody>\n            <tfoot>\n                {footer}\n            </tfoot>\n        </table>'
```

### Step 3: Assign expected1 = DataFrame(...)

```python
expected1 = DataFrame(data=[['bodyA', 'bodyB']], columns=['A', 'B'])
```

### Step 4: Assign expected2 = DataFrame(...)

```python
expected2 = DataFrame(data=[['bodyA', 'bodyB'], ['footA', 'footB']], columns=['A', 'B'])
```

### Step 5: Assign data1 = data_template.format(...)

```python
data1 = data_template.format(footer='')
```

### Step 6: Assign data2 = data_template.format(...)

```python
data2 = data_template.format(footer='<tr><td>footA</td><th>footB</th></tr>')
```

### Step 7: Assign result1 = value

```python
result1 = flavor_read_html(StringIO(data1))[0]
```

### Step 8: Assign result2 = value

```python
result2 = flavor_read_html(StringIO(data2))[0]
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result1, expected1)
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result2, expected2)
```


## Complete Example

```python
# Setup
# Fixtures: flavor_read_html

# Workflow
'\n        Make sure that read_html reads tfoot, containing td or th.\n        Ignores empty tfoot\n        '
data_template = '<table>\n            <thead>\n                <tr>\n                    <th>A</th>\n                    <th>B</th>\n                </tr>\n            </thead>\n            <tbody>\n                <tr>\n                    <td>bodyA</td>\n                    <td>bodyB</td>\n                </tr>\n            </tbody>\n            <tfoot>\n                {footer}\n            </tfoot>\n        </table>'
expected1 = DataFrame(data=[['bodyA', 'bodyB']], columns=['A', 'B'])
expected2 = DataFrame(data=[['bodyA', 'bodyB'], ['footA', 'footB']], columns=['A', 'B'])
data1 = data_template.format(footer='')
data2 = data_template.format(footer='<tr><td>footA</td><th>footB</th></tr>')
result1 = flavor_read_html(StringIO(data1))[0]
result2 = flavor_read_html(StringIO(data2))[0]
tm.assert_frame_equal(result1, expected1)
tm.assert_frame_equal(result2, expected2)
```

## Next Steps


---

*Source: test_html.py:674 | Complexity: Advanced | Last updated: 2026-06-02*