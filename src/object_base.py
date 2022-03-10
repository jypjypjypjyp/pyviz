from abc import ABCMeta, abstractclassmethod
import genpy
from visualization_msgs.msg import Marker, MarkerArray
from geometry_msgs.msg import Pose, PoseArray
from geometry_msgs.msg import Point
import copy


class MessageWithParam:
    def __init__(self, msg: genpy.Message, **kwds):
        for k, v in kwds.items():
            setattr(self, k, v)
        self.msg = msg


class ObjectBase(metaclass=ABCMeta):
    def __init__(self, object_split):
        self.id = int(object_split[0])
        self.type = object_split[1]

    @abstractclassmethod
    def draw(self, msg):
        pass

    @abstractclassmethod
    def create_msg(ts, *param):
        pass


class Line(ObjectBase):
    def __init__(self, object_split):
        if len(object_split) != 8:
            raise ValueError()
        ObjectBase.__init__(self, object_split)
        self.a = Point()
        self.a.x = float(object_split[2])
        self.a.y = float(object_split[3])
        self.a.z = float(object_split[4])
        self.b = Point()
        self.b.x = float(object_split[5])
        self.b.y = float(object_split[6])
        self.b.z = float(object_split[7])

    def draw(self, msg: Marker):
        msg.points.append(self.a)
        msg.points.append(self.b)

    def create_msg(ts, *param):
        lines = Marker()
        lines.header.stamp = ts
        lines.header.frame_id = "world"
        lines.type = Marker.LINE_LIST
        lines.id = 999999999
        lines.action = Marker.MODIFY
        lines.pose.orientation.w = 1
        lines.scale.x = 0.1
        lines.color.r = param[0]
        lines.color.g = param[1]
        lines.color.b = param[2]
        lines.color.a = 1
        return lines

    def msg_type():
        return Marker


class Frame(ObjectBase):
    def __init__(self, object_split):
        if len(object_split) != 9:
            raise ValueError()
        ObjectBase.__init__(self, object_split)
        self.pose = Pose()
        self.pose.orientation.w = float(object_split[2])
        self.pose.orientation.x = float(object_split[3])
        self.pose.orientation.y = float(object_split[4])
        self.pose.orientation.z = float(object_split[5])
        self.pose.position.x = float(object_split[6])
        self.pose.position.y = float(object_split[7])
        self.pose.position.z = float(object_split[8])

    def draw(self, msg: PoseArray):
        msg.poses.append(self.pose)

    def create_msg(ts, *param):
        poses = PoseArray()
        poses.header.stamp = ts
        poses.header.frame_id = "world"
        return poses

    def msg_type():
        return PoseArray


class PointV(ObjectBase):
    def __init__(self, object_split):
        if len(object_split) != 5:
            raise ValueError()
        ObjectBase.__init__(self, object_split)
        self.a = Point()
        self.a.x = float(object_split[2])
        self.a.y = float(object_split[3])
        self.a.z = float(object_split[4])

    def draw(self, msg: Marker):
        msg.points.append(self.a)

    def create_msg(ts, *param):
        points = Marker()
        points.header.stamp = ts
        points.header.frame_id = "world"
        points.type = Marker.POINTS
        points.id = 999999998
        points.action = Marker.MODIFY
        points.pose.orientation.w = 1
        points.scale.x = 0.2
        points.scale.y = 0.2
        points.color.r = param[0]
        points.color.g = param[1]
        points.color.b = param[2]
        points.color.a = 1
        return points

    def msg_type():
        return Marker


class Text(ObjectBase):
    marker_template = Marker()

    @classmethod
    def init_template(cls):
        cls.marker_template.header.frame_id = "world"
        cls.marker_template.type = Marker.TEXT_VIEW_FACING
        cls.marker_template.action = Marker.MODIFY
        cls.marker_template.pose.orientation.w = 1
        cls.marker_template.scale.z = 1
        cls.marker_template.color.a = 1

    def __init__(self, object_split):
        if len(object_split) != 10:
            raise ValueError()
        ObjectBase.__init__(self, object_split)
        self.text = copy.deepcopy(self.marker_template)
        self.text.pose.orientation.w = float(object_split[2])
        self.text.pose.orientation.x = float(object_split[3])
        self.text.pose.orientation.y = float(object_split[4])
        self.text.pose.orientation.z = float(object_split[5])
        self.text.pose.position.x = float(object_split[6])
        self.text.pose.position.y = float(object_split[7])
        self.text.pose.position.z = float(object_split[8])
        self.text.text = object_split[9]

    def draw(self, msg: MessageWithParam):
        self.text.header.stamp = msg.ts
        self.text.color.r = msg.r
        self.text.color.g = msg.g
        self.text.color.b = msg.b
        self.text.id = self.id
        msg.msg.markers.append(self.text)

    def create_msg(ts, *param):
        aaa = MarkerArray()
        aaa.markers = []
        text_array = MessageWithParam(aaa, ts=ts, r=param[0], g=param[1], b=param[2])
        return text_array

    def msg_type():
        return MarkerArray


Text.init_template()
