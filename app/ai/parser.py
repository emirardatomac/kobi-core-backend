import json


def parse_ai_json(response: str):

    try:

        return json.loads(
            response
        )

    except:

        return {
            "error": "invalid_json",
            "raw_response": response
        }