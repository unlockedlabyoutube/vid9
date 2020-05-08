import tensorflow as tf

graph_def_file = "yolov2-tiny.pb"
input_arrays = ["input"]
output_arrays = ["output"]

converter = tf.lite.TFLiteConverter.from_frozen_graph(
        graph_def_file, input_arrays, output_arrays)
tflite_model = converter.convert()
open("converted_model.tflite", "wb").write(tflite_model)