from homeassistant.config_entries import ConfigEntry


async def async_setup_entry(hass, entry: ConfigEntry, async_add_devices):
    """Setup binary_sensors."""
    binary_sensors = []
