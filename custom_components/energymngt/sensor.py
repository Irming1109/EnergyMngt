from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.entity import EntityDescription
import random

DOMAIN = "energymngt"

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Opsætning af sensoren."""
    async_add_entities([RandomNumberSensor()], True)

class RandomNumberSensor(SensorEntity):
    """En simpel sensor, der viser et tilfældigt tal."""

    def __init__(self):
        """Initialiser sensoren."""
        self._attr_name = "Tilfældig Sensor"
        self._attr_unique_id = "random_sensor_1"
        self._attr_native_unit_of_measurement = "værdi"
        self._state = None

    def update(self):
        """Opdater sensorens tilstand med et nyt tilfældigt tal."""
        self._state = random.randint(0, 100)

    @property
    def native_value(self):
        """Returnerer sensorens aktuelle værdi."""
        return self._state
