import logging
import homeassistant.helpers.config_validation as cv
from homeassistant.core import HomeAssistant, ServiceCall

from .const import DOMAIN

LOGGER = logging.getLogger(__name__)

async def async_setup_services(hass: HomeAssistant) -> None:
    """Set up the services for the energymngt integration."""

    async def handle_get_hello_world2(call: ServiceCall) -> None:
        """Handle the get_hello_world2 service call."""
        # For testing purposes, just return a static value
        #entry_id = call.data['entry_id']
        #api: EnergyMngtAPI = hass.data[DOMAIN][entry_id]
        #result = api.get_hello_world2()
        hass.states.set("energymngt.hello_world2", "Hello World 2")


    mySchema = cv.make_entity_service_schema({'entry_id': cv.string})
    LOGGER.info("mySchema: %s", mySchema)

    hass.services.async_register(
        DOMAIN,
        'get_hello_world2',
        handle_get_hello_world2,
        schema=mySchema
    )

    async def handle_test_service(call: ServiceCall) -> None:
        """Handle the test_service call."""
        message = call.data.get("message", "This is a test message")
        LOGGER.info(f"Test service called with message: {message}")
        hass.states.set('energymngt.test_service', message)

    hass.services.async_register(DOMAIN, "test_service", handle_test_service, mySchema)