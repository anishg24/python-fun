import math
from matplotlib import pyplot as plt

class Gaussian():
    """
    Gaussian Distribution class for calculating and visualizing a Gaussian distribution
    
    Attributes:
        mean (float) - represents the mean value of the distribution
        stdev (float) - represents the standard deviation of the distribution
        data_list (list of floats) - list of floats extracted from a data file
    """
    
    def __init__(self, mu = 0, sigma = 1):
        self.mean = mu
        self.stdev = sigma
        self.data = [] 
        
    def calculate_mean(self):
        """
        Method to calculate the mean of the data set
        
        Args:
            None
        Returns:
            float - mean of the dataset
        """
        avg = 1.0 * sum(self.data) / len(self.data)
        self.mean = avg
        return self.mean
    
    def calculate_stdev(self, sample=True):
        """
        Method to calculate standard deviation of a dataset
        
        Args:
            sample (bool) - does the dataset represent sample or the population
        Returns:
            float - standard deviation of the dataset
        """
        if sample:
            n = len(self.data) - 1
        else:
            n = len(self.data)
            
        mean = self.mean
        sigma = 0
        
        for d in self.data:
            sigma += (d-mean)**2
        sigma = math.sqrt(sigma/n)
        self.stdev = sigma
        
        return self.stdev
    
    def read_data_file(self, file_name, sample=True):
        """
        Method to read data from a file. The file should have one number (float) per line.
        The numbers are stored in the data attribute. The mean and standard deviation are
        calculated after reading data from the file. 
        
        Args:
            file_name (string) - name of the file to read data from. 
        
        Returns:
            Nothing
        """
        
        with open(file_name) as f: 
            data_list = []
            line = f.readline()
            while line:
                data_list.append(float(line))
                line = f.readline()
            f.close()
            
            self.data = data_list
            self.mean = self.calculate_mean()
            self.stdev = self.calculate_stdev(sample)
            
    def plot_histogram(self):
        """
        Method to plot a histogram of data using matplotlib pyplot library. 
        
        Args:
            None
            
        Returns:
            Nothing
        """
        
        plt.hist(self.data)
        plt.title('Histogram')
        plt.xlabel('Data')
        plt.ylabel('Count')
        plt.text(2, 4, rf'$\mu={self.mean}, b=3${self.stdev}')
        
    
    def probability_density_function(self, x):
        """
        Method to calculate probability density function (pdf) for gaussian distribution.
        
        Args: 
            x (float) - point for calculating pdf
            
        Returns:
            float - pdf output
        """
        
        return (1.0 / (self.stdev * math.sqrt(2*math.pi))) * math.exp(-0.5*((x - self.mean) / self.stdev) ** 2)
    
    def plot_histogram_pdf(self, n_spaces=50):
        """
        Method to plot the normalized histogram of the data and plot 
        pdf along the same range
        
        Args:
            n_spaces (int) - number of data points
            
        Returns:
            list: x-values for the pdf plot
            list: y-values for the pdf plot
        """
        
        mu = self.mean
        sigma = self.stdev
        
        min_range = min(self.data)
        max_range = max(self.data)
        
        # calculate the interval between x values
        interval = 1.0 * (max_range - min_range) / n_spaces
        
        x = []
        y = []
        
        # calculate x values to visualize
        for i in range(n_spaces):
            tmp = min_range + interval * i
            x.append(tmp)
            y.append(self.probability_density_function(tmp))
            
        # render the plots
        figure, axes = plt.subplots(2, sharex=True)
        figure.subplots_adjust(hspace=.5)
        axes[0].hist(self.data, density=True)
        axes[0].set_title('Normed histogram of data')
        axes[0].set_ylabel('Density')
        
        axes[1].plot(x, y)
        axes[1].set_title('Normal Distribution for \n sample mean and sample standard deviation')
        axes[1].set_ylabel('Density')
        plt.show()
        
        return x, y

# Create an object of type Gaussian, feed it a text file of numbers and have the 
#  object calculate mean, standard deviation. Also, plot a histogram of the distribution.
file = "/Users/anishg/Desktop/Python/gaussian.txt"
gauss = Gaussian()
gauss.read_data_file(file)
print(gauss.calculate_mean())
print(gauss.calculate_stdev())
gauss.plot_histogram()
plt.show()
