"""Nullable traversals shared by the run, message and runner paths.

`tool_resources` is nullable in the schema and the Redis stream payload is external
input, so both are validated once here instead of indexing them at each call site.
"""


def vector_store_file_ids(tool_resources):
    """Return the first vector store's file ids, or [] when any level is absent."""
    if not tool_resources:
        return []
    file_search = tool_resources.get("file_search")
    if not isinstance(file_search, dict):
        return []
    stores = file_search.get("vector_stores")
    if not isinstance(stores, list) or not stores:
        return []
    first = stores[0]
    if not isinstance(first, dict):
        return []
    file_ids = first.get("file_ids")
    return list(file_ids) if isinstance(file_ids, list) else []


def is_stream_entry(value):
    """True when a value looks like (stream_id, {field: value}) from xread."""
    return (
        isinstance(value, (list, tuple))
        and len(value) == 2
        and isinstance(value[0], str)
        and isinstance(value[1], dict)
    )
