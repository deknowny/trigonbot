import math

import vkquick as vq



@vq.Command(
    prefixes="/?",
    names=["sin", "син", "s", "с"],
    use_regex_escape=False,
    crave_correct_arguments=False,
    on_invalid_argument={
        "angle": "Передайте угол, для которого "
                 "нужно найти косинус"
    }
)
def sin_via_angle(angle: int = vq.Integer):
    radian_angle = math.radians(angle)
    sin_value = math.sin(radian_angle)
    return f"Синус {angle}\u00B0 равен {sin_value:.4f}"


@vq.Command(
    prefixes="/?",
    names=["cos", "кос", "c", "к"],
    use_regex_escape=False,
    crave_correct_arguments=False,
    on_invalid_argument={
        "angle": "Передайте угол, для которого "
                 "нужно найти косинус"
    }
)
def cos_via_angle(angle: int = vq.Integer):
    radian_angle = math.radians(angle)
    sin_value = math.cos(radian_angle)
    return f"Косинус {angle}\u00B0 равен {sin_value:.4f}"


@vq.Command(
    prefixes="/?",
    names=["asin", "асиг", "as", "ас"],
    use_regex_escape=False,
    crave_correct_arguments=False,
    on_invalid_argument={
        "sin_value": "Передайте дробную часть значения синуса (от -1 до 1),"
                     " для которого нужно найти исходный угол"
    }
)
def angle_via_sin(sin_value: int = vq.Float(min_=-1, max_=1)):
    angle_value = math.asin(sin_value)
    angle_value = math.degrees(angle_value)
    return f"Арксинус {sin_value} равен {angle_value:.4f}\u00B0"


@vq.Command(
    prefixes="/?",
    names=["acos", "акос", "ac", "ак"],
    use_regex_escape=False,
    crave_correct_arguments=False,
    on_invalid_argument={
        "cos_value": "Передайте дробную часть значения косинуса,"
                     " для которого нужно найти исходный угол"
    }
)
def angle_via_cos(cos_value: float = vq.Float):
    angle_value = math.acos(cos_value)
    angle_value = math.degrees(angle_value)
    return f"Арккосинус {cos_value} равен {angle_value:.4f}\u00B0"
