from strictjson import strict_json_async

from llm import llm
from prompts import GEN_SYS_PROMPT, GEN_USER_PROMPT
from user import User

num = 5
description = "Simulate 3 characters discussing the recent Nobel Prize Awards"


# need three usernames, bios, interests


async def generate_profiles(description, num):
    user_prompt = GEN_USER_PROMPT.format(description, num)
    system_prompt = GEN_SYS_PROMPT

    result = await strict_json_async(
        system_prompt=system_prompt,
        user_prompt=user_prompt,
        output_format={
            "names": f"A list containing {num} names for each user, type: List[str]",
            "bios": f"A list containing {num} bios for each user, type: List[str]",
            "interests": f"A list of interests for {num} users, type: List[List[str]]",
        },
        llm=llm,
    )
    return result
