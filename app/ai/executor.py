from app.ai.tools import (
    get_order_status,
    check_inventory,
    get_cargo_status,
    get_dashboard_summary
)


def execute_tool(data: dict):

    tool = data.get(
        "tool"
    )

    parameters = data.get(
        "parameters", {}
    )


    if tool == "get_order_status":

        return get_order_status(
            parameters.get(
                "order_id"
            )
        )


    if tool == "check_inventory":

        return check_inventory()


    if tool == "get_cargo_status":

        return get_cargo_status(
            parameters.get(
                "tracking_id"
            )
        )


    if tool == "get_dashboard_summary":

        return get_dashboard_summary()


    return {
        "error": "tool_not_found"
    }