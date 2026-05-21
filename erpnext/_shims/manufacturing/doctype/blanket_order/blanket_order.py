# _shims/manufacturing/doctype/blanket_order/blanket_order.py
# Stub — replaces top-level import in sales_order.py and purchase_order.py.
# validate_against_blanket_order is called only when a BlanketOrder link is set.
# Since the doctype doesn't exist in this build, the field will be absent and
# this function will never receive a populated blanket_order value.

import frappe


def validate_against_blanket_order(doc, is_child=False):
    """No-op stub: Blanket Orders are not part of this build."""
    pass
