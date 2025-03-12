import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.loader import async_get_integration

from .const import DOMAIN, PLATFORMS, STARTUP

# Initialiserer et logger for integrationen
LOGGER = logging.getLogger(__name__)

# Denne funktion bliver kaldt, når integrationen er blevet konfigureret gennem UI (via Config Flow)
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):

    hass.data.setdefault(DOMAIN, {})
    integration = await async_get_integration(hass, DOMAIN)
    LOGGER.info(STARTUP, integration.version)

    LOGGER.info(f"Konfiguration af enermymngt entry: {entry.entry_id}")
    
    # Her kan du initialisere sensorer eller andre enheder, hvis nødvendigt
    # For eksempel kan du tilføje sensorer som en del af entry konfigurationen
    hass.data.setdefault(DOMAIN, {})[entry.entry_id] = entry.data
    await async_setup_entry(hass, entry, async_add_entities)

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    # Returner True for at indikere at opsætningen er gennemført
    return True

# Rydder op, når integrationen fjernes
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Fjern eventuelle ressourcer, når entry fjernes."""
    LOGGER.info(f"Fjerner entry: {entry.entry_id}")
    return True


async def async_setup(hass: HomeAssistant, config: dict):
    """Set up integrationen fra konfigurationsfilen."""
    hass.states.async_set(f"{DOMAIN}.status", "running5")
    return True