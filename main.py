import math
from scipy.constants import N_A, elementary_charge

# constants
faraday_constant = N_A * elementary_charge #C

# gibbs free energy of formation
s_h2 =
gf_h2 = h_h2 + T * s_h2 #J
gf_o2 = h_o2 + T * s_o2 #J
gf_h2o = h_h2o + T * s_h2o #J
delta_gf_pemfc = delta_gf_h2o - delta_gf_h2 - 0.5 * delta_gf_o2


ocv =  - delta_gf_pemfc / (2 * faraday_constant) #V


