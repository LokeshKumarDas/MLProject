from MLProject.logger import logging
from MLProject.exception import Exception
from MLProject.pipeline.training_pipeline import TrainPipeline
import sys

obj = TrainPipeline()
obj.run_pipeline()