# Blur

A Python script that applies a Gaussian blur and gamma correction to images. It can process a single image or an entire directory of images in batch.

## What it does

1. Applies a two-pass Gaussian blur (horizontal then vertical) to each image
2. Applies gamma correction (gamma = 1.5) to brighten the blurred result
3. Saves the output to the specified location

When processing a directory, it automatically creates a `blurred/` subdirectory inside the input directory and saves all processed images there with their original filenames.

### Supported image formats

`.png`, `.jpg`, `.jpeg`, `.bmp`, `.tiff`, `.tif`, `.webp`

## Dependencies

### Python

- **Python 3.6+** is required (uses f-strings and `os.makedirs` with `exist_ok`)

### Python packages

| Package | Version | Purpose |
|---------|---------|---------|
| **OpenCV** (`cv2`) | 4.x recommended | Image reading, Gaussian blur, and writing |
| **NumPy** (`numpy`) | 1.x or 2.x | Gamma correction lookup table generation |

Both are third-party packages and must be installed separately.

### Installing dependencies

Using pip:

```bash
pip install opencv-python numpy
```

Or with pip3 explicitly:

```bash
pip3 install opencv-python numpy
```

> **Note:** The PyPI package is called `opencv-python`, but it is imported as `cv2` in Python.

If you only need the core modules without GUI support (e.g. on a headless server), you can use the headless variant instead:

```bash
pip install opencv-python-headless numpy
```

## Usage

### Blur a single image

```bash
python3 blur.py <input_image> <output_image>
```

Example:

```bash
python3 blur.py photo.png photo_blurred.png
```

### Blur all images in a directory

```bash
python3 blur.py <directory>
```

Example:

```bash
python3 blur.py /Users/you/Photos/vacation
```

This will create a `blurred/` folder inside the given directory and save all blurred images there.

## Configuration

The blur intensity can be changed by editing the constants at the top of `blur.py`:

```python
BLUR_LOW = 20
BLUR_MED = 50    # default
BLUR_HIGH = 100
```

The script uses `BLUR_MED` (50) by default. To use a different level, modify the `blur_level` parameter in the `blur_image()` function call.
