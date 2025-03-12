"""Entity base definitions."""

from collections.abc import Callable
from dataclasses import dataclass

from homeassistant.components.binary_sensor import BinarySensorEntityDescription
from homeassistant.components.sensor import SensorEntityDescription

from .api import EnergyMngtAPI
from .const import UPDATE_SIGNAL


@dataclass
class EnergyMngtBaseEntityDescriptionMixin:
    """Describes a basic EnergyMngt entity."""

    value_fn: Callable[[EnergyMngtAPI], bool | str | int | float]


@dataclass
class EnergyMngtSensorEntityDescription(
    SensorEntityDescription, EnergyMngtBaseEntityDescriptionMixin
):
    """Describes a EnergyMngt sensor."""

    unit_fn: Callable[[EnergyMngtAPI], None] = None
    update_signal: str = UPDATE_SIGNAL


@dataclass
class EnergyMngtBinarySensorEntityDescription(
    BinarySensorEntityDescription, EnergyMngtBaseEntityDescriptionMixin
):
    """Describes a EnergyMngt sensor."""

    unit_fn: Callable[[EnergyMngtAPI], None] = None