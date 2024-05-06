import cv2
import argparse
import os

def extract_frames(video_path, output_path, frame_interval):
    # Open the video file
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Video file not found or could not be opened.")
        return
    
    # Get the video properties
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = total_frames / fps

    # Extract frames at specified intervals
    frame_count = 0
    success, image = cap.read()
    while success:
        if frame_count % frame_interval == 0:
            frame_filename = f"{output_path}/frame_{frame_count}.jpg"
            cv2.imwrite(frame_filename, image)
        success, image = cap.read()
        frame_count += 1

    cap.release()
    print(f"{int(frame_count / frame_interval)} frames extracted.")

if __name__ == "__main__":
    # Parse arguments
    parser = argparse.ArgumentParser(description="A program to extract frames from a video at specified intervals.")
    parser.add_argument("--source", required=True, help="Path to the video file")
    parser.add_argument("--output", required=True, help="Path to the folder where frames will be saved")
    parser.add_argument("--interval", type=int, default=30, help="Frame interval")
    args = parser.parse_args()

    # Check if the output folder exists, if not create it
    if not os.path.exists(args.output):
        os.makedirs(args.output)

    # Extract frames
    extract_frames(args.source, args.output, args.interval)
