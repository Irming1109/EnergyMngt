from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.entity import EntityDescription
import random

from .const import DOMAIN

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities):
    """Opsæt sensoren baseret på UI-konfigurationen."""
    sensor_name = entry.data.get("sensor_name", "Min Sensor")  # Henter sensor-navnet fra entry
    async_add_entities([RandomNumberSensor(sensor_name)], True)

class RandomNumberSensor(SensorEntity):
    """En simpel sensor, der viser et tilfældigt tal."""

    def __init__(self, name):
        """Initialiser sensoren."""
        self._attr_name = name
        self._attr_unique_id = f"sensor_{name.lower().replace(' ', '_')}"
        self._state = None

    def update(self):
        """Opdater sensorens tilstand med et nyt tilfældigt tal."""
        self._state = random.randint(0, 100)

    @property
    def native_value(self):
        """Returnerer sensorens aktuelle værdi."""
        return self._state
