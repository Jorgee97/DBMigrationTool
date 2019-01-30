from MigrationTool.core import migrate_database
from MigrationTool.constants import MIGRATE_ALL, MIGRATE_TABLES, MIGRATE_TABLES_DATA, MIGRATE_TABLES_VIEW, \
    MSSQL_TO_POSTGRESQL
from MigrationTool.helpers import EngineDetails
from appJar import gui


def checkbox_options(checkbox):
    if checkbox == MIGRATE_ALL and app.getCheckBox(MIGRATE_ALL):
        app.setCheckBox(MIGRATE_TABLES_VIEW, False)
        app.setCheckBox(MIGRATE_TABLES, False)
        app.setCheckBox(MIGRATE_TABLES_DATA, False)
    elif checkbox == MIGRATE_TABLES and app.getCheckBox(MIGRATE_TABLES):
        app.setCheckBox(MIGRATE_TABLES_VIEW, False)
        app.setCheckBox(MIGRATE_ALL, False)
        app.setCheckBox(MIGRATE_TABLES_DATA, False)
    elif checkbox == MIGRATE_TABLES_DATA and app.getCheckBox(MIGRATE_TABLES_DATA):
        app.setCheckBox(MIGRATE_TABLES_VIEW, False)
        app.setCheckBox(MIGRATE_TABLES, False)
        app.setCheckBox(MIGRATE_ALL, False)
    elif checkbox == MIGRATE_TABLES_VIEW and app.getCheckBox(MIGRATE_TABLES_VIEW):
        app.setCheckBox(MIGRATE_ALL, False)
        app.setCheckBox(MIGRATE_TABLES, False)
        app.setCheckBox(MIGRATE_TABLES_DATA, False)


def validate_all_fields_filled():
    if app.getOptionBox("12") is None:
        app.infoBox("Error2", "You most select an available migration.")
        return False

    for entry in app.getAllEntries():
        if app.getAllEntries()[entry] == "":
            app.infoBox("Error1", "All the fields most be completed to proceed.")
            return False
    return True


def press(btn_name):
    if btn_name == "Cancel":
        app.stop()

    drivers = app.getOptionBox("12")
    if validate_all_fields_filled():
        drivers = drivers.split('_')
        actual_database = EngineDetails(
            drivers[0],
            app.getEntry("username"),
            app.getEntry("password"),
            app.getEntry("host"),
            app.getEntry("database_name"))
        target_database = EngineDetails(
            drivers[1],
            app.getEntry("t_username"),
            app.getEntry("t_password"),
            app.getEntry("t_host"),
            app.getEntry("t_database_name"))

        option = [x for x in app.getAllCheckBoxes() if app.getAllCheckBoxes()[x] is True]
        migrate_database(MSSQL_TO_POSTGRESQL, actual_database, target_database, option[0], app)


if __name__ == '__main__':

    app = gui("Database Migration Tool")
    app.setSticky("nesw")
    app.setExpand("both")
    app.setFont(10)

    app.addLabel("11", "Select the migration you want to do:", 0, 0)
    app.addOptionBox("12", ["- Available Migrations -", MSSQL_TO_POSTGRESQL], 0, 1)

    # Actual database divisor
    with app.labelFrame("Actual database details"):
        app.addLabel("13", "Username:", 0, 0)
        app.addEntry("username", 0, 1)

        app.addLabel("14", "Password:", 1, 0)
        app.addEntry("password", 1, 1)

        app.addLabel("15", "Host (add port if necessary): ", 2, 0)
        app.addEntry("host", 2, 1)

        app.addLabel("16", "Database Name: ", 3, 0)
        app.addEntry("database_name", 3, 1)

    # Target database divisor
    with app.labelFrame("Target database details", row=1, column=1):
        app.addLabel("17", "Username:", 0, 0)
        app.addEntry("t_username", 0, 1)

        app.addLabel("18", "Password:", 1, 0)
        app.addEntry("t_password", 1, 1)

        app.addLabel("19", "Host (add port if necessary): ", 2, 0)
        app.addEntry("t_host", 2, 1)

        app.addLabel("20", "Database Name: ", 3, 0)
        app.addEntry("t_database_name", 3, 1)

    app.addCheckBox(MIGRATE_TABLES, row=2, column=0)
    app.addCheckBox(MIGRATE_TABLES_DATA, row=2, column=1)
    app.addCheckBox(MIGRATE_TABLES_VIEW, row=3, column=0)
    app.addCheckBox(MIGRATE_ALL, row=3, column=1)

    app.setCheckBox(MIGRATE_TABLES_DATA, True)
    app.setCheckBoxChangeFunction(MIGRATE_TABLES, checkbox_options)
    app.setCheckBoxChangeFunction(MIGRATE_TABLES_DATA, checkbox_options)
    app.setCheckBoxChangeFunction(MIGRATE_TABLES_VIEW, checkbox_options)
    app.setCheckBoxChangeFunction(MIGRATE_ALL, checkbox_options)

    # Progress bar to inform the user
    app.addMeter("progress", row=4, colspan=2)
    app.setMeterFill("progress", "green")

    app.addButton("Proceed", press, row=5, column=0)
    app.addButton("Cancel", press, row=5, column=1)

    app.go()


