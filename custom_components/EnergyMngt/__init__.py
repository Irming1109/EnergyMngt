from homeassistant.core import HomeAssistant

DOMAIN = "energymngt"

async def async_setup(hass: HomeAssistant, config: dict):
    """Set up integrationen fra konfigurationsfilen."""
    hass.states.async_set(f"{DOMAIN}.status", "running")
    return True
