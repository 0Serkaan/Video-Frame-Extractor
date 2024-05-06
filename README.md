# Video Frame Extractor

This simple Python script is used to extract frames from a video file at specified intervals.

## Installation

1. Download and install Python on your computer. [Python Download Page](https://www.python.org/downloads/)
2. Download the project from GitHub or as a ZIP file and extract it to a folder.
3. Open a terminal or command prompt and navigate to the folder where the project is located:
    ```bash
    cd path/to/video-frame-extractor
    ```
4. Install the required dependencies by running the following command:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

You can extract video frames by running the following command in a terminal or command prompt:

```bash
python extract_frames.py --source 'video.mp4' --output 'frames' --interval 30
--source: Path to the video file.
--output: Path to the folder where frames will be saved.
--interval: Frame interval (default is 30).
For example:

--source 'video.mp4': Specify the name and path of the video file.
--output 'frames': Specify the folder where frames will be saved.
--interval 30: Specify how often frames will be extracted.
Frames will be saved in the specified folder under names like frame_0.jpg, frame_30.jpg, frame_60.jpg, etc.