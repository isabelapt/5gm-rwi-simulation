import os
import numpy as np

try:
    import tensorflow as tf
except ImportError:
    tf = None

try:
    from rwisimulation.positionmatrix import position_matrix_per_object_shape
except ImportError:
    position_matrix_per_object_shape = None

working_directory = os.path.dirname(os.path.realpath(__file__))
# Directory where the RWI project will run on
base_insite_project_path = os.path.join(working_directory, 'SimpleFunciona')
# InSite project path
setup_path = os.path.join(base_insite_project_path, 'model.setup')
setup_path = setup_path.replace(' ', '\ ')
# Where the InSite project will store the results (Study Area name)
project_output_dir = os.path.join(base_insite_project_path, 'study')
# Name (basename) of the paths file generated in the simulation
paths_file_name = 'model.paths.t001_01.r002.p2m'
# Base object file to generate the `object_dst_file_name`
base_object_file_name = os.path.join(base_insite_project_path, "base.object")
# Object which will be modified in the RWI project
dst_object_file_name = os.path.join(base_insite_project_path, "random-line.object")
# Base txrx file to generate the `txrx_dst_file_name`
base_txrx_file_name = os.path.join(base_insite_project_path, "base.object")
# txrx which will be modified in the RWI project
dst_txrx_file_name = os.path.join(base_insite_project_path, 'model.txrx')

# dimensions of the cars which will be placed on `dst_object_file_name`
car_dimensions = (1.76, 4.54, 1.47)
# id of the car material (must be defined on `base_object_file_name`)
car_material_id = 0
car_structure_name = 'car'
# name of the antenna points in `base_txrx_file_name`
antenna_points_name = 'Rx'
# antenna to be placed above the cars
antenna_origin = (car_dimensions[0] / 2, car_dimensions[1] / 2, car_dimensions[2])
# origin and destination of the line to place the cars
line_origin = (648, 456, 0.2)
line_destination = 531
# dimension `line_destination` is indicating to
line_dimension = 1
# distance between cars
def car_distances():
    return np.random.uniform(1, 3)

# Where to store the results (will create subfolders for each "run")
results_dir = os.path.join(working_directory, 'restuls')
def base_run_dir_fn(i):
    """returns the `run_dir` for run `i`"""
    return "run{:05d}".format(i)
n_run = 2
# Copy of the RWI project used in the simulation
results_base_model_dir = os.path.join(results_dir, 'base')
# TFRecord compression, can be NONE
tfrecord_compression = 'GZIP'
# Generated TFRecord
tfrecord_file_name = os.path.join(results_dir, 'rwi.tfrecord')



tfrecord_options = tf.python_io.TFRecordOptions(
    eval('tf.python_io.TFRecordCompressionType.{}'.format(tfrecord_compression))
) \
    if tf is not None else None

# where to map the received to TFRecords (minx, miny, maxx, maxy)
analysis_area = (633, 456, 663, 531)
analysis_area_resolution = 0.5
antenna_number = 4

position_matrix_shape = position_matrix_per_object_shape(analysis_area, analysis_area_resolution) \
    if position_matrix_per_object_shape is not None else None
best_tx_rx_shape = (2,)

#tfrecord_file_name = '/Users/psb/ownCloud/Projects/DNN Wireless/rwi-simulation/rwi.tfrecord'
#tfrecord_file_name = '/Users/psb/ownCloud/Projects/DNN Wireless/tempmm/rwi-simulation/rwi.tfrecord'
tfrecord_file_name = os.path.join(results_dir, 'rwi.tfrecord')

#calcprop_bin = r'"C:\Program Files\Remcom\Wireless InSite 3.2.0.3\bin\calc\calcprop"'
calcprop_bin = ('REMCOMINC_LICENSE_FILE=/home/psb/ownCloudMBP/Projects/DNN\ Wireless/WI32_UFPA1_DEMO_180224.lic ' +
                'LD_LIBRARY_PATH=/home/psb/insite/remcom/OpenMPI/1.4.4/Linux-x86_64RHEL6/lib/:' +
                '/home/psb/insite/remcom/WirelessInSite/3.2.0.3/Linux-x86_64RHEL6/bin/ ' +
                '/home/psb/insite/remcom/WirelessInSite/3.2.0.3/Linux-x86_64RHEL6/bin/calcprop_3.2.0.3')
