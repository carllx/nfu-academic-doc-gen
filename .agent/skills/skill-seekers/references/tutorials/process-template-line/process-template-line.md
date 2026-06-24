# How To: Process Template Line

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test process template line

## Prerequisites

**Required Modules:**
- `__future__`
- `contextlib`
- `io`
- `itertools`
- `logging`
- `os`
- `shutil`
- `sys`
- `tempfile`
- `pytest`
- `setuptools.command.egg_info`
- `setuptools.dist`
- `setuptools.tests.textwrap`
- `distutils`
- `distutils.errors`


## Step-by-Step Guide

### Step 1: Assign file_list = FileList(...)

```python
file_list = FileList()
```

**Verification:**
```python
assert file_list.files == wanted
```

### Step 2: Assign ml = make_local_path

```python
ml = make_local_path
```

### Step 3: Call self.make_files()

```python
self.make_files(['foo.tmp', 'ok', 'xo', 'four.txt', 'buildout.cfg', ml('.hg/last-message.txt'), ml('global/one.txt'), ml('global/two.txt'), ml('global/files.x'), ml('global/here.tmp'), ml('f/o/f.oo'), ml('dir/graft-one'), ml('dir/dir2/graft2'), ml('dir3/ok'), ml('dir3/sub/ok.txt')])
```

### Step 4: Assign MANIFEST_IN = DALS(...)

```python
MANIFEST_IN = DALS('        include ok\n        include xo\n        exclude xo\n        include foo.tmp\n        include buildout.cfg\n        global-include *.x\n        global-include *.txt\n        global-exclude *.tmp\n        recursive-include f *.oo\n        recursive-exclude global *.x\n        graft dir\n        prune dir3\n        ')
```

### Step 5: Assign wanted = value

```python
wanted = ['buildout.cfg', 'four.txt', 'ok', ml('.hg/last-message.txt'), ml('dir/graft-one'), ml('dir/dir2/graft2'), ml('f/o/f.oo'), ml('global/one.txt'), ml('global/two.txt')]
```

### Step 6: Call file_list.sort()

```python
file_list.sort()
```

**Verification:**
```python
assert file_list.files == wanted
```

### Step 7: Call file_list.process_template_line()

```python
file_list.process_template_line(line)
```


## Complete Example

```python
# Workflow
file_list = FileList()
ml = make_local_path
self.make_files(['foo.tmp', 'ok', 'xo', 'four.txt', 'buildout.cfg', ml('.hg/last-message.txt'), ml('global/one.txt'), ml('global/two.txt'), ml('global/files.x'), ml('global/here.tmp'), ml('f/o/f.oo'), ml('dir/graft-one'), ml('dir/dir2/graft2'), ml('dir3/ok'), ml('dir3/sub/ok.txt')])
MANIFEST_IN = DALS('        include ok\n        include xo\n        exclude xo\n        include foo.tmp\n        include buildout.cfg\n        global-include *.x\n        global-include *.txt\n        global-exclude *.tmp\n        recursive-include f *.oo\n        recursive-exclude global *.x\n        graft dir\n        prune dir3\n        ')
for line in MANIFEST_IN.split('\n'):
    if not line:
        continue
    file_list.process_template_line(line)
wanted = ['buildout.cfg', 'four.txt', 'ok', ml('.hg/last-message.txt'), ml('dir/graft-one'), ml('dir/dir2/graft2'), ml('f/o/f.oo'), ml('global/one.txt'), ml('global/two.txt')]
file_list.sort()
assert file_list.files == wanted
```

## Next Steps


---

*Source: test_manifest.py:373 | Complexity: Intermediate | Last updated: 2026-06-02*