import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers import config_validation as cv
from homeassistant.core import HomeAssistant, ServiceCall

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
    LOGGER.info("Setting up %s", DOMAIN)

    async def handle_test_service(call: ServiceCall):
        # Set a state with a static message for testing purposes
        hass.states.set('energymngt.test_service', "This is a test message")

    hass.services.async_register(DOMAIN, 'test_service', handle_test_service, schema=vol.Schema({}))

    async def handle_get_hello_world2(call: ServiceCall):
        # For testing purposes, just return a static value
        #entry_id = call.data['entry_id']
        #api: EnergyMngtAPI = hass.data[DOMAIN][entry_id]
        #result = api.get_hello_world2()
        hass.states.set('energymngt.hello_world2', "Hello World 2")

    hass.services.async_register(DOMAIN, 'get_hello_world2', handle_get_hello_world2, schema=cv.make_entity_service_schema({
        'entry_id': cv.string,
    }))




    return True