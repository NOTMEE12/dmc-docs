import dash_mantine_components as dmc

from lib.configurator import Configurator

TARGET_ID = "interactive-select-position"

target = dmc.Select(
    label="Your favorite framework/library",
    data=["React", "Angular", "Svelte", "Vue"],
    value="Vue",
    clearable=True,
    w=400,
    id=TARGET_ID,
)


configurator = Configurator(target, TARGET_ID)

configurator.add_select("dropdownPosition", ["top", "bottom", "flip"], "top")

component = configurator.panel
