# How To: Keep Default Na

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test keep default na

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

### Step 1: Assign html_data = '<table>\n                        <thead>\n                            <tr>\n                            <th>a</th>\n                            </tr>\n                        </thead>\n                        <tbody>\n                            <tr>\n                            <td> N/A</td>\n                            </tr>\n                            <tr>\n                            <td> NA</td>\n                            </tr>\n                        </tbody>\n                    </table>'

```python
html_data = '<table>\n                        <thead>\n                            <tr>\n                            <th>a</th>\n                            </tr>\n                        </thead>\n                        <tbody>\n                            <tr>\n                            <td> N/A</td>\n                            </tr>\n                            <tr>\n                            <td> NA</td>\n                            </tr>\n                        </tbody>\n                    </table>'
```

### Step 2: Assign expected_df = DataFrame(...)

```python
expected_df = DataFrame({'a': ['N/A', 'NA']})
```

### Step 3: Assign html_df = value

```python
html_df = flavor_read_html(StringIO(html_data), keep_default_na=False)[0]
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(expected_df, html_df)
```

### Step 5: Assign expected_df = DataFrame(...)

```python
expected_df = DataFrame({'a': [np.nan, np.nan]})
```

### Step 6: Assign html_df = value

```python
html_df = flavor_read_html(StringIO(html_data), keep_default_na=True)[0]
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(expected_df, html_df)
```


## Complete Example

```python
# Setup
# Fixtures: flavor_read_html

# Workflow
html_data = '<table>\n                        <thead>\n                            <tr>\n                            <th>a</th>\n                            </tr>\n                        </thead>\n                        <tbody>\n                            <tr>\n                            <td> N/A</td>\n                            </tr>\n                            <tr>\n                            <td> NA</td>\n                            </tr>\n                        </tbody>\n                    </table>'
expected_df = DataFrame({'a': ['N/A', 'NA']})
html_df = flavor_read_html(StringIO(html_data), keep_default_na=False)[0]
tm.assert_frame_equal(expected_df, html_df)
expected_df = DataFrame({'a': [np.nan, np.nan]})
html_df = flavor_read_html(StringIO(html_data), keep_default_na=True)[0]
tm.assert_frame_equal(expected_df, html_df)
```

## Next Steps


---

*Source: test_html.py:1198 | Complexity: Intermediate | Last updated: 2026-06-02*