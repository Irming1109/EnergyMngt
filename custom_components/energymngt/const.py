"""Const used in the integration."""

# Startup banner
STARTUP = "start info"

CONF_TEMPLATE = "extra_cost_template"

DEFAULT_TEMPLATE = "{{0.0|float(0)}}"
DOMAIN = "energymngt"

PLATFORMS = ["sensor", "binary_sensor"]

UPDATE_SIGNAL = f"{DOMAIN}_SIGNAL_UPDATE"