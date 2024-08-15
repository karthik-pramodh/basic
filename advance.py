import jetson.inference # type: ignore
import jetson.utils # type: ignore
import argparse
import sys

# Set up the argument parser
parser = argparse.ArgumentParser(description="Detect objects in a live camera stream using an object detection network.",
                                 formatter_class=argparse.RawTextHelpFormatter,
                                 epilog=jetson.inference.detectNet.Usage())

# Parse the command line
parser.add_argument("input_URI", type=str, default="", nargs='?', help="URI of the input stream")
parser.add_argument("output_URI", type=str, default="", nargs='?', help="URI of the output stream")
parser.add_argument("--network", type=str, default="ssd-mobilenet-v2", help="Pre-trained model to load (see below for options)")
parser.add_argument("--overlay", type=str, default="box,labels,conf", help="Detection overlay flags (e.g., overlay=box,labels,conf)")
parser.add_argument("--threshold", type=float, default=0.5, help="Minimum detection threshold to use")

args = parser.parse_args()

# Load the network
net = jetson.inference.detectNet(args.network, sys.argv, args.threshold)

# Create video sources
input = jetson.utils.videoSource(args.input_URI)  # '/dev/video0' for webcam
output = jetson.utils.videoOutput(args.output_URI)  # 'display://0' for displaying on screen

# Process the stream
while True:
    # Capture the next image
    img = input.Capture()

    # Detect objects in the image
    detections = net.Detect(img, overlay=args.overlay)

    # Render the detections
    output.Render(img)

    # Exit if 'q' is pressed
    if not output.IsStreaming() or jetson.utils.glDisplay.IsClosed():
        break