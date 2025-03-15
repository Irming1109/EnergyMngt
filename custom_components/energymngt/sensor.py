import logging

import homeassistant.helpers.config_validation as cv
from homeassistant.components import sensor
from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
)

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_NAME, EntityCategory
from homeassistant.core import HomeAssistant
from homeassistant.helpers.dispatcher import async_dispatcher_connect
from homeassistant.helpers.template import Template
from homeassistant.util import slugify as util_slugify

from .api import EnergyMngtAPI
from .base import EnergyMngtSensorEntityDescription
from .const import CONF_TEMPLATE, DEFAULT_TEMPLATE, DOMAIN

LOGGER = logging.getLogger(__name__)

SENSORS = [
        EnergyMngtSensorEntityDescription(
        key="hello_world_str",
        entity_category=None,
        icon="mdi:flash",
        value_fn=lambda energymngt: energymngt.get_hello_world(),
    ),
]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities):

    sensor_name = "energymngtKasper"
    async_add_entities([RandomNumberSensor(sensor_name)], True)
    
    """Setup sensors."""
    sensors = []

    for sensor in SENSORS:
        entity = EnergyMngtSensor(sensor, hass, entry)
        LOGGER.debug(
            "Added sensor with entity_id '%s'",
            entity.entity_id,
        )
        sensors.append(entity)

    async_add_entities(sensors)


class EnergyMngtSensor(SensorEntity):
    """Representation of a EnergyMngt Sensor."""

    _attr_has_entity_name = True
    _attr_available = True

    def __init__(
        self,
        description: EnergyMngtSensorEntityDescription,
        hass: HomeAssistant,
        entry: ConfigEntry,
    ) -> None:
        """Initialize a EnergyMngt Sensor."""
        super().__init__()

        self.entity_description = description
        self._config = entry
        self._hass = hass
        self.api: EnergyMngtAPI = hass.data[DOMAIN][entry.entry_id]
        self._cost_template = entry.options.get(CONF_TEMPLATE)

        self._attr_unique_id = util_slugify(
            f"{self.entity_description.key}_{self._config.entry_id}"
        )
        self._attr_should_poll = True

        LOGGER.debug(f"CONF_NAME: {CONF_NAME}")
        LOGGER.debug(f"self._config.data.get(CONF_NAME): {self._config.data.get(CONF_NAME)}")

        self._attr_device_info = {
            "identifiers": {(DOMAIN, self._config.entry_id)},
            "name": self._config.data.get(CONF_NAME),
            "manufacturer": "Energy Management",
        }

        self._attr_native_unit_of_measurement = (
            self.entity_description.unit_of_measurement
        )

        async_dispatcher_connect(
            self._hass,
            util_slugify(self.entity_description.update_signal),
            self.handle_update,
        )

        self.entity_id = sensor.ENTITY_ID_FORMAT.format(
            util_slugify(
                f"{self._config.data.get(CONF_NAME)}_{self.entity_description.key}"
            )
        )

        if not isinstance(self._cost_template, Template):
            if self._cost_template in (None, ""):
                self._cost_template = DEFAULT_TEMPLATE
            self._cost_template = cv.template(self._cost_template)
        else:
            if self._cost_template.template in ("", None):
                self._cost_template = cv.template(DEFAULT_TEMPLATE)

    async def handle_attributes(self) -> None:
        """Handle attributes."""
        #if self.entity_description.key == "current_price_vat":
        #    self._attr_extra_state_attributes = {}
        #    price_set: list = []
        #    for price in self.api.prices_today:
        #        price_set.append(
        #            {
        #                "start": price["date"],
        #                "end": price["date"] + timedelta(hours=1),
        #                "price": price["price"]["total"],
        #            }
        #        )

    async def handle_update(self) -> None:
        """Handle data update."""
        try:
            self._attr_native_value = self.entity_description.value_fn(
                self._hass.data[DOMAIN][self._config.entry_id]
            )

            LOGGER.debug(
                "Setting value for '%s' to: %s",
                self.entity_id,
                self._attr_native_value,
            )
            await self.handle_attributes()
            self._attr_available = True
 
        except Exception as e:
            if self._attr_available:
                LOGGER.error("The EnergyMngt API made an invalid response: %s", e)
            self._attr_available = False

    async def async_added_to_hass(self):
        await self.handle_update()
        return await super().async_added_to_hass()


#async def async_setup_entry(hass, entry: ConfigEntry, async_add_entities):
#    """Opsæt sensoren baseret på UI-konfigurationen."""
#    sensor_name = entry.data.get("sensor_name", "Min Sensor")  # Henter sensor-navnet fra entry
#    async_add_entities([RandomNumberSensor(sensor_name)], True)

class RandomNumberSensor(SensorEntity):
    """En simpel sensor, der viser et tilfældigt tal."""

    _attr_device_class = "measurement"
    _attr_native_unit_of_measurement = "units"

    def __init__(self, name):
        """Initialiser sensoren."""
        self._attr_name = name
        self._attr_unique_id = f"sensor_{name.lower().replace(' ', '_')}"
        self._attr_state = None

    async def async_update(self):
        """Opdater sensorens tilstand med et nyt tilfældigt tal."""
        self._state = 33 #random.randint(0, 100)

    @property
    def native_value(self):
        """Returnerer sensorens aktuelle værdi."""
        return self._state
