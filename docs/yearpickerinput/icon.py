import dash_mantine_components as dmc
from dash_iconify import DashIconify

component = dmc.YearPickerInput(
    leftSection=DashIconify(icon="fa:calendar"),
    leftSectionPointerEvents="none",
    label="Pick date",
    placeholder="Pick date",
)