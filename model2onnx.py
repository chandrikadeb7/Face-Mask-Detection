
# import the necessary packages
from tensorflow.keras.models import load_model, save_model
import argparse
import tf2onnx
import onnx

def model2onnx():
	# construct the argument parser and parse the arguments
	ap = argparse.ArgumentParser()
	ap.add_argument("-m", "--model", type=str,
		default="mask_detector.model",
		help="path to trained face mask detector model")
	ap.add_argument("-o", "--output", type=str,
		default='mask_detector.onnx',
		help="path to trained face mask detector model")
	args = vars(ap.parse_args())


	# load the face mask detector model from disk
	print("[INFO] loading face mask detector model...")
	model = load_model(args["model"])
	onnx_model, _ = tf2onnx.convert.from_keras(model, opset=13)

	onnx_model.graph.input[0].type.tensor_type.shape.dim[0].dim_param = '?'
	onnx_model.graph.output[0].type.tensor_type.shape.dim[0].dim_param = '?'

	onnx.save(onnx_model, args['output'])


if __name__ == "__main__":
	model2onnx()
