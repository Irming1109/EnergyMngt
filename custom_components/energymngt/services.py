import logging
import homeassistant.helpers.config_validation as cv
import voluptuous as vol

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, ServiceCall, SupportsResponse

from .api import EnergyMngtAPI
from .const import DOMAIN

LOGGER = logging.getLogger(__name__)

HELLO_SCHEMA = vol.Schema(
    {
        vol.Required("currency"): str,
    }
)

async def async_setup_services(hass: HomeAssistant) -> None:
    """Set up the services for the energymngt integration."""

    async def handle_get_hello_world2(call: ServiceCall) -> None:
        """Handle the get_hello_world2 service call."""

        currency = call.data.get("currency", "N/A")
        LOGGER.debug("called currency with %r", currency)

        api = hass.data[DOMAIN][ConfigEntry.entry_id]
        result = api.get_hello_world2()

        return {"result": result, "message": "Hello World 2"}  # Return a dictionary


    hass.services.async_register(
        domain=DOMAIN,
        service='get_hello_world2',
        service_func=handle_get_hello_world2,
        schema=HELLO_SCHEMA,
        supports_response=SupportsResponse.OPTIONAL,
    )

    mySchema = cv.make_entity_service_schema({'entry_id': cv.string})
    LOGGER.info("mySchema: %s", mySchema)

    async def handle_test_service(call: ServiceCall) -> None:
        """Handle the test_service call."""
        message = call.data.get("message", "This is a test message")
        LOGGER.info(f"Test service called with message: {message}")
        hass.states.set('energymngt.test_service', message)

    hass.services.async_register(DOMAIN, "test_service", handle_test_service, mySchema)