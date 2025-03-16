import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, ServiceCall

import voluptuous as vol

from .services import async_setup_services
from .api import EnergyMngtAPI
from .const import DOMAIN, PLATFORMS

# Initialize a logger for the integration
LOGGER = logging.getLogger(__name__)

# This function is called when the integration is configured through the UI (via Config Flow)
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:

    LOGGER.info("Setting up entry for %s", DOMAIN)
    hass.data.setdefault(DOMAIN, {})

    api = EnergyMngtAPI(hass, entry)
    LOGGER.debug("entry.entry_id %s", entry.entry_id)
    hass.data[DOMAIN][entry.entry_id] = api
    hass.data[DOMAIN]["Kasper"] = "Claus"

    valll = hass.data[DOMAIN]["Kasper"]
    LOGGER.info("valll %s", valll)

    await async_setup_services(hass)

    # Forward config entry setup to the sensor platform
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    return True

# Clean up when the integration is removed
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
 
    LOGGER.info("Removing entry for %s", DOMAIN)
    unload_ok = await hass.config_entries.async_forward_entry_unload(entry, PLATFORMS)
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)
        return True
    return False

async def async_setup(hass: HomeAssistant, config: dict):
    LOGGER.info("Setting up %s", DOMAIN)

    #async def handle_test_service(call: ServiceCall):
        # Set a state with a static message for testing purposes
    #    LOGGER.info("Test service called")
    #    hass.states.set("energymngt.test_service", "This is a test message")

    #hass.services.async_register(DOMAIN, 'test_service', handle_test_service, schema=vol.Schema({}))

    #async def handle_get_hello_world2(call: ServiceCall):
        # For testing purposes, just return a static value
        #entry_id = call.data['entry_id']
        #api: EnergyMngtAPI = hass.data[DOMAIN][entry_id]
        #result = api.get_hello_world2()
    #    hass.states.set("energymngt.hello_world2", "Hello World 2")

    #hass.services.async_register(DOMAIN, 'get_hello_world2', handle_get_hello_world2, schema=cv.make_entity_service_schema({
    #    'entry_id': cv.string,
    #}))




    return True