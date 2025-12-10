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
    
    def _count_token_repeats(self, tokens: List[str], varname:str) -> Tuple[int,int]:
        pos = tokens.count(varname)
        neg = tokens.count('-' + varname)
        return pos, neg
    
    def build_augmented_matrix(self) -> None:
        if self.lines is None or self.n is None:
            raise RuntimeError("jer unda gamoidzaxos read_file funqcia")
        n = self.n
        varnames = [f'x{x+1}' for i in range(n)]
        A = np.zeros((n, n), dtype=float)
        B = np.zeros((n, 1), dtype=float)

        for i, line in enumerate(self.lines):
            tokens = line.split()
            for j, v in enumerate(varnames):
                pos, neg = self._count_token_repeats(tokens, v)
                coeff = pos - neg
                A[i ,j] = coeff
            
            posb = tokens.count('b')
            negb = tokens.count('-b')
            B[i, 0] = posb - negb
        
        self.A = A
        self.B = B
    
    def compute_determinants_and_solve(self, eps_zero: float = 1e-12) -> None:

        if self.A is None or self.B is None:
            raise RuntimeError("jer unda gamoidzaxos build argumented matrix funqcia")
        self.detA = float(np.linalg.det(self.A))

        if abs(self.detA) < eps_zero:
            self.dets_replaced = []
            self.solution = None
            self.norm = None
            return
        
        n = self.n
        dets= []
        sols = np.zeros(n, dtype=float)

        for col in range(n):
            Ai = self.A.copy()
            Ai[:, col] = self.B[:, 0]
            detAi = float(np.linalg.det(Ai))
            dets.append(detAi)
            sols[col] = detAi / self.detA

        self.dets_replaced = dets
        self.solution = sols
        self.norm = float(np.linalg.norm(sols))

    def run_all(self) -> None:
        self.read_file()
        self.build_augmented_matrix()
        self.compute_determinants_and_solve()
    
    def summary(self)-> str:
        lines = [f'file: {self.filename}', f'ucnobebi (n): {self.n}', f'det(A): {self.detA}']
        if self.solution is None:
            lines.append('კრამერის მეთოდი მიუდეგარია (det(A) ~ 0)')
        else:
            lines.append(f'ნორმა(solution-ის): {self.norm}')
        return '\n'.join(lines)


    def _count_token_repeats(self, tokens: List[str], varnames:str) -> Tuple[int,int]:
        if self.lines is None or self.n is None:
            raise RuntimeError("pirvelad unda gamoidzaxot read_filei")
        
        n = self.n
        varnames = [f'x {i+1}' for i in range(n)]
        