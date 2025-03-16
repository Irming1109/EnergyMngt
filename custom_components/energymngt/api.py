"""API connector for Energy Management."""

import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant


LOGGER = logging.getLogger(__name__)

class EnergyMngtAPI:
    def __init__(
        self, hass: HomeAssistant, entry: ConfigEntry
    ) -> None:
        """Initialize the Stromligning connector object."""

        self._entry = entry

        self.hass = hass

    def get_hello_world(self):
        return "Hello, World!"

    def get_hello_world2(self):
        return 67