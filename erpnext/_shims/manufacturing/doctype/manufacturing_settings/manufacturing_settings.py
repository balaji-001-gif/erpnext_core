# _shims/manufacturing/doctype/manufacturing_settings/manufacturing_settings.py
# Stub for the server-side method called from stock_entry.js.
# Manufacturing Settings is not part of this build, so material consumption
# is always considered disabled.

import frappe


@frappe.whitelist()
def is_material_consumption_enabled():
    """No-op stub: Manufacturing Settings are not part of this build."""
    return 0
