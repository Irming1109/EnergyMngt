from homeassistant.core import HomeAssistant

DOMAIN = "energymngt"

async def async_setup(hass: HomeAssistant, config: dict):
    """Set up integrationen fra konfigurationsfilen."""
    hass.states.async_set(f"{DOMAIN}.status", "running")
    return True
    
import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers import discovery

from .const import DOMAIN

# Initialiserer et logger for integrationen
_LOGGER = logging.getLogger(__name__)

# Denne funktion bliver kaldt, når integrationen er blevet konfigureret gennem UI (via Config Flow)
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Gør integrationen klar til brug baseret på de indstillinger brugeren har givet."""
    _LOGGER.info(f"Konfiguration af enermymngt entry: {entry.entry_id}")
    
    # Her kan du initialisere sensorer eller andre enheder, hvis nødvendigt
    # For eksempel kan du tilføje sensorer som en del af entry konfigurationen
    hass.data.setdefault(DOMAIN, {})[entry.entry_id] = entry.data
    await async_setup_entry(hass, entry, async_add_entities)

    # Returner True for at indikere at opsætningen er gennemført
    return True

# Rydder op, når integrationen fjernes
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Fjern eventuelle ressourcer, når entry fjernes."""
    _LOGGER.info(f"Fjerner entry: {entry.entry_id}")
    return True
