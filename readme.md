# Machine Learning Model Training Visualization

This repository contains code for visualizing the training progress of a machine learning model using TensorFlow/Keras and Matplotlib. It includes a custom callback, `PlotLearning`, which saves the training and validation metrics as a series of images. These images can be compiled into a GIF to visually track the training progress over epochs.

## Repository Structure

- `plot_learning.py`: Contains the `PlotLearning` class, a TensorFlow/Keras callback that logs training metrics and saves them as images after each epoch.
- `train_model.py`: Demonstrates how to use the `PlotLearning` callback within a training script.
- `training_animation.gif`: An animated GIF showing the training progress, generated from the output images of the training script.

## Setup and Running

### Prerequisites

Ensure you have the following installed:
- Python 3.6+
- TensorFlow 2.x
- Matplotlib
- NumPy

You can install the necessary libraries using pip:

```bash
pip install tensorflow matplotlib numpy
```
## Running the Training Script

To run the training script, follow these steps:

1. **Clone the repository** to your local machine:

    ```bash
    git clone <repository-url>
    ```

2. **Navigate to the cloned directory**:

    ```bash
    cd <repository-directory>
    ```

3. **Run the training script**:

    ```bash
    python train_model.py
    ```

This will start the model training process. The `PlotLearning` callback will show images at each epoch.

## Training Visualization

Below is an animated GIF that shows the training progress, visualizing how the model's loss and accuracy evolve over each epoch:

![Training Progress](/images/training_animation.gif)

This GIF is generated automatically by saving plots at each epoch using the `PlotLearning` callback and compiling them into a GIF.

