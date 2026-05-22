# _shims/manufacturing/doctype/work_order/work_order.py
# Stub for top-level import in material_request.py.
# get_item_details is used when creating a Work Order from a Material Request —
# a flow that cannot happen without the Work Order doctype.


def get_item_details(item_code, project=None):
    """No-op stub: Work Orders are not part of this build."""
    return {}


# Additional lazy-import stubs (called inside functions, won't be reached
# in a build without manufacturing, but silences any accidental import)
class OverProductionError(Exception):
    pass


def get_disassembly_available_qty(source_stock_entry, current_name):
    return 0


def get_reserved_qty_for_production(item_code, warehouse):
    return 0


def make_stock_entry(work_order_id, purpose, qty=None):
    return {}
