# erpnext_core — Fork Changes from ERPNext v16

## What was removed

| Module | Directory | Reason |
|---|---|---|
| Manufacturing | `erpnext/manufacturing/` | Not in scope |
| Quality Management | `erpnext/quality_management/` | Not in scope |
| Subcontracting | `erpnext/subcontracting/` | Depends on manufacturing |
| CRM | `erpnext/crm/` | Not in scope |
| Projects | `erpnext/projects/` | Not in scope |
| Support | `erpnext/support/` | Not in scope |
| Telephony | `erpnext/telephony/` | Not in scope |
| EDI | `erpnext/edi/` | Not in scope |
| Bulk Transaction | `erpnext/bulk_transaction/` | Not in scope |
| Maintenance | `erpnext/maintenance/` | Not in scope |

## What was added

### `erpnext/_shims/`
Stub package that satisfies top-level Python imports in core files that
referenced dropped modules. **Never add real logic here.** These are
no-ops that exist solely to prevent `ImportError` at startup.

| Shim | Replaces | Used by |
|---|---|---|
| `_shims/manufacturing/doctype/blanket_order/blanket_order.py` | `validate_against_blanket_order` | `sales_order.py`, `purchase_order.py` |
| `_shims/manufacturing/doctype/production_plan/production_plan.py` | `get_items_for_material_requests`, `get_sales_orders` | `sales_order.py` |
| `_shims/manufacturing/doctype/work_order/work_order.py` | `get_item_details` | `material_request.py` |
| `_shims/manufacturing/doctype/bom/bom.py` | `add_additional_cost`, `validate_bom_no`, `get_bom_items_as_dict`, etc. | `stock_entry.py`, `stock_entry_type.py` |
| `_shims/subcontracting/doctype/subcontracting_bom/subcontracting_bom.py` | `get_subcontracting_boms_for_finished_goods` | `purchase_order.py`, `material_request.py` |
| `_shims/projects/doctype/timesheet/timesheet.py` | `get_projectwise_timesheet_data` | `sales_invoice.py` |

## Source files patched

These are the **only ERPNext source files modified** (beyond deletion).
Each patch is a one-line import redirect or a `return` guard on a lazy import.

| File | Change |
|---|---|
| `selling/doctype/sales_order/sales_order.py` | Top-level imports → `_shims`; lazy subcontracting import guarded with `return` |
| `buying/doctype/purchase_order/purchase_order.py` | Top-level imports → `_shims`; lazy subcontracting import guarded with `return` |
| `stock/doctype/stock_entry/stock_entry.py` | Top-level BOM imports → `_shims` (sed replaced all occurrences including lazy) |
| `stock/doctype/stock_entry_type/stock_entry_type.py` | Top-level BOM import → `_shims` |
| `stock/doctype/material_request/material_request.py` | Top-level work_order + subcontracting_bom imports → `_shims` |
| `stock/doctype/bin/bin.py` | Lazy manufacturing imports → `_shims` |
| `accounts/doctype/sales_invoice/sales_invoice.py` | Top-level timesheet import → `_shims` |
| `selling/doctype/quotation/quotation.py` | 3 lazy CRM imports guarded with `return` |
| `selling/doctype/customer/customer.py` | Lazy CRM import guarded with `return` |
| `controllers/selling_controller.py` | Lazy CRM import guarded with `return` |
| `controllers/subcontracting_inward_controller.py` | Lazy subcontracting import guarded with `return` |
| `setup/install.py` | CRM Campaign custom field creation stubbed; Manufacturing role profile removed |
| `domains/manufacturing.py` | Deleted |
| `hooks.py` | 34 scheduler/doc_event lines for dropped modules commented out; app identity updated |
| `modules.txt` | Stripped to kept modules only |
| `patches.txt` | 22 patches for dropped modules commented out |
| `patches/v11_0/make_job_card.py` | Entire execute() replaced with no-op |

## DocType JSON patches

12 DocType JSON files had `Link` fields pointing at dropped doctypes.
These fields were converted from `Link` → `Data` (options removed).
Data is preserved in existing records; the field just loses its lookup button.

Fields affected: `bom_no`, `work_order`, `blanket_order`, `production_plan`,
`job_card`, `subcontracting_order`, `subcontracting_inward_order`,
`quality_inspection_template`, `default_bom` across stock, buying, selling, accounts doctypes.

## Known limitations

1. **Test suite**: Many test files import from dropped modules. Tests touching
   manufacturing, subcontracting, or CRM flows will fail. Do not run
   `bench run-tests` without filtering: `bench run-tests --module accounts`.

2. **Stock Entry — Manufacture purpose**: The "Manufacture" and
   "Material Consumption for Manufacture" stock entry purposes still exist
   as Select options in `StockEntryType`. They will not crash (shims cover the
   imports), but no BOM-driven item population will occur. Remove these
   purposes from the StockEntryType fixtures if you want a clean UI.

3. **Subcontracting fields in Buying Settings**: `backflush_raw_materials_of_subcontract_based_on`
   and `auto_create_subcontracting_order` remain as inert UI fields.
   They reference no dropped doctypes and cause no errors.

4. **ERPNext upstream patches**: When pulling upstream security/bugfix patches,
   always check if the patch touches any of the 11 files listed above.
   Re-apply the `_shims` redirect if a patch modifies an import block.

## Applying upstream ERPNext v16 patches

```bash
# Add upstream remote
git remote add upstream https://github.com/frappe/erpnext.git

# Fetch v16 branch
git fetch upstream version-16

# Cherry-pick a specific fix
git cherry-pick <commit-sha>

# After cherry-pick, verify no new dropped-module imports crept in
grep -rn "from erpnext\.manufacturing\|from erpnext\.crm\|from erpnext\.projects\|from erpnext\.subcontracting" \
  erpnext/ --include="*.py" \
  | grep -v "_shims\|test_\|/tests/\|patches/\|# \[REMOVED\]\|return  #"
```

## Installation

```bash
bench get-app erpnext_core https://github.com/yourorg/erpnext_core
bench --site yoursite.local install-app erpnext_core
bench migrate
```
