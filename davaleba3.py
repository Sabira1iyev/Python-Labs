import os
import numpy as np
from typing import List, Tuple, Optional

class KramerProcess:
    def __init__(self,filename:str):
        self.filename = filename
        self.lines: Optional[np.ndarray] = None
        self.n: Optional[int] = None
        self.A: Optional[np.ndarray] = None
        self.B:Optional[np.ndarray] = None
        self.detA:Optional[float] = None
        self.dets_replaced: Optional[List[float]] = None
        self.solution:Optional[np.ndarray] = None
        self.norm: Optional[float] = None


    def read_file(self) -> None:
        try:
            self.lines = np.loadtxt(self.filename, dtype=str, delimiter='\n', comments = None)
        except Exception:
            with open(self.filename, 'r', encoding="utf-8") as f:
                raw = f.read().splitlines()
            self.lines = np.array(raw, dtype=str)
        
        if isinstance(self.lines,str):
            self.lines = np.array([self.lines],dtype = str)
        self.n = len(self.lines)


    def _count_token_repeats(self, tokens: List[str], varnames:str) -> Tuple[int,int]:
        if self.lines is None or self.n is None:
            raise RuntimeError("pirvelad unda gamoidzaxot read_filei")
        
        n = self.n
        varnames = [f'x {i+1}' for i in range(n)]
        