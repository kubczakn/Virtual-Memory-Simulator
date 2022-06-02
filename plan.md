# Things to specify:
- Number of VPN bits
- Number of PPN bits
- Number of page table levels (start with single level)
- Size of a page
- Instruction being loaded in 
- Different processes? 

# Eviction Policy
- LRU

# Input Contraints
- Certain inputs must be powers of two 
- Limit on how large inputs can be 
- Fix the size of VPN and/or PPN bits?  
  -  Fix VPN bits, allow for variable PPN bits

# Design
- Represent disk as a list 
- Represent page table as a list 
- global pager class for flask app 
  - endpoints interact with global pager 
- have certain physical pages initially reside in physical memory 
