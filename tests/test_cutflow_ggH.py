import sys

logfile = open('skim_ggH.log', 'r')
lines = [line.rstrip() for line in logfile]

required_lines = [
   'Number of events: 47696',
   'Cross-section: 19.6',
   'Integrated luminosity: 11467',
   'Global scaling: 0.1',
   'Passes trigger: pass=3402       all=47696      -- eff=7.13 % cumulative eff=7.13 %',
   'nMuon > 0 : pass=3402       all=3402       -- eff=100.00 % cumulative eff=7.13 %',
   'nTau > 0  : pass=3401       all=3402       -- eff=99.97 % cumulative eff=7.13 %',
   'Event has good taus: pass=846        all=3401       -- eff=24.88 % cumulative eff=1.77 %',
   'Event has good muons: pass=813        all=846        -- eff=96.10 % cumulative eff=1.70 %',
   'Valid muon in selected pair: pass=813        all=813        -- eff=100.00 % cumulative eff=1.70 %',
   'Valid tau in selected pair: pass=813        all=813        -- eff=100.00 % cumulative eff=1.70 %',
]

print('\n'.join(lines))
for required_line in required_lines:
    if not required_line in lines:
        print(f'Did not find line in log file. {required_line}')
        sys.exit(1)
