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
        LOGGER.info("handle_get_hello_world2")
        LOGGER.debug("hass.data[DOMAIN] %r", hass.data[DOMAIN])

        valll = hass.data[DOMAIN]["Kasper"]
        LOGGER.info("valll %s", valll)

        currency = call.data.get("currency", "N/A")
        LOGGER.info("info: get_hello_world2")
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

    async def handle_test_service(call: ServiceCall) -> None:
        """Handle the test_service call."""
        message = call.data.get("message", "This is a test message")
        LOGGER.info(f"Test service called with message: {message}")
        hass.states.set('energymngt.test_service', message)

    hass.services.async_register(domain=DOMAIN, service="test_service", service_func=handle_test_service, schema=HELLO_SCHEMA)