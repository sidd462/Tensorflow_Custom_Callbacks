import matplotlib.pyplot as plt
from IPython.display import clear_output

class PlotLearning(tf.keras.callbacks.Callback):
    def on_train_begin(self, logs={}):
        self.i = 0
        self.x = []
        self.losses = []
        self.val_losses = []
        self.acc = []
        self.val_acc = []
        self.fig = plt.figure()
        
        self.logs = []

    def on_epoch_end(self, epoch, logs={}):
        self.logs.append(logs)
        self.x.append(self.i)
        self.losses.append(logs.get('loss'))
        self.val_losses.append(logs.get('val_loss'))
        self.acc.append(logs.get('accuracy'))
        self.val_acc.append(logs.get('val_accuracy'))
        self.i += 1
        
        clear_output(wait=True)
        
        # Use the 'dark_background' style for a clean and professional look
        plt.style.use('dark_background')
        
        # Creating subplots for better control over layout
        fig, ax1 = plt.subplots(figsize=(10, 6))
        ax1.set_xlabel('Epoch', fontsize=14)
        ax1.set_ylabel('Loss', color='tab:red', fontsize=14)
        ax1.plot(self.x, self.losses, label="Training Loss", color='tab:red')
        ax1.plot(self.x, self.val_losses, label="Validation Loss", color='tab:orange')
        ax1.tick_params(axis='y', labelcolor='tab:red')
        ax1.legend(loc='center left')
        
        # Explicitly turn off the grid
        ax1.grid(False)
        
        # Create a second y-axis for the accuracy
        ax2 = ax1.twinx()
        ax2.set_ylabel('Accuracy', color='tab:blue', fontsize=14)
        ax2.plot(self.x, self.acc, label="Training Accuracy", color='tab:blue', linestyle='--')
        ax2.plot(self.x, self.val_acc, label="Validation Accuracy", color='tab:green', linestyle='--')
        ax2.tick_params(axis='y', labelcolor='tab:blue')
        ax2.legend(loc='center right')
        
        # Turn off grid for the second axis
        ax2.grid(False)
        
        plt.title('Training and Validation Metrics', fontsize=16)
        plt.show()
