# Porting a project from `fusepy` to `refuse`

The import logic has changed.

| Old (`fusepy`) | New (`refuse`) |
| --- | --- |
| `import fuse` | `from refuse import fuse` |
| `import fusell` | `from refuse import fusell` |
| `from fuse import something` | `from refuse.fuse import something` |
| `from fusell import something` | `from refuse.fusell import something` |
