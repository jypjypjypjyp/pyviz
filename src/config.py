from object_base import *

lines = poses = points = points2 = text_msg = None
type_config_map = {
    "LINE": [Line, (1.0, 0.0, 0.0)],
    "LINE2": [Line, (0.0, 1.0, 0.0)],
    "LINE3": [Line, (0.0, 0.0, 1.0)],
    "LINE4": [Line, (1.0, 0.0, 1.0)],
    "POSE": [Frame, ()],
    "POINT": [PointV, (1.0, 0.0, 0.0)],
    "POINT2": [PointV, (0.0, 1.0, 0.0)],
    "POINT3": [PointV, (1.0, 1.0, 0.0)],
    "TEXT": [Text, (1.0, 0.0, 0.0)],
}
