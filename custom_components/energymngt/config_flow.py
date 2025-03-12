from homeassistant import config_entries
import voluptuous as vol

from .const import DOMAIN

class EnergymngtConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):

    VERSION = 1

    async def async_step_user(self, user_input=None):

        """Handle a config flow for Stromligning."""
        errors = {}

        if user_input is not None:
            # Create a new entry with what, user has entered
            return self.async_create_entry(title="Energi Management Integration", data=user_input)
            
            
        # Defines needed inputs from user (example: sensor_name)
        schema = vol.Schema(
            {
                vol.Required("sensor_name", default="Min Sensor"): str,
            }
        )

        # Shows formula for user
        return self.async_show_form(step_id="user", data_schema=schema, errors=errors)
