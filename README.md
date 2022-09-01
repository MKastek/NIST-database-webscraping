## NIST Database webscraping

Help:
```
python NIST_lines.py --help
```
Positional arguments:
```
positional arguments:
  element               Name of element from NIST Database
  line                  Value of wavelength to be searched
  n                     Number of wavelengths to be searched
  filename              Name of the file with output

```
Optional arguments:
```
options:
  -h, --help            show this help message and exit
  --low_w LOW_W         Minimum wavelength value
  --upper_w UPPER_W     Maximum wavelength value
  --sp_num SP_NUM [SP_NUM ...]  List of ionization stages
  --threshold THRESHOLD Intensity threshold
```

# Examples:
```
python NIST_lines.py Ar 811 10 data 
```

Output in file data.csv: 
|    | element   |   sp_num |   obs_wl_air(nm) |   unc_obs_wl |   ritz_wl_air(nm) |   unc_ritz_wl |   intens |   gA(s^-1) | Acc   |   Ei(cm-1) |   Ek(cm-1) | conf_i                | term_i   | J_i   | conf_k                | term_k   | J_k   |   Type | tp_ref   | line_ref   |
|---:|:----------|---------:|-----------------:|-------------:|------------------:|--------------:|---------:|-----------:|:------|-----------:|-----------:|:----------------------|:---------|:------|:----------------------|:---------|:------|-------:|:---------|:-----------|
|  0 | Ar        |        1 |          811.531 |       0.001  |           811.531 |       0.001   |    35000 |    2.3e+08 | B     |    93143.8 |     105463 | 3s2.3p5.(2P*<3/2>).4s | 2[3/2]*  | 2     | 3s2.3p5.(2P*<3/2>).4p | 2[5/2]   | 3     |    nan | T5223    | L2634      |
|  1 | Ar        |        1 |          810.369 |       0.001  |           810.369 |       0.001   |    20000 |    7.5e+07 | B+    |    93750.6 |     106087 | 3s2.3p5.(2P*<3/2>).4s | 2[3/2]*  | 1     | 3s2.3p5.(2P*<3/2>).4p | 2[3/2]   | 1     |    nan | T5223    | L2634      |
|  2 | Ar        |        2 |          810.369 |       2e-05  |           810.369 |       4e-05   |    12023 |  nan       | nan   |   143371   |     155708 | 3s2.3p4.(3P).3d       | 4F       | 3/2   | 3s2.3p4.(3P).4p       | 4P*      | 1/2   |    nan | nan      | L11520     |
|  3 | Ar        |        1 |          805.331 |       0.001  |           805.331 |       0.001   |        7 |    2.6e+06 | C     |   106238   |     118651 | 3s2.3p5.(2P*<3/2>).4p | 2[3/2]   | 2     | 3s2.3p5.(2P*<3/2>).4d | 2[1/2]*  | 1     |    nan | T1218n   | L2634      |
|  4 | Ar        |        2 |          804.376 |       0.002  |           804.375 |       2.6e-05 |        5 |  nan       | nan   |   148620   |     161049 | 3s2.3p4.(1D).4s       | 2D       | 3/2   | 3s2.3p4.(3P).4p       | 4S*      | 3/2   |    nan | nan      | L14821     |
|  5 | Ar        |        2 |          816.54  |       0.0008 |           816.539 |       2.7e-05 |        3 |  nan       | nan   |   143108   |     155351 | 3s2.3p4.(3P).3d       | 4F       | 5/2   | 3s2.3p4.(3P).4p       | 4P*      | 3/2   |    nan | nan      | L14821     |
|  6 | Ar        |        2 |          804.431 |       0.0008 |           804.43  |       2.6e-05 |        2 |  nan       | nan   |   183676   |     196103 | 3s2.3p4.(3P).4d       | 4D       | 7/2   | 3s2.3p4.(3P<1>).4f    | 2[4]*    | 9/2   |    nan | nan      | L14821     |
|  7 | Ar        |        2 |          811.065 |       0.002  |           811.066 |       2.7e-05 |        1 |  nan       | nan   |   142717   |     155043 | 3s2.3p4.(3P).3d       | 4F       | 7/2   | 3s2.3p4.(3P).4p       | 4P*      | 5/2   |    nan | nan      | L14821     |
|  8 | Ar        |        2 |          808.375 |       0.002  |           808.376 |       0.00014 |        1 |  nan       | nan   |   192712   |     205079 | 3s2.3p4.(3P).4d       | 2D       | 3/2   | 3s2.3p4.(3P<2>).5f    | 2[2]*    | 5/2   |    nan | nan      | L14821     |
|  9 | Ar        |        2 |          815.065 |       0.0008 |           815.065 |       0.00013 |        1 |  nan       | nan   |   192712   |     204978 | 3s2.3p4.(3P).4d       | 2D       | 3/2   | 3s2.3p4.(3P<2>).5f    | 2[3]*    | 5/2   |    nan | nan      | L14821     |
