# _shims/manufacturing/doctype/bom/bom.py
# Stubs for top-level imports in stock_entry.py and stock_entry_type.py.
# BOM-based stock entry purposes (Manufacture, Material Consumption for Manufacture)
# will not exist in the UI, so these are unreachable in normal operation.


def add_additional_cost(stock_entry, work_order):
    """No-op stub."""
    pass


def get_op_cost_from_sub_assemblies(bom_no, company, currency, conversion_rate, qty=1):
    """No-op stub."""
    return 0


def get_secondary_items_from_sub_assemblies(bom_no, qty, is_stock_item=None):
    """No-op stub."""
    return []


def validate_bom_no(item, bom_no):
    """No-op stub."""
    pass


def get_bom_items_as_dict(
    bom, company, qty=1, fetch_exploded=1, fetch_scrap_items=0,
    include_non_stock_items=False, fetch_qty_in_stock_uom=True
):
    """No-op stub."""
    return {}


def get_backflush_based_on(bom_no):
    """No-op stub."""
    return None


class BOMRecursionError(Exception):
    pass
