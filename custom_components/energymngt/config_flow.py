from homeassistant import config_entries
import voluptuous as vol

from .const import DOMAIN  # Sørg for, at du har en const.py-fil

class EnermymngtConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Håndter UI-konfigurationen for enermymngt integrationen."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Trin 1: Brugeren starter opsætningen i UI."""
        errors = {}

        if user_input is not None:
            # Opret en ny entry med det, brugeren har indtastet
            return self.async_create_entry(title="Energi Management Integration", data=user_input)

        # Definerer de nødvendige inputs for brugeren (f.eks. sensor_name)
        schema = vol.Schema(
            {
                vol.Required("sensor_name", default="Min Sensor"): str,
            }
        )

        # Viser formularen til brugeren
        return self.async_show_form(step_id="user", data_schema=schema, errors=errors)
