# picked from issue #448

import tensorflow as tf
from grpc.beta import implementations
from tensorflow_serving.apis import predict_pb2
from tensorflow_serving.apis import prediction_service_pb2
import time 

tf.enable_eager_execution()

tf.app.flags.DEFINE_string('server', 'localhost:9000',
                           'PredictionService host:port')
tf.app.flags.DEFINE_string('image', '', 'path to image in JPEG format')
FLAGS = tf.app.flags.FLAGS


def read_tensor_from_image_file(file_name,
                                input_height=299,
                                input_width=299,
                                input_mean=0,
                                input_std=255):
    input_name = "file_reader"
    file_reader = tf.read_file(file_name, input_name)
    if file_name.endswith(".png"):
        image_reader = tf.image.decode_png(
            file_reader, channels=3, name="png_reader")
    elif file_name.endswith(".gif"):
        image_reader = tf.squeeze(
            tf.image.decode_gif(file_reader, name="gif_reader"))
    elif file_name.endswith(".bmp"):
        image_reader = tf.image.decode_bmp(file_reader, name="bmp_reader")
    else:
        image_reader = tf.image.decode_jpeg(
            file_reader, channels=3, name="jpeg_reader")
    float_caster = tf.cast(image_reader, tf.float32)
    dims_expander = tf.expand_dims(float_caster, 0)
    resized = tf.image.resize_bilinear(
        dims_expander, [input_height, input_width])
    normalized = tf.divide(tf.subtract(resized, [input_mean]), [input_std])

    return normalized


def main(args):
    host, port = FLAGS.server.split(':')
    channel = implementations.insecure_channel(host, int(port))
    stub = prediction_service_pb2.beta_create_PredictionService_stub(channel)
    # Send requesti
    image_time = time.time()
    image = read_tensor_from_image_file(FLAGS.image)
    print("time to read tensor from image file: {0}ms".format(int(round((time.time() - image_time) * 1000))))
    request = predict_pb2.PredictRequest()
    request.model_spec.name = 'inception'
    request.model_spec.signature_name = tf.saved_model.signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY
    request.inputs['image'].CopyFrom(tf.contrib.util.make_tensor_proto(image))
    request_time = time.time()
    result = stub.Predict(request, 5.0)  # 10 secs timeout
    print("request time: {0}ms".format(int(round((time.time() - image_time) * 1000))))
    print(result)


if __name__ == '__main__':
    tf.app.run()
