# the authors' name are: Mac & Maggie
import math
val_1_radi = 4
val_2_hypo = math.sqrt(val_1_radi**2 + val_1_radi**2)
val_3_sqsf = val_2_hypo * val_2_hypo
val_4_cisf = math.pi * (val_1_radi**2)
answer = val_4_cisf - val_3_sqsf
print("Area of circle = ", val_4_cisf)
print("Area of square = ", val_3_sqsf)
print("Area of the shaded area =", answer)
