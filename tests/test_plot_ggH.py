import sys
import ROOT

f = ROOT.TFile.Open('hist_ggH.root')
keys = [k.GetName() for k in f.GetListOfKeys()]

required_keys = ['ggH_pt_1', 'ggH_pt_2']

print('\n'.join(keys))
for required_key in required_keys:
    if not required_key in keys:
        print(f'Required key not found. {required_key}')
        sys.exit(1)

integral = f.ggH_pt_1.Integral()
if abs(integral - 222.88716647028923) > 0.0001:
    print(f'Integral of ggH_pt_1 is different: {integral}')
    sys.exit(1)
