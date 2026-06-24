# How To: Dist Fetch Build Egg

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: Check multiple calls to `Distribution.fetch_build_egg` work as expected.

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `os`
- `re`
- `urllib.parse`
- `urllib.request`
- `pytest`
- `setuptools`
- `setuptools.dist`
- `fixtures`
- `test_find_packages`
- `textwrap`
- `distutils.errors`

**Setup Required:**
```python
# Fixtures: tmpdir, setuptools_wheel
```

## Step-by-Step Guide

### Step 1: '\n    Check multiple calls to `Distribution.fetch_build_egg` work as expected.\n    '

```python
'\n    Check multiple calls to `Distribution.fetch_build_egg` work as expected.\n    '
```

**Verification:**
```python
assert [dist.name for dist in resolved_dists if dist] == reqs
```

### Step 2: Assign index = tmpdir.mkdir(...)

```python
index = tmpdir.mkdir('index')
```

### Step 3: Assign index_url = urllib.parse.urljoin(...)

```python
index_url = urllib.parse.urljoin('file://', urllib.request.pathname2url(str(index)))
```

### Step 4: Call sdist_with_index()

```python
sdist_with_index('barbazquux', '3.2.0')
```

### Step 5: Call sdist_with_index()

```python
sdist_with_index('barbazquux-runner', '2.11.1')
```

### Step 6: Assign reqs = unknown.split(...)

```python
reqs = '\n    barbazquux-runner\n    barbazquux\n    '.split()
```

**Verification:**
```python
assert [dist.name for dist in resolved_dists if dist] == reqs
```

### Step 7: Assign dist_dir = index.mkdir(...)

```python
dist_dir = index.mkdir(distname)
```

### Step 8: Assign dist_sdist = value

```python
dist_sdist = f'{distname}-{version}.tar.gz'
```

### Step 9: Call make_trivial_sdist()

```python
make_trivial_sdist(str(dist_dir.join(dist_sdist)), distname, version, setuptools_wheel)
```

### Step 10: Call fp.write()

```python
fp.write(DALS('\n            [easy_install]\n            index_url = {index_url}\n            ').format(index_url=index_url))
```

### Step 11: Assign dist = Distribution(...)

```python
dist = Distribution()
```

### Step 12: Call dist.parse_config_files()

```python
dist.parse_config_files()
```

### Step 13: Assign resolved_dists = value

```python
resolved_dists = [dist.fetch_build_egg(r) for r in reqs]
```

### Step 14: Call fp.write()

```python
fp.write(DALS('\n                <!DOCTYPE html><html><body>\n                <a href="{dist_sdist}" rel="internal">{dist_sdist}</a><br/>\n                </body></html>\n                ').format(dist_sdist=dist_sdist))
```


## Complete Example

```python
# Setup
# Fixtures: tmpdir, setuptools_wheel

# Workflow
'\n    Check multiple calls to `Distribution.fetch_build_egg` work as expected.\n    '
index = tmpdir.mkdir('index')
index_url = urllib.parse.urljoin('file://', urllib.request.pathname2url(str(index)))

def sdist_with_index(distname, version):
    dist_dir = index.mkdir(distname)
    dist_sdist = f'{distname}-{version}.tar.gz'
    make_trivial_sdist(str(dist_dir.join(dist_sdist)), distname, version, setuptools_wheel)
    with dist_dir.join('index.html').open('w') as fp:
        fp.write(DALS('\n                <!DOCTYPE html><html><body>\n                <a href="{dist_sdist}" rel="internal">{dist_sdist}</a><br/>\n                </body></html>\n                ').format(dist_sdist=dist_sdist))
sdist_with_index('barbazquux', '3.2.0')
sdist_with_index('barbazquux-runner', '2.11.1')
with tmpdir.join('setup.cfg').open('w') as fp:
    fp.write(DALS('\n            [easy_install]\n            index_url = {index_url}\n            ').format(index_url=index_url))
reqs = '\n    barbazquux-runner\n    barbazquux\n    '.split()
with tmpdir.as_cwd():
    dist = Distribution()
    dist.parse_config_files()
    resolved_dists = [dist.fetch_build_egg(r) for r in reqs]
assert [dist.name for dist in resolved_dists if dist] == reqs
```

## Next Steps


---

*Source: test_dist.py:18 | Complexity: Advanced | Last updated: 2026-06-02*