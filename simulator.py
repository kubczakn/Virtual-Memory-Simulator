import math
from dataclasses import dataclass
from typing import Tuple, List

DISK_SIZE = 2048


@dataclass 
class PageTableEntry:
	"""Class representing an entry in the page table."""
	ppn: int
	lru: int
	valid: int

# TODO: Implement shadow page table to keep track of vpn -> ppn mappings 

class Pager():
	"""Representation of a memory pager."""
	def __init__(self, v_mem_size: int, p_mem_size: int, page_size: int):
		"""Initialize pager with provided configuration."""

		def init_disk_and_phys_mem() -> Tuple(List[List[int]], List[List[int]]):
			"""Create data structures for physical memory and disk."""
			num_p_mem_pages = p_mem_size / page_size
			num_disk_pages = DISK_SIZE / page_size
			p_mem = [[0] * page_size for _ in num_p_mem_pages]
			disk = [[0] * page_size for _ in num_disk_pages]
			return p_mem, disk

		vpn_bits = math.log(v_mem_size, 2) - math.log(page_size) 
		self.pt = [PageTableEntry()] * pow(vpn_bits, 2) 
		self.p_mem, self.disk = init_disk_and_phys_mem

	
	def extract_vpn_and_page_offset(self, virtual_address: int) -> Tuple[int, int]:
		"""Extract virtual page number and page offset from given virtual
			address."""
		return 0, 0


	def page_table_access(self, vpn: int):
		"""Access the page table with the given virtual page number.
		   Return corresponding physical page number if access was a 
		   	hit, otherwise return -1.
		"""

		return -1

 
	def handle_page_fault(self) -> int:
		"""Handle page fault by bringing in the corresponding page from
			disk."""
		return 0
	

	def mem_access(self, virtual_address: int):
		"""Perform memory access on given virtual address."""
		vpn, page_offset = self.extract_vpn_and_page_offset(virtual_address)
		ppn = self.page_table_access(vpn)
		page_fault = ppn == -1
		if page_fault:
			ppn = self.handle_page_fault()
		
		mem_data = self.p_mem[ppn][page_offset]
		return
