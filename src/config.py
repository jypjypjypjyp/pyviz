from object_base import *

lines = poses = points = points2 = text_msg = None
type_config_map = {
    'LINE': [Line, (1., 0., 0.)],
    'POSE': [Frame, ()],
    'POINT': [PointV, (0., 1., 0.)],
    'POINT2': [PointV, (0., 0., 1.)],
    'TEXT': [Text, (1., 0., 0.)]}
