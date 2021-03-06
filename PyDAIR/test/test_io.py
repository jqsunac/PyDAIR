import os
import math
import unittest
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna
from PyDAIR.seq.IgSeq import IgSeq
from PyDAIR.io.PyDAIRIO import *

_data_path = os.path.join(os.path.dirname(__file__), 'data/samples')
_result_path = os.path.join(os.path.dirname(__file__), 'data/results')


class Test_pydair_io(unittest.TestCase):
    
    
    def setUp(self):
        self.pydair_input_path  = _data_path + '/sample.1.pydair'
        self.pydair_output_path = _result_path + '/test_output_io.pydair'
    
    
    def test_pydair_io(self):
        pydair_i_fh = PyDAIRIO(self.pydair_input_path, 'r')
        pydair_o_fh = PyDAIRIO(self.pydair_output_path, 'w')
        # read record in PyDAIR flat file
        for igseq in pydair_i_fh.parse():
            # print contents
            print('-----------------------------------------------')
            cdr3_seq = igseq.get_cdr3_data()
            print(cdr3_seq.nucl_seq)
            print(cdr3_seq.prot_seq)
            # write object into new file
            pydair_o_fh.write(igseq)
        print('-----------------------------------------------')
        pydair_i_fh.close()
        pydair_o_fh.close()
    
    
    
    
if __name__ == '__main__':
    unittest.main()

