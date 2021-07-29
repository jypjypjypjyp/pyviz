from object_base import *

lines = poses = points = points2 = text_msg = None
type_config_map = {
    'LINE': [Line, (1., 0., 0.)],
    'POSE': [Frame, ()],
    'POINT': [PointV, (0., 1., 0.)],
    'POINT2': [PointV, (0., 0., 1.)],
    'TEXT': [Text, (1., 0., 0.)]}
# type_msg_map = {
#     'LINE': lines,
#     'POSE': poses,
#     'POINT': points,
#     'POINT2': points2,
#     'TEXT': text_msg}
# msg_color_map = {
#     'LINE': (1, 0, 0),
#     'POSE': (),
#     'POINT': (0, 1, 0),
#     'POINT2': (0, 0, 1),
#     'TEXT': (1, 0, 0)}
