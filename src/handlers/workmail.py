import pandas as pd
import numpy as np
from dotenv import load_dotenv
import boto3
import botocore
import openai
from pydantic import BaseModel

# pip install boto3>=1.26.0 botocore==1.38.29 numpy==1.26.4 pandas==2.3.0 pydantic==2.11.5 openai==1.86.0 python-dotenv==1.1.01

# load_dotenv()

def lambda_handler(event, context):
    return {"message": "Test Lambda ran successfully"}
