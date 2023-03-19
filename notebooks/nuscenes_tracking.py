# Apply 3D tracking
# Dataset: Nuscenes
# Major packages: 
# 1. https://github.com/eddyhkchiu/mahalanobis_3d_multi_object_tracking 
# 2. https://github.com/nutonomy/nuscenes-devkit.git

from nuscenes import NuScenes
from nuscenes.eval.common.data_classes import EvalBoxes
from nuscenes.eval.tracking.data_classes import TrackingBox 
from nuscenes.eval.detection.data_classes import DetectionBox 
from nuscenes.utils.data_classes import LidarPointCloud, RadarPointCloud, Box

import matplotlib.pyplot as plt






