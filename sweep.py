##################################################################
#
# USER EDITABLE SWEEP SETTINGS
#
#   - this file should be copied and renamed _my_sweep.py
#   - DO NOT alter the two-space indentation in this file
#   - the sweep parameters will be used in the results 
#     directory naming
# 
##################################################################

def sweep_parms():
  ###################################
  # uncomment ONE platform
  ###################################
  #platform = "linux"
  platform = "pan"

  ###################################
  # set the mesh and model
  ###################################
  mesh = "cell01m_HARMONIC_100p"
  model = "generic3d_03"   # using implicit Cer diffusion constant
  #model = "generic3d_04"   # separate Cer diffusion constant

  ###################################
  # list fixed parameters (if any)
  ###################################
  #parms = [["PLCds", 0.5], ["IPRdn", 0.5], ["IPRdf", 3.5]]
  #parms = [["kRyR", 0.0]]
  #parms = [["Dce", 5.0]]
  parms = []

  ###################################
  # list 2D parameter sweep values
  ###################################
  #parmA = "Vdeg"
  #valsA = [0.16, 0.18]
  #parmB = "K3K"
  #valsB = [0.4, 0.43]

  #parmA = "IPRdf"
  #valsA = [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5]
  #parmB = "IPRdn"
  #valsB = [0.4]

  parmA = "VPLC"
  valsA = [0.01, 0.02, 0.03, 0.04, 0.05]
  parmB = "kIPR"
  valsB = [2.0, 4.0, 6.0, 8.0, 10.0, 12.0]

  ###################################
  return platform, mesh, model, parms, parmA, valsA, parmB, valsB

