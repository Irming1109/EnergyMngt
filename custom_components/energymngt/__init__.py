import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers import config_validation as cv
from homeassistant.core import HomeAssistant, ServiceCall
# from homeassistant.loader import async_get_integration

from .api import EnergyMngtAPI
from .const import DOMAIN, PLATFORMS

# Initialiserer et logger for integrationen
LOGGER = logging.getLogger(__name__)

# Denne funktion bliver kaldt, når integrationen er blevet konfigureret gennem UI (via Config Flow)
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
  
    LOGGER.info("Opsætning af entry for %s", DOMAIN)
    hass.data.setdefault(DOMAIN, {})

    api = EnergyMngtAPI(hass, entry)
    hass.data[DOMAIN][entry.entry_id] = api

    # Forward config entry setup to the sensor platform
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    #hass.async_create_task(
    #    hass.config_entries.async_forward_entry_setup(entry, "sensor")
    #)

    return True

# Rydder op, når integrationen fjernes
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
 
    LOGGER.info("Fjerner entry for %s", DOMAIN)
    unload_ok = await hass.config_entries.async_forward_entry_unload(entry, PLATFORMS)
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)
        return True
    return False


async def async_setup(hass: HomeAssistant, config: dict):
    LOGGER.info("Opsætning af %s", DOMAIN)

    async def handle_get_hello_world2(call: ServiceCall):
        api: EnergyMngtAPI = hass.data[DOMAIN][entry.entry_id]
        result = api.get_hello_world2()
        hass.states.set('energymngt.hello_world2', result)

    hass.services.async_register(DOMAIN, 'get_hello_world2', handle_get_hello_world2, schema=cv.make_entity_service_schema({
        'entry_id': cv.string,
    }))
    
    return True