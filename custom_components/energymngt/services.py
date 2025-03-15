import logging
from homeassistant.core import HomeAssistant, ServiceCall

_LOGGER = logging.getLogger(__name__)

async def async_setup_services(hass: HomeAssistant) -> None:
    """Set up the services for the energymngt integration."""

    async def handle_test_service(call: ServiceCall) -> None:
        """Handle the test_service call."""
        message = call.data.get("message", "This is a test message")
        _LOGGER.info(f"Test service called with message: {message}")
        hass.states.set('energymngt.test_service', message)

    hass.services.async_register("energymngt", "test_service", handle_test_service)