# Keyboard75
<img width="998" height="695" alt="Screenshot 2026-09-16 233355" src="https://github.com/user-attachments/assets/c123dae7-2937-4cee-b458-c0d36d3c33b0" />

SO I made a custom 75 % layout Mechanical keyboard which has a rotor encoder at the top for brightness controlee as well . It is based on rp2040 chip  . SO I had to design the MCU circuit by myself as well . The PCB was designed on kicad and CAD was done on Fusion . firmware was written in VS-Code. It has a very compact design. The Keyboard also includes per switch LED and diodes to prevent ghosting. It connects to the PC via USB-C input .

## Features
 - Based on Rp2040 chip
 - had compact 75% keyboard layout
 - Per Switch LED and diode for ghosting prevention
 - USB-C Type for Connection
 - Uplifted CAD Design for comfortable typing


##  BOM

| Comment | Footprint | Quantity | Total Price ($) | Link |
|---|---|---:|---:|---|
| 33pF | 0603 | 4 | 0.0236 | https://jlcpcb.com/partdetail/2015-CL10C330JB8NNNC/C1663 |
| 0.1uF | 0603 | 10 | 0.124 | https://jlcpcb.com/partdetail/YAGEO-CC0603KRX7R9BB104/C14663 |
| 100nF | 0603 | 10 | 0.124 | https://jlcpcb.com/partdetail/YAGEO-CC0603KRX7R9BB104/C14663 |
| 10uF | 0603 | 4 | 0.1276 | https://jlcpcb.com/partdetail/20411-CL10A106KP8NNNC/C19702 |
| 1uF | 0603 | 4 | 0.0684 | https://jlcpcb.com/partdetail/16531-CL10A105KB8NNNC/C15849 |
| USB_C_Receptacle_USB2.0_16P | USB_C_Receptacle_G-Switch_GT-USB-7010ASV | 2 | 0.0988 | https://jlcpcb.com/partdetail/DEALON-USB_TYPE_C006/C2927026 |
| 5.1K | 0603 | 4 | 0.0076 | https://jlcpcb.com/partdetail/23913-0603WAF5101T5E/C23186 |
| 1K | 0603 | 4 | 0.0132 | https://jlcpcb.com/partdetail/21904-0603WAF1001T5E/C21190 |
| 27ohm | 0603 | 20 | 0.022 | https://jlcpcb.com/partdetail/23790019-RCA0327RJLF/C22356575 |
| 10K | 0603 | 4 | 0.0108 | https://jlcpcb.com/partdetail/26547-0603WAF1002T5E/C25804 |
| RP2040 | QFN-56-1EP_7x7mm_P0.4mm_EP3.2x3.2mm | 2 | 1.979 | https://jlcpcb.com/partdetail/RaspberryPi-RP2040/C2040 |
| 12MHz | Crystal_SMD_3225-4Pin_3.2x2.5mm | 5 | 2.14 | https://jlcpcb.com/partdetail/KDSDaishinku-DSX321G12MHz/C93234 |
| PCB + 3D Prints Cost | — | 1 | 30.80 | https://jlcpcb.com |
| PCBA Cost | — | 1 | 27.88 | https://jlcpcb.com |
| PCB Shipping | — | 1 | 14.03 | https://jlcpcb.com |
| Hot-swap | — | 90 | 6.75 | https://meckeys.com/shop/accessories/keyboard-accessories/key-switches/kailh-hot-swap-socket/?attribute_pa_variations=white |
| Mechanical Switch | — | 90 | 21.10 | https://meckeys.com/shop/accessories/keyboard-accessories/key-switches/akko-v3-pro-cream-black-switch/ |
| KEY-CAPS | — | 1 | 11.50 | https://meckeys.com/shop/accessories/keyboard-accessories/keycaps/side-engraved-keycap-set/?attribute_pa_pick-your-style=blackberry-side-printed |
| 0.1uF Capacitor | 0603 | 90 | 3.60 | https://sharvielectronics.com/product/0-1uf-16v-capacitor-0603-smd-package/ |
| 1N4007 Diodes | SOD-123FL | 90 | 2.60 | https://sharvielectronics.com/product/a7-1n4007-100v-1a-silicon-rectifier-diode-sod-123fl-smd-package/ |
| SK6812MINI-E | — | 90 | 8.10 | https://www.etstore.in/products/e9974?variant=48993209319675 |
| Components Shipping | — | 1 | 3.30 | https://www.etstore.in/ |
| **TOTAL** | — | — | **$132.67** | — |


### Schematic<br><br>
<img width="1145" height="487" alt="Screenshot 2026-09-17 152250" src="https://github.com/user-attachments/assets/29d6a225-76d8-4742-9a19-9c49ef642b64" />

###  PCB Design<br><br>
<img width="1145" height="478" alt="Screenshot 2026-09-17 010254" src="https://github.com/user-attachments/assets/7142dd1e-be23-40dc-8cad-d427951c3c95" />
<img width="1428" height="595" alt="Screenshot 2026-09-14 191653" src="https://github.com/user-attachments/assets/c4afff5c-2307-4906-a571-6005fceb05f3" />

### 3D Render <br><br>
<img width="998" height="695" alt="Screenshot 2026-09-16 233355" src="https://github.com/user-attachments/assets/75386767-fe08-4e1e-bc64-4f97e4780715" />
<img width="676" height="437" alt="Screenshot 2026-09-16 233434" src="https://github.com/user-attachments/assets/01c7b3e3-fad2-4b3a-b18d-bbaee34f60a0" />







