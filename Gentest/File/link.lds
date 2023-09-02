OUTPUT_ARCH( "riscv" )

SECTIONS
{
  . = 0x10110000;
  .text : { *(.text) }
  .data : { *(.data) }
}
