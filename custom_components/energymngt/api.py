"""API connector for Energy Management."""

import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant


LOGGER = logging.getLogger(__name__)

class EnergyMngtAPI:
    """An object to store Energy Management API date."""

    def __init__(
        self, hass: HomeAssistant, entry: ConfigEntry, rand_min: int, rand_sec: int
    ) -> None:
        """Initialize the Energy Management connector object."""
        self.next_update = f"13:{rand_min}:{rand_sec}"

        self._entry = entry

        self.hass = hass


    def get_hello_world(self) -> str:        
        return "Hello world"
