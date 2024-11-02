from MLProject.logger import logging
from MLProject.exception import Exception
from MLProject.pipeline.training_pipeline import TrainPipeline
import sys
import warnings
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)

obj = TrainPipeline()
obj.run_pipeline()