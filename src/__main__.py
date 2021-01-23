import os

import vkquick as vq
import dotenv

from src.commands import sin_via_angle, cos_via_angle, angle_via_sin, angle_via_cos


dotenv.load_dotenv()


group_bot = vq.Bot.init_via_token(
    os.getenv("GROUP_TOKEN")
)

group_bot.add_command(sin_via_angle)
group_bot.add_command(cos_via_angle)
group_bot.add_command(angle_via_sin)
group_bot.add_command(angle_via_cos)

user_bot = group_bot.copy(os.getenv("USER_TOKEN"))

if __name__ == "__main__":
    vq.run_many_bots(
        [group_bot, user_bot]
    )

