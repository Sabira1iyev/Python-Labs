import os
import numpy as np
from typing import List, Tuple, Optional

class KramerProcess:
    def __init__(self,filename:str):
        self.filename = filename
        self.lines: Optional[np.ndarray] = none
