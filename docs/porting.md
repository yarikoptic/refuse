# Porting a project from `fusepy` to `refuse`

The import logic has changed.

| Old (`fusepy`) | New (`refuse`) |
| --- | --- |
| `import fuse` | `from refuse import high as fuse` |
| `import fusell` | `from refuse import low as fusell` |
| `from fuse import something` | `from refuse.high import something` |
| `from fusell import something` | `from refuse.low import something` |
